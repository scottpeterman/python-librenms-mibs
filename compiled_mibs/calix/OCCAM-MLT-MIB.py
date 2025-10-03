# SNMP MIB module (OCCAM-MLT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\calix\OCCAM-MLT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:23 2025
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

(occamGenericMonitorModules,) = mibBuilder.importSymbols(
    "OCCAM-REG-MODULE",
    "occamGenericMonitorModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

occamMltMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    occamMltMib.setRevisions(
        ("2001-04-27 10:51",
         "2007-04-17 00:00",
         "2007-02-22 00:00",
         "2006-09-26 10:00",
         "2006-02-22 01:35")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MltTestType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("force", 2))
    )



class MltTestStatus(TextualConvention, Integer32):
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
        *(("none", 1),
          ("mltBusy", 2),
          ("complete", 3),
          ("portInUse", 4),
          ("inProgress", 5),
          ("mltError", 6),
          ("mltNotResponding", 7))
    )



class MltTestIdentifier(TextualConvention, Integer32):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("statusSuite", 1),
          ("mltSuite", 2),
          ("activeModeVoltages", 3),
          ("highImpedanceModeVoltages", 4),
          ("dcResistance", 5),
          ("capacitance", 6),
          ("loopDetect", 7),
          ("loopLength", 8))
    )



class MltTestHookState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onhook", 1),
          ("offhook", 2),
          ("notAvailable", 3))
    )



class MltTestPassFail(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("notAvailable", 3))
    )



class MltTestRingerResult(TextualConvention, Integer32):
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
        *(("pass", 1),
          ("fail", 2),
          ("notAvailable", 3),
          ("low", 4))
    )



class MltTestYesNo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("notAvailable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MltTestConfig_ObjectIdentity = ObjectIdentity
mltTestConfig = _MltTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1)
)
_MltTestIdentifier_Type = MltTestIdentifier
_MltTestIdentifier_Object = MibScalar
mltTestIdentifier = _MltTestIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 1),
    _MltTestIdentifier_Type()
)
mltTestIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTestIdentifier.setStatus("current")
_MltTestType_Type = MltTestType
_MltTestType_Object = MibScalar
mltTestType = _MltTestType_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 2),
    _MltTestType_Type()
)
mltTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTestType.setStatus("current")


class _MltTestPort_Type(Integer32):
    """Custom type mltTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_MltTestPort_Type.__name__ = "Integer32"
_MltTestPort_Object = MibScalar
mltTestPort = _MltTestPort_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 3),
    _MltTestPort_Type()
)
mltTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltTestPort.setStatus("current")


class _MltDcResistanceRange_Type(Integer32):
    """Custom type mltDcResistanceRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MltDcResistanceRange_Type.__name__ = "Integer32"
_MltDcResistanceRange_Object = MibScalar
mltDcResistanceRange = _MltDcResistanceRange_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 4),
    _MltDcResistanceRange_Type()
)
mltDcResistanceRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltDcResistanceRange.setStatus("current")


class _MltLoopLengthMultiplier_Type(Integer32):
    """Custom type mltLoopLengthMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_MltLoopLengthMultiplier_Type.__name__ = "Integer32"
_MltLoopLengthMultiplier_Object = MibScalar
mltLoopLengthMultiplier = _MltLoopLengthMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 5),
    _MltLoopLengthMultiplier_Type()
)
mltLoopLengthMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltLoopLengthMultiplier.setStatus("current")


class _MltLoopDetectThreshold_Type(Integer32):
    """Custom type mltLoopDetectThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_MltLoopDetectThreshold_Type.__name__ = "Integer32"
_MltLoopDetectThreshold_Object = MibScalar
mltLoopDetectThreshold = _MltLoopDetectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 1, 6),
    _MltLoopDetectThreshold_Type()
)
mltLoopDetectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mltLoopDetectThreshold.setStatus("current")
_MltTestStatus_ObjectIdentity = ObjectIdentity
mltTestStatus = _MltTestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 2)
)
_MltLastTestStatus_Type = MltTestStatus
_MltLastTestStatus_Object = MibScalar
mltLastTestStatus = _MltLastTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 2, 1),
    _MltLastTestStatus_Type()
)
mltLastTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLastTestStatus.setStatus("current")
_MltErrorText_Type = OctetString
_MltErrorText_Object = MibScalar
mltErrorText = _MltErrorText_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 2, 2),
    _MltErrorText_Type()
)
mltErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltErrorText.setStatus("current")
_MltTestResults_ObjectIdentity = ObjectIdentity
mltTestResults = _MltTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3)
)
_MltStatusResultsTable_Object = MibTable
mltStatusResultsTable = _MltStatusResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mltStatusResultsTable.setStatus("current")
_MltStatusResultsEntry_Object = MibTableRow
mltStatusResultsEntry = _MltStatusResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1)
)
mltStatusResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltStatusResultsEntry.setStatus("current")
_MltStatusAlarm_Type = OctetString
_MltStatusAlarm_Object = MibTableColumn
mltStatusAlarm = _MltStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 1),
    _MltStatusAlarm_Type()
)
mltStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusAlarm.setStatus("current")
_MltStatusHookState_Type = MltTestHookState
_MltStatusHookState_Object = MibTableColumn
mltStatusHookState = _MltStatusHookState_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 2),
    _MltStatusHookState_Type()
)
mltStatusHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusHookState.setStatus("current")
_MltStatusTransversalCurrent_Type = Integer32
_MltStatusTransversalCurrent_Object = MibTableColumn
mltStatusTransversalCurrent = _MltStatusTransversalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 3),
    _MltStatusTransversalCurrent_Type()
)
mltStatusTransversalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusTransversalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusTransversalCurrent.setUnits("0.1 mA")
_MltStatusLongitudinalCurrent_Type = Integer32
_MltStatusLongitudinalCurrent_Object = MibTableColumn
mltStatusLongitudinalCurrent = _MltStatusLongitudinalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 4),
    _MltStatusLongitudinalCurrent_Type()
)
mltStatusLongitudinalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusLongitudinalCurrent.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusLongitudinalCurrent.setUnits("0.1 mA")
_MltStatusTipVoltage_Type = Integer32
_MltStatusTipVoltage_Object = MibTableColumn
mltStatusTipVoltage = _MltStatusTipVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 5),
    _MltStatusTipVoltage_Type()
)
mltStatusTipVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusTipVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusTipVoltage.setUnits("0.1 V")
_MltStatusRingVoltage_Type = Integer32
_MltStatusRingVoltage_Object = MibTableColumn
mltStatusRingVoltage = _MltStatusRingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 6),
    _MltStatusRingVoltage_Type()
)
mltStatusRingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusRingVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusRingVoltage.setUnits("0.1 V")
_MltStatusTipRingVoltage_Type = Integer32
_MltStatusTipRingVoltage_Object = MibTableColumn
mltStatusTipRingVoltage = _MltStatusTipRingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 7),
    _MltStatusTipRingVoltage_Type()
)
mltStatusTipRingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusTipRingVoltage.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusTipRingVoltage.setUnits("0.1 V")
_MltStatusVdd_Type = Integer32
_MltStatusVdd_Object = MibTableColumn
mltStatusVdd = _MltStatusVdd_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 1, 1, 8),
    _MltStatusVdd_Type()
)
mltStatusVdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltStatusVdd.setStatus("current")
if mibBuilder.loadTexts:
    mltStatusVdd.setUnits("0.1 V")
_MltTestResultsTable_Object = MibTable
mltTestResultsTable = _MltTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    mltTestResultsTable.setStatus("current")
_MltTestResultsEntry_Object = MibTableRow
mltTestResultsEntry = _MltTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1)
)
mltTestResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltTestResultsEntry.setStatus("current")
_MltTestAlarm_Type = OctetString
_MltTestAlarm_Object = MibTableColumn
mltTestAlarm = _MltTestAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 1),
    _MltTestAlarm_Type()
)
mltTestAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestAlarm.setStatus("current")
_MltTestHookState_Type = MltTestHookState
_MltTestHookState_Object = MibTableColumn
mltTestHookState = _MltTestHookState_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 2),
    _MltTestHookState_Type()
)
mltTestHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHookState.setStatus("current")
_MltTestVdd_Type = Integer32
_MltTestVdd_Object = MibTableColumn
mltTestVdd = _MltTestVdd_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 3),
    _MltTestVdd_Type()
)
mltTestVdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestVdd.setStatus("current")
if mibBuilder.loadTexts:
    mltTestVdd.setUnits("0.1 V")
_MltTestActiveModeVoltagesVdctr_Type = Integer32
_MltTestActiveModeVoltagesVdctr_Object = MibTableColumn
mltTestActiveModeVoltagesVdctr = _MltTestActiveModeVoltagesVdctr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 4),
    _MltTestActiveModeVoltagesVdctr_Type()
)
mltTestActiveModeVoltagesVdctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdctr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdctr.setUnits("0.1 Vdc")
_MltTestActiveModeVoltagesVdctg_Type = Integer32
_MltTestActiveModeVoltagesVdctg_Object = MibTableColumn
mltTestActiveModeVoltagesVdctg = _MltTestActiveModeVoltagesVdctg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 5),
    _MltTestActiveModeVoltagesVdctg_Type()
)
mltTestActiveModeVoltagesVdctg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdctg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdctg.setUnits("0.1 Vdc")
_MltTestActiveModeVoltagesVdcrg_Type = Integer32
_MltTestActiveModeVoltagesVdcrg_Object = MibTableColumn
mltTestActiveModeVoltagesVdcrg = _MltTestActiveModeVoltagesVdcrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 6),
    _MltTestActiveModeVoltagesVdcrg_Type()
)
mltTestActiveModeVoltagesVdcrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdcrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVdcrg.setUnits("0.1 Vdc")
_MltTestActiveModeVoltagesVactr_Type = Integer32
_MltTestActiveModeVoltagesVactr_Object = MibTableColumn
mltTestActiveModeVoltagesVactr = _MltTestActiveModeVoltagesVactr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 7),
    _MltTestActiveModeVoltagesVactr_Type()
)
mltTestActiveModeVoltagesVactr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVactr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVactr.setUnits("0.1 Vrms")
_MltTestActiveModeVoltagesVactg_Type = Integer32
_MltTestActiveModeVoltagesVactg_Object = MibTableColumn
mltTestActiveModeVoltagesVactg = _MltTestActiveModeVoltagesVactg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 8),
    _MltTestActiveModeVoltagesVactg_Type()
)
mltTestActiveModeVoltagesVactg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVactg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVactg.setUnits("0.1 Vrms")
_MltTestActiveModeVoltagesVacrg_Type = Integer32
_MltTestActiveModeVoltagesVacrg_Object = MibTableColumn
mltTestActiveModeVoltagesVacrg = _MltTestActiveModeVoltagesVacrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 9),
    _MltTestActiveModeVoltagesVacrg_Type()
)
mltTestActiveModeVoltagesVacrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVacrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestActiveModeVoltagesVacrg.setUnits("0.1 Vrms")
_MltTestHighImpedanceModeVoltagesVdctr_Type = Integer32
_MltTestHighImpedanceModeVoltagesVdctr_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVdctr = _MltTestHighImpedanceModeVoltagesVdctr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 10),
    _MltTestHighImpedanceModeVoltagesVdctr_Type()
)
mltTestHighImpedanceModeVoltagesVdctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdctr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdctr.setUnits("0.1 Vdc")
_MltTestHighImpedanceModeVoltagesVdctg_Type = Integer32
_MltTestHighImpedanceModeVoltagesVdctg_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVdctg = _MltTestHighImpedanceModeVoltagesVdctg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 11),
    _MltTestHighImpedanceModeVoltagesVdctg_Type()
)
mltTestHighImpedanceModeVoltagesVdctg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdctg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdctg.setUnits("0.1 Vdc")
_MltTestHighImpedanceModeVoltagesVdcrg_Type = Integer32
_MltTestHighImpedanceModeVoltagesVdcrg_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVdcrg = _MltTestHighImpedanceModeVoltagesVdcrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 12),
    _MltTestHighImpedanceModeVoltagesVdcrg_Type()
)
mltTestHighImpedanceModeVoltagesVdcrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdcrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVdcrg.setUnits("0.1 Vdc")
_MltTestHighImpedanceModeVoltagesVactr_Type = Integer32
_MltTestHighImpedanceModeVoltagesVactr_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVactr = _MltTestHighImpedanceModeVoltagesVactr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 13),
    _MltTestHighImpedanceModeVoltagesVactr_Type()
)
mltTestHighImpedanceModeVoltagesVactr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVactr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVactr.setUnits("0.1 Vrms")
_MltTestHighImpedanceModeVoltagesVactg_Type = Integer32
_MltTestHighImpedanceModeVoltagesVactg_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVactg = _MltTestHighImpedanceModeVoltagesVactg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 14),
    _MltTestHighImpedanceModeVoltagesVactg_Type()
)
mltTestHighImpedanceModeVoltagesVactg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVactg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVactg.setUnits("0.1 Vrms")
_MltTestHighImpedanceModeVoltagesVacrg_Type = Integer32
_MltTestHighImpedanceModeVoltagesVacrg_Object = MibTableColumn
mltTestHighImpedanceModeVoltagesVacrg = _MltTestHighImpedanceModeVoltagesVacrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 15),
    _MltTestHighImpedanceModeVoltagesVacrg_Type()
)
mltTestHighImpedanceModeVoltagesVacrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVacrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestHighImpedanceModeVoltagesVacrg.setUnits("0.1 Vrms")
_MltTestDcCurrentsItransversal_Type = Integer32
_MltTestDcCurrentsItransversal_Object = MibTableColumn
mltTestDcCurrentsItransversal = _MltTestDcCurrentsItransversal_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 16),
    _MltTestDcCurrentsItransversal_Type()
)
mltTestDcCurrentsItransversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestDcCurrentsItransversal.setStatus("current")
if mibBuilder.loadTexts:
    mltTestDcCurrentsItransversal.setUnits("0.1 mA")
_MltTestDcCurrentsIlongitudinal_Type = Integer32
_MltTestDcCurrentsIlongitudinal_Object = MibTableColumn
mltTestDcCurrentsIlongitudinal = _MltTestDcCurrentsIlongitudinal_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 17),
    _MltTestDcCurrentsIlongitudinal_Type()
)
mltTestDcCurrentsIlongitudinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestDcCurrentsIlongitudinal.setStatus("current")
if mibBuilder.loadTexts:
    mltTestDcCurrentsIlongitudinal.setUnits("0.1 mA")
_MltTestDcCurrentsItip_Type = Integer32
_MltTestDcCurrentsItip_Object = MibTableColumn
mltTestDcCurrentsItip = _MltTestDcCurrentsItip_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 18),
    _MltTestDcCurrentsItip_Type()
)
mltTestDcCurrentsItip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestDcCurrentsItip.setStatus("current")
if mibBuilder.loadTexts:
    mltTestDcCurrentsItip.setUnits("0.1 mA")
_MltTestDcCurrentsIring_Type = Integer32
_MltTestDcCurrentsIring_Object = MibTableColumn
mltTestDcCurrentsIring = _MltTestDcCurrentsIring_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 19),
    _MltTestDcCurrentsIring_Type()
)
mltTestDcCurrentsIring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestDcCurrentsIring.setStatus("current")
if mibBuilder.loadTexts:
    mltTestDcCurrentsIring.setUnits("0.1 mA")
_MltTestCapacitanceCeqtr_Type = Integer32
_MltTestCapacitanceCeqtr_Object = MibTableColumn
mltTestCapacitanceCeqtr = _MltTestCapacitanceCeqtr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 20),
    _MltTestCapacitanceCeqtr_Type()
)
mltTestCapacitanceCeqtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqtr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqtr.setUnits("nF")
_MltTestCapacitanceCeqtg_Type = Integer32
_MltTestCapacitanceCeqtg_Object = MibTableColumn
mltTestCapacitanceCeqtg = _MltTestCapacitanceCeqtg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 21),
    _MltTestCapacitanceCeqtg_Type()
)
mltTestCapacitanceCeqtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqtg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqtg.setUnits("nF")
_MltTestCapacitanceCeqrg_Type = Integer32
_MltTestCapacitanceCeqrg_Object = MibTableColumn
mltTestCapacitanceCeqrg = _MltTestCapacitanceCeqrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 22),
    _MltTestCapacitanceCeqrg_Type()
)
mltTestCapacitanceCeqrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestCapacitanceCeqrg.setUnits("nF")
_MltTestResistanceRtr_Type = Integer32
_MltTestResistanceRtr_Object = MibTableColumn
mltTestResistanceRtr = _MltTestResistanceRtr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 23),
    _MltTestResistanceRtr_Type()
)
mltTestResistanceRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestResistanceRtr.setStatus("current")
if mibBuilder.loadTexts:
    mltTestResistanceRtr.setUnits("Ohm")
_MltTestResistanceRtg_Type = Integer32
_MltTestResistanceRtg_Object = MibTableColumn
mltTestResistanceRtg = _MltTestResistanceRtg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 24),
    _MltTestResistanceRtg_Type()
)
mltTestResistanceRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestResistanceRtg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestResistanceRtg.setUnits("Ohm")
_MltTestResistanceRrg_Type = Integer32
_MltTestResistanceRrg_Object = MibTableColumn
mltTestResistanceRrg = _MltTestResistanceRrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 25),
    _MltTestResistanceRrg_Type()
)
mltTestResistanceRrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestResistanceRrg.setStatus("current")
if mibBuilder.loadTexts:
    mltTestResistanceRrg.setUnits("Ohm")
_MltTestGr909HazardousPotentialTestResult_Type = MltTestPassFail
_MltTestGr909HazardousPotentialTestResult_Object = MibTableColumn
mltTestGr909HazardousPotentialTestResult = _MltTestGr909HazardousPotentialTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 26),
    _MltTestGr909HazardousPotentialTestResult_Type()
)
mltTestGr909HazardousPotentialTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909HazardousPotentialTestResult.setStatus("current")
_MltTestGr909ForeignEmfTestResult_Type = MltTestPassFail
_MltTestGr909ForeignEmfTestResult_Object = MibTableColumn
mltTestGr909ForeignEmfTestResult = _MltTestGr909ForeignEmfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 27),
    _MltTestGr909ForeignEmfTestResult_Type()
)
mltTestGr909ForeignEmfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ForeignEmfTestResult.setStatus("current")
_MltTestGr909FuseTestTipFuse_Type = MltTestPassFail
_MltTestGr909FuseTestTipFuse_Object = MibTableColumn
mltTestGr909FuseTestTipFuse = _MltTestGr909FuseTestTipFuse_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 28),
    _MltTestGr909FuseTestTipFuse_Type()
)
mltTestGr909FuseTestTipFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909FuseTestTipFuse.setStatus("obsolete")
_MltTestGr909FuseTestRingFuse_Type = MltTestPassFail
_MltTestGr909FuseTestRingFuse_Object = MibTableColumn
mltTestGr909FuseTestRingFuse = _MltTestGr909FuseTestRingFuse_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 29),
    _MltTestGr909FuseTestRingFuse_Type()
)
mltTestGr909FuseTestRingFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909FuseTestRingFuse.setStatus("obsolete")
_MltTestGr909ResistiveFaultTestResult_Type = MltTestPassFail
_MltTestGr909ResistiveFaultTestResult_Object = MibTableColumn
mltTestGr909ResistiveFaultTestResult = _MltTestGr909ResistiveFaultTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 30),
    _MltTestGr909ResistiveFaultTestResult_Type()
)
mltTestGr909ResistiveFaultTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ResistiveFaultTestResult.setStatus("current")
_MltTestGr909ReceiverOffhookTestResult_Type = MltTestPassFail
_MltTestGr909ReceiverOffhookTestResult_Object = MibTableColumn
mltTestGr909ReceiverOffhookTestResult = _MltTestGr909ReceiverOffhookTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 31),
    _MltTestGr909ReceiverOffhookTestResult_Type()
)
mltTestGr909ReceiverOffhookTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestResult.setStatus("current")
_MltTestGr909ReceiverOffhookTestResistance1_Type = Integer32
_MltTestGr909ReceiverOffhookTestResistance1_Object = MibTableColumn
mltTestGr909ReceiverOffhookTestResistance1 = _MltTestGr909ReceiverOffhookTestResistance1_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 32),
    _MltTestGr909ReceiverOffhookTestResistance1_Type()
)
mltTestGr909ReceiverOffhookTestResistance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestResistance1.setStatus("current")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestResistance1.setUnits("Ohm")
_MltTestGr909ReceiverOffhookTestResistance2_Type = Integer32
_MltTestGr909ReceiverOffhookTestResistance2_Object = MibTableColumn
mltTestGr909ReceiverOffhookTestResistance2 = _MltTestGr909ReceiverOffhookTestResistance2_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 33),
    _MltTestGr909ReceiverOffhookTestResistance2_Type()
)
mltTestGr909ReceiverOffhookTestResistance2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestResistance2.setStatus("current")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestResistance2.setUnits("Ohm")
_MltTestGr909ReceiverOffhookTestDifference_Type = Integer32
_MltTestGr909ReceiverOffhookTestDifference_Object = MibTableColumn
mltTestGr909ReceiverOffhookTestDifference = _MltTestGr909ReceiverOffhookTestDifference_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 34),
    _MltTestGr909ReceiverOffhookTestDifference_Type()
)
mltTestGr909ReceiverOffhookTestDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestDifference.setStatus("current")
if mibBuilder.loadTexts:
    mltTestGr909ReceiverOffhookTestDifference.setUnits("%")
_MltTestGr909RingerTestResult_Type = MltTestRingerResult
_MltTestGr909RingerTestResult_Object = MibTableColumn
mltTestGr909RingerTestResult = _MltTestGr909RingerTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 35),
    _MltTestGr909RingerTestResult_Type()
)
mltTestGr909RingerTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909RingerTestResult.setStatus("current")
_MltTestGr909RingerTestRen_Type = Integer32
_MltTestGr909RingerTestRen_Object = MibTableColumn
mltTestGr909RingerTestRen = _MltTestGr909RingerTestRen_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 36),
    _MltTestGr909RingerTestRen_Type()
)
mltTestGr909RingerTestRen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestGr909RingerTestRen.setStatus("current")
if mibBuilder.loadTexts:
    mltTestGr909RingerTestRen.setUnits("0.1 REN")
_MltTestErrors_Type = OctetString
_MltTestErrors_Object = MibTableColumn
mltTestErrors = _MltTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 37),
    _MltTestErrors_Type()
)
mltTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestErrors.setStatus("current")
_MltTestFuseTestTipFuse_Type = MltTestPassFail
_MltTestFuseTestTipFuse_Object = MibTableColumn
mltTestFuseTestTipFuse = _MltTestFuseTestTipFuse_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 38),
    _MltTestFuseTestTipFuse_Type()
)
mltTestFuseTestTipFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestFuseTestTipFuse.setStatus("current")
_MltTestFuseTestRingFuse_Type = MltTestPassFail
_MltTestFuseTestRingFuse_Object = MibTableColumn
mltTestFuseTestRingFuse = _MltTestFuseTestRingFuse_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 2, 1, 39),
    _MltTestFuseTestRingFuse_Type()
)
mltTestFuseTestRingFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltTestFuseTestRingFuse.setStatus("current")
_MltActiveModeVoltagesResultsTable_Object = MibTable
mltActiveModeVoltagesResultsTable = _MltActiveModeVoltagesResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    mltActiveModeVoltagesResultsTable.setStatus("current")
_MltActiveModeVoltagesResultsEntry_Object = MibTableRow
mltActiveModeVoltagesResultsEntry = _MltActiveModeVoltagesResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1)
)
mltActiveModeVoltagesResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltActiveModeVoltagesResultsEntry.setStatus("current")
_MltActiveModeVoltagesVdctr_Type = Integer32
_MltActiveModeVoltagesVdctr_Object = MibTableColumn
mltActiveModeVoltagesVdctr = _MltActiveModeVoltagesVdctr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 1),
    _MltActiveModeVoltagesVdctr_Type()
)
mltActiveModeVoltagesVdctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdctr.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdctr.setUnits("0.1 Vdc")
_MltActiveModeVoltagesVdctg_Type = Integer32
_MltActiveModeVoltagesVdctg_Object = MibTableColumn
mltActiveModeVoltagesVdctg = _MltActiveModeVoltagesVdctg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 2),
    _MltActiveModeVoltagesVdctg_Type()
)
mltActiveModeVoltagesVdctg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdctg.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdctg.setUnits("0.1 Vdc")
_MltActiveModeVoltagesVdcrg_Type = Integer32
_MltActiveModeVoltagesVdcrg_Object = MibTableColumn
mltActiveModeVoltagesVdcrg = _MltActiveModeVoltagesVdcrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 3),
    _MltActiveModeVoltagesVdcrg_Type()
)
mltActiveModeVoltagesVdcrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdcrg.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVdcrg.setUnits("0.1 Vdc")
_MltActiveModeVoltagesVactr_Type = Integer32
_MltActiveModeVoltagesVactr_Object = MibTableColumn
mltActiveModeVoltagesVactr = _MltActiveModeVoltagesVactr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 4),
    _MltActiveModeVoltagesVactr_Type()
)
mltActiveModeVoltagesVactr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVactr.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVactr.setUnits("0.1 Vrms")
_MltActiveModeVoltagesVactg_Type = Integer32
_MltActiveModeVoltagesVactg_Object = MibTableColumn
mltActiveModeVoltagesVactg = _MltActiveModeVoltagesVactg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 5),
    _MltActiveModeVoltagesVactg_Type()
)
mltActiveModeVoltagesVactg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVactg.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVactg.setUnits("0.1 Vrms")
_MltActiveModeVoltagesVacrg_Type = Integer32
_MltActiveModeVoltagesVacrg_Object = MibTableColumn
mltActiveModeVoltagesVacrg = _MltActiveModeVoltagesVacrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 6),
    _MltActiveModeVoltagesVacrg_Type()
)
mltActiveModeVoltagesVacrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVacrg.setStatus("current")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesVacrg.setUnits("0.1 Vrms")
_MltActiveModeVoltagesErrors_Type = OctetString
_MltActiveModeVoltagesErrors_Object = MibTableColumn
mltActiveModeVoltagesErrors = _MltActiveModeVoltagesErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 3, 1, 7),
    _MltActiveModeVoltagesErrors_Type()
)
mltActiveModeVoltagesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltActiveModeVoltagesErrors.setStatus("current")
_MltHighImpedanceModeVoltagesResultsTable_Object = MibTable
mltHighImpedanceModeVoltagesResultsTable = _MltHighImpedanceModeVoltagesResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesResultsTable.setStatus("current")
_MltHighImpedanceModeVoltagesResultsEntry_Object = MibTableRow
mltHighImpedanceModeVoltagesResultsEntry = _MltHighImpedanceModeVoltagesResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1)
)
mltHighImpedanceModeVoltagesResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesResultsEntry.setStatus("current")
_MltHighImpedanceModeVoltagesVdctr_Type = Integer32
_MltHighImpedanceModeVoltagesVdctr_Object = MibTableColumn
mltHighImpedanceModeVoltagesVdctr = _MltHighImpedanceModeVoltagesVdctr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 1),
    _MltHighImpedanceModeVoltagesVdctr_Type()
)
mltHighImpedanceModeVoltagesVdctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdctr.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdctr.setUnits("0.1 Vdc")
_MltHighImpedanceModeVoltagesVdctg_Type = Integer32
_MltHighImpedanceModeVoltagesVdctg_Object = MibTableColumn
mltHighImpedanceModeVoltagesVdctg = _MltHighImpedanceModeVoltagesVdctg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 2),
    _MltHighImpedanceModeVoltagesVdctg_Type()
)
mltHighImpedanceModeVoltagesVdctg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdctg.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdctg.setUnits("0.1 Vdc")
_MltHighImpedanceModeVoltagesVdcrg_Type = Integer32
_MltHighImpedanceModeVoltagesVdcrg_Object = MibTableColumn
mltHighImpedanceModeVoltagesVdcrg = _MltHighImpedanceModeVoltagesVdcrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 3),
    _MltHighImpedanceModeVoltagesVdcrg_Type()
)
mltHighImpedanceModeVoltagesVdcrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdcrg.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVdcrg.setUnits("0.1 Vdc")
_MltHighImpedanceModeVoltagesVactr_Type = Integer32
_MltHighImpedanceModeVoltagesVactr_Object = MibTableColumn
mltHighImpedanceModeVoltagesVactr = _MltHighImpedanceModeVoltagesVactr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 4),
    _MltHighImpedanceModeVoltagesVactr_Type()
)
mltHighImpedanceModeVoltagesVactr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVactr.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVactr.setUnits("0.1 Vrms")
_MltHighImpedanceModeVoltagesVactg_Type = Integer32
_MltHighImpedanceModeVoltagesVactg_Object = MibTableColumn
mltHighImpedanceModeVoltagesVactg = _MltHighImpedanceModeVoltagesVactg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 5),
    _MltHighImpedanceModeVoltagesVactg_Type()
)
mltHighImpedanceModeVoltagesVactg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVactg.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVactg.setUnits("0.1 Vrms")
_MltHighImpedanceModeVoltagesVacrg_Type = Integer32
_MltHighImpedanceModeVoltagesVacrg_Object = MibTableColumn
mltHighImpedanceModeVoltagesVacrg = _MltHighImpedanceModeVoltagesVacrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 6),
    _MltHighImpedanceModeVoltagesVacrg_Type()
)
mltHighImpedanceModeVoltagesVacrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVacrg.setStatus("current")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesVacrg.setUnits("0.1 Vrms")
_MltHighImpedanceModeVoltagesErrors_Type = OctetString
_MltHighImpedanceModeVoltagesErrors_Object = MibTableColumn
mltHighImpedanceModeVoltagesErrors = _MltHighImpedanceModeVoltagesErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 4, 1, 7),
    _MltHighImpedanceModeVoltagesErrors_Type()
)
mltHighImpedanceModeVoltagesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltHighImpedanceModeVoltagesErrors.setStatus("current")
_MltDcResistanceResultsTable_Object = MibTable
mltDcResistanceResultsTable = _MltDcResistanceResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    mltDcResistanceResultsTable.setStatus("current")
_MltDcResistanceResultsEntry_Object = MibTableRow
mltDcResistanceResultsEntry = _MltDcResistanceResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5, 1)
)
mltDcResistanceResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltDcResistanceResultsEntry.setStatus("current")
_MltDcResistanceRtr_Type = Integer32
_MltDcResistanceRtr_Object = MibTableColumn
mltDcResistanceRtr = _MltDcResistanceRtr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5, 1, 1),
    _MltDcResistanceRtr_Type()
)
mltDcResistanceRtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDcResistanceRtr.setStatus("current")
if mibBuilder.loadTexts:
    mltDcResistanceRtr.setUnits("Ohm")
_MltDcResistanceRtg_Type = Integer32
_MltDcResistanceRtg_Object = MibTableColumn
mltDcResistanceRtg = _MltDcResistanceRtg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5, 1, 2),
    _MltDcResistanceRtg_Type()
)
mltDcResistanceRtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDcResistanceRtg.setStatus("current")
if mibBuilder.loadTexts:
    mltDcResistanceRtg.setUnits("Ohm")
_MltDcResistanceRrg_Type = Integer32
_MltDcResistanceRrg_Object = MibTableColumn
mltDcResistanceRrg = _MltDcResistanceRrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5, 1, 3),
    _MltDcResistanceRrg_Type()
)
mltDcResistanceRrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDcResistanceRrg.setStatus("current")
if mibBuilder.loadTexts:
    mltDcResistanceRrg.setUnits("Ohm")
_MltDcResistanceErrors_Type = OctetString
_MltDcResistanceErrors_Object = MibTableColumn
mltDcResistanceErrors = _MltDcResistanceErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 5, 1, 4),
    _MltDcResistanceErrors_Type()
)
mltDcResistanceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltDcResistanceErrors.setStatus("current")
_MltCapacitanceResultsTable_Object = MibTable
mltCapacitanceResultsTable = _MltCapacitanceResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6)
)
if mibBuilder.loadTexts:
    mltCapacitanceResultsTable.setStatus("current")
_MltCapacitanceResultsEntry_Object = MibTableRow
mltCapacitanceResultsEntry = _MltCapacitanceResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6, 1)
)
mltCapacitanceResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltCapacitanceResultsEntry.setStatus("current")
_MltCapacitanceCeqtr_Type = Integer32
_MltCapacitanceCeqtr_Object = MibTableColumn
mltCapacitanceCeqtr = _MltCapacitanceCeqtr_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6, 1, 1),
    _MltCapacitanceCeqtr_Type()
)
mltCapacitanceCeqtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCapacitanceCeqtr.setStatus("current")
if mibBuilder.loadTexts:
    mltCapacitanceCeqtr.setUnits("nF")
_MltCapacitanceCeqtg_Type = Integer32
_MltCapacitanceCeqtg_Object = MibTableColumn
mltCapacitanceCeqtg = _MltCapacitanceCeqtg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6, 1, 2),
    _MltCapacitanceCeqtg_Type()
)
mltCapacitanceCeqtg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCapacitanceCeqtg.setStatus("current")
if mibBuilder.loadTexts:
    mltCapacitanceCeqtg.setUnits("nF")
_MltCapacitanceCeqrg_Type = Integer32
_MltCapacitanceCeqrg_Object = MibTableColumn
mltCapacitanceCeqrg = _MltCapacitanceCeqrg_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6, 1, 3),
    _MltCapacitanceCeqrg_Type()
)
mltCapacitanceCeqrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCapacitanceCeqrg.setStatus("current")
if mibBuilder.loadTexts:
    mltCapacitanceCeqrg.setUnits("nF")
_MltCapacitanceErrors_Type = OctetString
_MltCapacitanceErrors_Object = MibTableColumn
mltCapacitanceErrors = _MltCapacitanceErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 6, 1, 4),
    _MltCapacitanceErrors_Type()
)
mltCapacitanceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltCapacitanceErrors.setStatus("current")
_MltLoopDetectResultsTable_Object = MibTable
mltLoopDetectResultsTable = _MltLoopDetectResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7)
)
if mibBuilder.loadTexts:
    mltLoopDetectResultsTable.setStatus("current")
_MltLoopDetectResultsEntry_Object = MibTableRow
mltLoopDetectResultsEntry = _MltLoopDetectResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7, 1)
)
mltLoopDetectResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltLoopDetectResultsEntry.setStatus("current")
_MltLoopDetectLoopCapacitance_Type = Integer32
_MltLoopDetectLoopCapacitance_Object = MibTableColumn
mltLoopDetectLoopCapacitance = _MltLoopDetectLoopCapacitance_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7, 1, 1),
    _MltLoopDetectLoopCapacitance_Type()
)
mltLoopDetectLoopCapacitance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopDetectLoopCapacitance.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopDetectLoopCapacitance.setUnits("nF")
_MltLoopDetectDetectionThreshold_Type = Integer32
_MltLoopDetectDetectionThreshold_Object = MibTableColumn
mltLoopDetectDetectionThreshold = _MltLoopDetectDetectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7, 1, 2),
    _MltLoopDetectDetectionThreshold_Type()
)
mltLoopDetectDetectionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopDetectDetectionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopDetectDetectionThreshold.setUnits("nF")
_MltLoopDetectLoopDetected_Type = MltTestYesNo
_MltLoopDetectLoopDetected_Object = MibTableColumn
mltLoopDetectLoopDetected = _MltLoopDetectLoopDetected_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7, 1, 3),
    _MltLoopDetectLoopDetected_Type()
)
mltLoopDetectLoopDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopDetectLoopDetected.setStatus("current")
_MltLoopDetectErrors_Type = OctetString
_MltLoopDetectErrors_Object = MibTableColumn
mltLoopDetectErrors = _MltLoopDetectErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 7, 1, 4),
    _MltLoopDetectErrors_Type()
)
mltLoopDetectErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopDetectErrors.setStatus("current")
_MltLoopLengthResultsTable_Object = MibTable
mltLoopLengthResultsTable = _MltLoopLengthResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8)
)
if mibBuilder.loadTexts:
    mltLoopLengthResultsTable.setStatus("current")
_MltLoopLengthResultsEntry_Object = MibTableRow
mltLoopLengthResultsEntry = _MltLoopLengthResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1)
)
mltLoopLengthResultsEntry.setIndexNames(
    (0, "OCCAM-MLT-MIB", "mltTestPort"),
)
if mibBuilder.loadTexts:
    mltLoopLengthResultsEntry.setStatus("current")
_MltLoopLengthCapacitanceFactor_Type = Integer32
_MltLoopLengthCapacitanceFactor_Object = MibTableColumn
mltLoopLengthCapacitanceFactor = _MltLoopLengthCapacitanceFactor_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 1),
    _MltLoopLengthCapacitanceFactor_Type()
)
mltLoopLengthCapacitanceFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthCapacitanceFactor.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopLengthCapacitanceFactor.setUnits("nF/mile")
_MltLoopLengthLoopCapacitance_Type = Integer32
_MltLoopLengthLoopCapacitance_Object = MibTableColumn
mltLoopLengthLoopCapacitance = _MltLoopLengthLoopCapacitance_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 2),
    _MltLoopLengthLoopCapacitance_Type()
)
mltLoopLengthLoopCapacitance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthLoopCapacitance.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopLengthLoopCapacitance.setUnits("nF")
_MltLoopLengthLoopLength_Type = Integer32
_MltLoopLengthLoopLength_Object = MibTableColumn
mltLoopLengthLoopLength = _MltLoopLengthLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 3),
    _MltLoopLengthLoopLength_Type()
)
mltLoopLengthLoopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthLoopLength.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopLengthLoopLength.setUnits("ft")
_MltLoopLengthUncompensatedLoopCapacitance_Type = Integer32
_MltLoopLengthUncompensatedLoopCapacitance_Object = MibTableColumn
mltLoopLengthUncompensatedLoopCapacitance = _MltLoopLengthUncompensatedLoopCapacitance_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 4),
    _MltLoopLengthUncompensatedLoopCapacitance_Type()
)
mltLoopLengthUncompensatedLoopCapacitance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthUncompensatedLoopCapacitance.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopLengthUncompensatedLoopCapacitance.setUnits("nF")
_MltLoopLengthUncompensatedLoopLength_Type = Integer32
_MltLoopLengthUncompensatedLoopLength_Object = MibTableColumn
mltLoopLengthUncompensatedLoopLength = _MltLoopLengthUncompensatedLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 5),
    _MltLoopLengthUncompensatedLoopLength_Type()
)
mltLoopLengthUncompensatedLoopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthUncompensatedLoopLength.setStatus("current")
if mibBuilder.loadTexts:
    mltLoopLengthUncompensatedLoopLength.setUnits("ft")
_MltLoopLengthErrors_Type = OctetString
_MltLoopLengthErrors_Object = MibTableColumn
mltLoopLengthErrors = _MltLoopLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 3, 8, 1, 6),
    _MltLoopLengthErrors_Type()
)
mltLoopLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mltLoopLengthErrors.setStatus("current")
_MltTestNotifications_ObjectIdentity = ObjectIdentity
mltTestNotifications = _MltTestNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 4)
)

# Managed Objects groups


# Notification objects

mltTestCompletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6066, 2, 1, 1, 3, 4, 1)
)
mltTestCompletedNotification.setObjects(
      *(("OCCAM-MLT-MIB", "mltTestIdentifier"),
        ("OCCAM-MLT-MIB", "mltTestPort"),
        ("OCCAM-MLT-MIB", "mltLastTestStatus"),
        ("OCCAM-MLT-MIB", "mltErrorText"))
)
if mibBuilder.loadTexts:
    mltTestCompletedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCCAM-MLT-MIB",
    **{"MltTestType": MltTestType,
       "MltTestStatus": MltTestStatus,
       "MltTestIdentifier": MltTestIdentifier,
       "MltTestHookState": MltTestHookState,
       "MltTestPassFail": MltTestPassFail,
       "MltTestRingerResult": MltTestRingerResult,
       "MltTestYesNo": MltTestYesNo,
       "occamMltMib": occamMltMib,
       "mltTestConfig": mltTestConfig,
       "mltTestIdentifier": mltTestIdentifier,
       "mltTestType": mltTestType,
       "mltTestPort": mltTestPort,
       "mltDcResistanceRange": mltDcResistanceRange,
       "mltLoopLengthMultiplier": mltLoopLengthMultiplier,
       "mltLoopDetectThreshold": mltLoopDetectThreshold,
       "mltTestStatus": mltTestStatus,
       "mltLastTestStatus": mltLastTestStatus,
       "mltErrorText": mltErrorText,
       "mltTestResults": mltTestResults,
       "mltStatusResultsTable": mltStatusResultsTable,
       "mltStatusResultsEntry": mltStatusResultsEntry,
       "mltStatusAlarm": mltStatusAlarm,
       "mltStatusHookState": mltStatusHookState,
       "mltStatusTransversalCurrent": mltStatusTransversalCurrent,
       "mltStatusLongitudinalCurrent": mltStatusLongitudinalCurrent,
       "mltStatusTipVoltage": mltStatusTipVoltage,
       "mltStatusRingVoltage": mltStatusRingVoltage,
       "mltStatusTipRingVoltage": mltStatusTipRingVoltage,
       "mltStatusVdd": mltStatusVdd,
       "mltTestResultsTable": mltTestResultsTable,
       "mltTestResultsEntry": mltTestResultsEntry,
       "mltTestAlarm": mltTestAlarm,
       "mltTestHookState": mltTestHookState,
       "mltTestVdd": mltTestVdd,
       "mltTestActiveModeVoltagesVdctr": mltTestActiveModeVoltagesVdctr,
       "mltTestActiveModeVoltagesVdctg": mltTestActiveModeVoltagesVdctg,
       "mltTestActiveModeVoltagesVdcrg": mltTestActiveModeVoltagesVdcrg,
       "mltTestActiveModeVoltagesVactr": mltTestActiveModeVoltagesVactr,
       "mltTestActiveModeVoltagesVactg": mltTestActiveModeVoltagesVactg,
       "mltTestActiveModeVoltagesVacrg": mltTestActiveModeVoltagesVacrg,
       "mltTestHighImpedanceModeVoltagesVdctr": mltTestHighImpedanceModeVoltagesVdctr,
       "mltTestHighImpedanceModeVoltagesVdctg": mltTestHighImpedanceModeVoltagesVdctg,
       "mltTestHighImpedanceModeVoltagesVdcrg": mltTestHighImpedanceModeVoltagesVdcrg,
       "mltTestHighImpedanceModeVoltagesVactr": mltTestHighImpedanceModeVoltagesVactr,
       "mltTestHighImpedanceModeVoltagesVactg": mltTestHighImpedanceModeVoltagesVactg,
       "mltTestHighImpedanceModeVoltagesVacrg": mltTestHighImpedanceModeVoltagesVacrg,
       "mltTestDcCurrentsItransversal": mltTestDcCurrentsItransversal,
       "mltTestDcCurrentsIlongitudinal": mltTestDcCurrentsIlongitudinal,
       "mltTestDcCurrentsItip": mltTestDcCurrentsItip,
       "mltTestDcCurrentsIring": mltTestDcCurrentsIring,
       "mltTestCapacitanceCeqtr": mltTestCapacitanceCeqtr,
       "mltTestCapacitanceCeqtg": mltTestCapacitanceCeqtg,
       "mltTestCapacitanceCeqrg": mltTestCapacitanceCeqrg,
       "mltTestResistanceRtr": mltTestResistanceRtr,
       "mltTestResistanceRtg": mltTestResistanceRtg,
       "mltTestResistanceRrg": mltTestResistanceRrg,
       "mltTestGr909HazardousPotentialTestResult": mltTestGr909HazardousPotentialTestResult,
       "mltTestGr909ForeignEmfTestResult": mltTestGr909ForeignEmfTestResult,
       "mltTestGr909FuseTestTipFuse": mltTestGr909FuseTestTipFuse,
       "mltTestGr909FuseTestRingFuse": mltTestGr909FuseTestRingFuse,
       "mltTestGr909ResistiveFaultTestResult": mltTestGr909ResistiveFaultTestResult,
       "mltTestGr909ReceiverOffhookTestResult": mltTestGr909ReceiverOffhookTestResult,
       "mltTestGr909ReceiverOffhookTestResistance1": mltTestGr909ReceiverOffhookTestResistance1,
       "mltTestGr909ReceiverOffhookTestResistance2": mltTestGr909ReceiverOffhookTestResistance2,
       "mltTestGr909ReceiverOffhookTestDifference": mltTestGr909ReceiverOffhookTestDifference,
       "mltTestGr909RingerTestResult": mltTestGr909RingerTestResult,
       "mltTestGr909RingerTestRen": mltTestGr909RingerTestRen,
       "mltTestErrors": mltTestErrors,
       "mltTestFuseTestTipFuse": mltTestFuseTestTipFuse,
       "mltTestFuseTestRingFuse": mltTestFuseTestRingFuse,
       "mltActiveModeVoltagesResultsTable": mltActiveModeVoltagesResultsTable,
       "mltActiveModeVoltagesResultsEntry": mltActiveModeVoltagesResultsEntry,
       "mltActiveModeVoltagesVdctr": mltActiveModeVoltagesVdctr,
       "mltActiveModeVoltagesVdctg": mltActiveModeVoltagesVdctg,
       "mltActiveModeVoltagesVdcrg": mltActiveModeVoltagesVdcrg,
       "mltActiveModeVoltagesVactr": mltActiveModeVoltagesVactr,
       "mltActiveModeVoltagesVactg": mltActiveModeVoltagesVactg,
       "mltActiveModeVoltagesVacrg": mltActiveModeVoltagesVacrg,
       "mltActiveModeVoltagesErrors": mltActiveModeVoltagesErrors,
       "mltHighImpedanceModeVoltagesResultsTable": mltHighImpedanceModeVoltagesResultsTable,
       "mltHighImpedanceModeVoltagesResultsEntry": mltHighImpedanceModeVoltagesResultsEntry,
       "mltHighImpedanceModeVoltagesVdctr": mltHighImpedanceModeVoltagesVdctr,
       "mltHighImpedanceModeVoltagesVdctg": mltHighImpedanceModeVoltagesVdctg,
       "mltHighImpedanceModeVoltagesVdcrg": mltHighImpedanceModeVoltagesVdcrg,
       "mltHighImpedanceModeVoltagesVactr": mltHighImpedanceModeVoltagesVactr,
       "mltHighImpedanceModeVoltagesVactg": mltHighImpedanceModeVoltagesVactg,
       "mltHighImpedanceModeVoltagesVacrg": mltHighImpedanceModeVoltagesVacrg,
       "mltHighImpedanceModeVoltagesErrors": mltHighImpedanceModeVoltagesErrors,
       "mltDcResistanceResultsTable": mltDcResistanceResultsTable,
       "mltDcResistanceResultsEntry": mltDcResistanceResultsEntry,
       "mltDcResistanceRtr": mltDcResistanceRtr,
       "mltDcResistanceRtg": mltDcResistanceRtg,
       "mltDcResistanceRrg": mltDcResistanceRrg,
       "mltDcResistanceErrors": mltDcResistanceErrors,
       "mltCapacitanceResultsTable": mltCapacitanceResultsTable,
       "mltCapacitanceResultsEntry": mltCapacitanceResultsEntry,
       "mltCapacitanceCeqtr": mltCapacitanceCeqtr,
       "mltCapacitanceCeqtg": mltCapacitanceCeqtg,
       "mltCapacitanceCeqrg": mltCapacitanceCeqrg,
       "mltCapacitanceErrors": mltCapacitanceErrors,
       "mltLoopDetectResultsTable": mltLoopDetectResultsTable,
       "mltLoopDetectResultsEntry": mltLoopDetectResultsEntry,
       "mltLoopDetectLoopCapacitance": mltLoopDetectLoopCapacitance,
       "mltLoopDetectDetectionThreshold": mltLoopDetectDetectionThreshold,
       "mltLoopDetectLoopDetected": mltLoopDetectLoopDetected,
       "mltLoopDetectErrors": mltLoopDetectErrors,
       "mltLoopLengthResultsTable": mltLoopLengthResultsTable,
       "mltLoopLengthResultsEntry": mltLoopLengthResultsEntry,
       "mltLoopLengthCapacitanceFactor": mltLoopLengthCapacitanceFactor,
       "mltLoopLengthLoopCapacitance": mltLoopLengthLoopCapacitance,
       "mltLoopLengthLoopLength": mltLoopLengthLoopLength,
       "mltLoopLengthUncompensatedLoopCapacitance": mltLoopLengthUncompensatedLoopCapacitance,
       "mltLoopLengthUncompensatedLoopLength": mltLoopLengthUncompensatedLoopLength,
       "mltLoopLengthErrors": mltLoopLengthErrors,
       "mltTestNotifications": mltTestNotifications,
       "mltTestCompletedNotification": mltTestCompletedNotification}
)
