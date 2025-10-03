# SNMP MIB module (ADVA-FSP3000ALM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\ADVA-FSP3000ALM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:39 2025
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

(IdentityTranslation,
 TrapAlarmSeverity,
 TrapCounter) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "IdentityTranslation",
    "TrapAlarmSeverity",
    "TrapCounter")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsp3000alm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14)
)
if mibBuilder.loadTexts:
    fsp3000alm.setRevisions(
        ("2023-11-10 00:00",
         "2023-04-19 00:00",
         "2022-12-10 00:00",
         "2022-03-04 00:00",
         "2021-12-02 00:00",
         "2021-07-20 00:00",
         "2021-02-10 00:00",
         "2020-12-14 00:00",
         "2020-11-10 00:00",
         "2020-06-01 00:00",
         "2019-12-01 00:00",
         "2019-07-03 00:00",
         "2018-11-26 00:00",
         "2018-07-09 00:00",
         "2018-05-24 00:00",
         "2017-11-07 00:00",
         "2017-03-21 00:00",
         "2017-03-08 00:00",
         "2016-10-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Fsp3000almAlarmListType(TextualConvention, Integer32):
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
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("alarmTempCPU", 1),
          ("alarmTempBoard1", 2),
          ("alarmTempBoard2Low", 3),
          ("alarmTempBoard2High", 4),
          ("alarmTempLaserLow", 5),
          ("alarmTempLaserHigh", 6),
          ("alarmMonNotRunning", 7),
          ("alarmFpRunning", 8),
          ("alarmFaRunning", 9),
          ("alarmFpMissing", 10),
          ("alarmThresCrossedFast", 11),
          ("alarmThresCrossedMedium", 12),
          ("alarmThresCrossedSlow", 13),
          ("alarmLinkBudgetExceeded", 14),
          ("alarmLinkBudgetNearlyExceeded", 15),
          ("alarmManagementState", 16),
          ("alarmDisabledState", 17),
          ("stateChangedTrap", 18),
          ("objectChangedTrap", 19),
          ("trapsinkCreatedTrap", 20),
          ("trapsinkDeletedTrap", 21),
          ("transient15MinMeasCollected", 22),
          ("transient1DayMeasCollected", 23),
          ("transientFpStarted", 24),
          ("transientFpCompleted", 25),
          ("transientFpFailed", 26),
          ("transientSwMgmtActionStarted", 27),
          ("transientSwMgmtActionCompleted", 28),
          ("transientSwMgmtActionFailed", 29),
          ("transientDbMgmtActionStarted", 30),
          ("transientDbMgmtActionCompleted", 31),
          ("transientDbMgmtActionFailed", 32),
          ("alarmNtpServerUnreachable", 33),
          ("transientFpSaved", 34),
          ("transientMonStarted", 35),
          ("transientMonStopped", 36),
          ("transientOtdrMeasurementStarted", 37),
          ("transientOtdrMeasurementCompleted", 38),
          ("transientOtdrMeasurementFailed", 39),
          ("transientOtdrMeasurementSaved", 40),
          ("transientFaStarted", 41),
          ("transientFaCompleted", 42),
          ("transientFaFailed", 43),
          ("transientFaSaved", 44),
          ("transientInternalError", 45),
          ("alarmRebootRunning", 46),
          ("alarmWarmupRunning", 47),
          ("alarmBadSysStat", 48),
          ("alarmWrongFWVersion", 49),
          ("alarmMonProcNotRunning", 50),
          ("transientFaDeleted", 51),
          ("transientOtdrMeasurementDeleted", 52),
          ("transientOtdrTraceMgmtActionStarted", 53),
          ("transientOtdrTraceMgmtActionCompleted", 54),
          ("transientOtdrTraceMgmtActionFailed", 55),
          ("alarmAlmPackageMismatch", 56),
          ("alarmEmailNotifyThresCrossedFast", 57),
          ("alarmEmailNotifyThresCrossedMedium", 58),
          ("alarmEmailNotifyThresCrossedSlow", 59),
          ("alarmEmailNotifyLinkBudgetExceeded", 60),
          ("alarmEmailNotifyLinkBudgetNearlyExceeded", 61),
          ("authenticationNotification", 62),
          ("authenticationNotificationSummary", 63),
          ("monitorPointCreated", 64),
          ("monitorPointDeleted", 65),
          ("alarmLossDeviationHigh", 66),
          ("alarmLossHigh", 67),
          ("alarmRootLinkFault", 68),
          ("transientResetMeansStarted", 69),
          ("transientResetMeansCompleted", 70),
          ("transientResetMeansFailed", 71),
          ("alarmTrafficOutage", 72),
          ("userAdded", 73),
          ("userDeleted", 74),
          ("customizedFpEventCreated", 75),
          ("customizedFpEventDeleted", 76),
          ("transientExportMgmtActionStarted", 77),
          ("transientExportMgmtActionCompleted", 78),
          ("transientExportMgmtActionFailed", 79),
          ("alarmSensor1High", 80),
          ("alarmSensor2High", 81),
          ("alarmEmailNotifyRootLinkFault", 82),
          ("transientTimeChange", 83),
          ("alarmTopologyChanged", 84),
          ("alarmEmailNotifyLossDeviationHigh", 85),
          ("alarmEmailNotifyLossHigh", 86),
          ("alarmEmailNotifySensor1High", 87),
          ("alarmEmailNotifySensor2High", 88),
          ("alarmEmulationMode", 89),
          ("transientFiberIdentifierStarted", 90),
          ("transientFiberIdentifierCompleted", 91),
          ("transientFiberIdentifierFailed", 92),
          ("transientPkiCertRequestStarted", 93),
          ("transientPkiCertRequestCompleted", 94),
          ("transientPkiCertRequestFailed", 95),
          ("alarmCertExceeded", 96),
          ("alarmCertNearlyExceeded", 97),
          ("transientLinkChanged", 98),
          ("alarmAddDropLinkLossHigh", 99),
          ("alarmAddDropLinkLossDev", 100),
          ("alarmEmailNotifyAddDropLinkLossHigh", 101),
          ("alarmEmailNotifyAddDropLinkLossDev", 102),
          ("segmentCreated", 103),
          ("segmentDeleted", 104),
          ("alarmEquipmentRemoved", 105),
          ("alarmEquipmentFault", 106),
          ("alarmAttenuationHigh", 107),
          ("internalExtensionChannelCreated", 108),
          ("internalExtensionChannelDeleted", 109),
          ("portExtenderCreated", 110),
          ("portExtenderDeleted", 111))
    )



# MIB Managed Objects in the order of their OIDs

_AdvaMIB_ObjectIdentity = ObjectIdentity
advaMIB = _AdvaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1)
)
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmSource"),
    (0, "ADVA-FSP3000ALM-MIB", "alarmType"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmSource_Type(Integer32):
    """Custom type alarmSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899000),
    )


_AlarmSource_Type.__name__ = "Integer32"
_AlarmSource_Object = MibTableColumn
alarmSource = _AlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 1),
    _AlarmSource_Type()
)
alarmSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSource.setStatus("current")
_AlarmType_Type = Fsp3000almAlarmListType
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 2),
    _AlarmType_Type()
)
alarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmSeverity_Type = TrapAlarmSeverity
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 3),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmTimeStamp_Type = DateAndTime
_AlarmTimeStamp_Object = MibTableColumn
alarmTimeStamp = _AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 1, 1, 4),
    _AlarmTimeStamp_Type()
)
alarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTimeStamp.setStatus("current")
_AlarmSeverityTable_Object = MibTable
alarmSeverityTable = _AlarmSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    alarmSeverityTable.setStatus("current")
_AlarmSeverityEntry_Object = MibTableRow
alarmSeverityEntry = _AlarmSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1)
)
alarmSeverityEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmSource"),
    (0, "ADVA-FSP3000ALM-MIB", "alarmSeverityType"),
)
if mibBuilder.loadTexts:
    alarmSeverityEntry.setStatus("current")
_AlarmSeverityType_Type = Fsp3000almAlarmListType
_AlarmSeverityType_Object = MibTableColumn
alarmSeverityType = _AlarmSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1, 2),
    _AlarmSeverityType_Type()
)
alarmSeverityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmSeverityType.setStatus("current")
_AlarmSeverityValue_Type = TrapAlarmSeverity
_AlarmSeverityValue_Object = MibTableColumn
alarmSeverityValue = _AlarmSeverityValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 2, 1, 3),
    _AlarmSeverityValue_Type()
)
alarmSeverityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSeverityValue.setStatus("current")
_AlarmEmailNotifyTable_Object = MibTable
alarmEmailNotifyTable = _AlarmEmailNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    alarmEmailNotifyTable.setStatus("current")
_AlarmEmailNotifyEntry_Object = MibTableRow
alarmEmailNotifyEntry = _AlarmEmailNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1)
)
alarmEmailNotifyEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmSource"),
    (0, "ADVA-FSP3000ALM-MIB", "alarmEmailNotifyType"),
)
if mibBuilder.loadTexts:
    alarmEmailNotifyEntry.setStatus("current")
_AlarmEmailNotifyType_Type = Fsp3000almAlarmListType
_AlarmEmailNotifyType_Object = MibTableColumn
alarmEmailNotifyType = _AlarmEmailNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 1),
    _AlarmEmailNotifyType_Type()
)
alarmEmailNotifyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmEmailNotifyType.setStatus("current")


class _AlarmEmailNotifyExternalId_Type(DisplayString):
    """Custom type alarmEmailNotifyExternalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmEmailNotifyExternalId_Type.__name__ = "DisplayString"
_AlarmEmailNotifyExternalId_Object = MibTableColumn
alarmEmailNotifyExternalId = _AlarmEmailNotifyExternalId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 2),
    _AlarmEmailNotifyExternalId_Type()
)
alarmEmailNotifyExternalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyExternalId.setStatus("current")


class _AlarmEmailNotifyId_Type(DisplayString):
    """Custom type alarmEmailNotifyId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlarmEmailNotifyId_Type.__name__ = "DisplayString"
_AlarmEmailNotifyId_Object = MibTableColumn
alarmEmailNotifyId = _AlarmEmailNotifyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 3),
    _AlarmEmailNotifyId_Type()
)
alarmEmailNotifyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyId.setStatus("current")


class _AlarmEmailNotifySeverity_Type(Integer32):
    """Custom type alarmEmailNotifySeverity based on Integer32"""
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
        *(("low", 1),
          ("med", 2),
          ("high", 3),
          ("notReported", 4))
    )


_AlarmEmailNotifySeverity_Type.__name__ = "Integer32"
_AlarmEmailNotifySeverity_Object = MibTableColumn
alarmEmailNotifySeverity = _AlarmEmailNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 4),
    _AlarmEmailNotifySeverity_Type()
)
alarmEmailNotifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifySeverity.setStatus("current")
_AlarmEmailNotifyTimeStamp_Type = DateAndTime
_AlarmEmailNotifyTimeStamp_Object = MibTableColumn
alarmEmailNotifyTimeStamp = _AlarmEmailNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 5),
    _AlarmEmailNotifyTimeStamp_Type()
)
alarmEmailNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyTimeStamp.setStatus("current")


class _AlarmEmailNotifyFaultPosition_Type(DisplayString):
    """Custom type alarmEmailNotifyFaultPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlarmEmailNotifyFaultPosition_Type.__name__ = "DisplayString"
_AlarmEmailNotifyFaultPosition_Object = MibTableColumn
alarmEmailNotifyFaultPosition = _AlarmEmailNotifyFaultPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 6),
    _AlarmEmailNotifyFaultPosition_Type()
)
alarmEmailNotifyFaultPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyFaultPosition.setStatus("current")


class _AlarmEmailNotifyFaultType_Type(DisplayString):
    """Custom type alarmEmailNotifyFaultType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmEmailNotifyFaultType_Type.__name__ = "DisplayString"
_AlarmEmailNotifyFaultType_Object = MibTableColumn
alarmEmailNotifyFaultType = _AlarmEmailNotifyFaultType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 7),
    _AlarmEmailNotifyFaultType_Type()
)
alarmEmailNotifyFaultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEmailNotifyFaultType.setStatus("current")


class _AlarmEmailNotifyState_Type(DisplayString):
    """Custom type alarmEmailNotifyState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmEmailNotifyState_Type.__name__ = "DisplayString"
_AlarmEmailNotifyState_Object = MibTableColumn
alarmEmailNotifyState = _AlarmEmailNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 8),
    _AlarmEmailNotifyState_Type()
)
alarmEmailNotifyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEmailNotifyState.setStatus("current")


class _AlarmEmailNotifyEvent_Type(DisplayString):
    """Custom type alarmEmailNotifyEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlarmEmailNotifyEvent_Type.__name__ = "DisplayString"
_AlarmEmailNotifyEvent_Object = MibTableColumn
alarmEmailNotifyEvent = _AlarmEmailNotifyEvent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 9),
    _AlarmEmailNotifyEvent_Type()
)
alarmEmailNotifyEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEmailNotifyEvent.setStatus("current")
_AlarmEmailNotifyEventTimeStamp_Type = DateAndTime
_AlarmEmailNotifyEventTimeStamp_Object = MibTableColumn
alarmEmailNotifyEventTimeStamp = _AlarmEmailNotifyEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 10),
    _AlarmEmailNotifyEventTimeStamp_Type()
)
alarmEmailNotifyEventTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmEmailNotifyEventTimeStamp.setStatus("current")
_AlarmEmailNotifyFaultAnalysisReference_Type = Integer32
_AlarmEmailNotifyFaultAnalysisReference_Object = MibTableColumn
alarmEmailNotifyFaultAnalysisReference = _AlarmEmailNotifyFaultAnalysisReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 11),
    _AlarmEmailNotifyFaultAnalysisReference_Type()
)
alarmEmailNotifyFaultAnalysisReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyFaultAnalysisReference.setStatus("current")


class _AlarmEmailNotifyCorrectedFaultPos_Type(DisplayString):
    """Custom type alarmEmailNotifyCorrectedFaultPos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlarmEmailNotifyCorrectedFaultPos_Type.__name__ = "DisplayString"
_AlarmEmailNotifyCorrectedFaultPos_Object = MibTableColumn
alarmEmailNotifyCorrectedFaultPos = _AlarmEmailNotifyCorrectedFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 12),
    _AlarmEmailNotifyCorrectedFaultPos_Type()
)
alarmEmailNotifyCorrectedFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyCorrectedFaultPos.setStatus("current")


class _AlarmEmailNotifyFaultPosLatitude_Type(DisplayString):
    """Custom type alarmEmailNotifyFaultPosLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlarmEmailNotifyFaultPosLatitude_Type.__name__ = "DisplayString"
_AlarmEmailNotifyFaultPosLatitude_Object = MibTableColumn
alarmEmailNotifyFaultPosLatitude = _AlarmEmailNotifyFaultPosLatitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 13),
    _AlarmEmailNotifyFaultPosLatitude_Type()
)
alarmEmailNotifyFaultPosLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyFaultPosLatitude.setStatus("current")


class _AlarmEmailNotifyFaultPosLongitude_Type(DisplayString):
    """Custom type alarmEmailNotifyFaultPosLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AlarmEmailNotifyFaultPosLongitude_Type.__name__ = "DisplayString"
_AlarmEmailNotifyFaultPosLongitude_Object = MibTableColumn
alarmEmailNotifyFaultPosLongitude = _AlarmEmailNotifyFaultPosLongitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 3, 1, 14),
    _AlarmEmailNotifyFaultPosLongitude_Type()
)
alarmEmailNotifyFaultPosLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEmailNotifyFaultPosLongitude.setStatus("current")
_AlarmDescriptionTable_Object = MibTable
alarmDescriptionTable = _AlarmDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    alarmDescriptionTable.setStatus("current")
_AlarmDescriptionEntry_Object = MibTableRow
alarmDescriptionEntry = _AlarmDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 4, 1)
)
alarmDescriptionEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "alarmType"),
)
if mibBuilder.loadTexts:
    alarmDescriptionEntry.setStatus("current")
_AlarmDescriptionName_Type = DisplayString
_AlarmDescriptionName_Object = MibTableColumn
alarmDescriptionName = _AlarmDescriptionName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 4, 1, 2),
    _AlarmDescriptionName_Type()
)
alarmDescriptionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescriptionName.setStatus("current")


class _LossAlarmsMasking_Type(Integer32):
    """Custom type lossAlarmsMasking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LossAlarmsMasking_Type.__name__ = "Integer32"
_LossAlarmsMasking_Object = MibScalar
lossAlarmsMasking = _LossAlarmsMasking_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 1, 5),
    _LossAlarmsMasking_Type()
)
lossAlarmsMasking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lossAlarmsMasking.setStatus("current")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2)
)
_Shelf_ObjectIdentity = ObjectIdentity
shelf = _Shelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1)
)
_ShelfUnitName_Type = SnmpAdminString
_ShelfUnitName_Object = MibScalar
shelfUnitName = _ShelfUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 1),
    _ShelfUnitName_Type()
)
shelfUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfUnitName.setStatus("current")
_FirmwarePackageRev_Type = SnmpAdminString
_FirmwarePackageRev_Object = MibScalar
firmwarePackageRev = _FirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 2),
    _FirmwarePackageRev_Type()
)
firmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwarePackageRev.setStatus("current")
_HardwareRev_Type = SnmpAdminString
_HardwareRev_Object = MibScalar
hardwareRev = _HardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 3),
    _HardwareRev_Type()
)
hardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRev.setStatus("current")
_FpgaRev_Type = SnmpAdminString
_FpgaRev_Object = MibScalar
fpgaRev = _FpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 4),
    _FpgaRev_Type()
)
fpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpgaRev.setStatus("current")
_SerialNumber_Type = SnmpAdminString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 5),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_PartNumber_Type = SnmpAdminString
_PartNumber_Object = MibScalar
partNumber = _PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 6),
    _PartNumber_Type()
)
partNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partNumber.setStatus("current")
_CleiCode_Type = SnmpAdminString
_CleiCode_Object = MibScalar
cleiCode = _CleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 7),
    _CleiCode_Type()
)
cleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cleiCode.setStatus("current")
_VendorId_Type = SnmpAdminString
_VendorId_Object = MibScalar
vendorId = _VendorId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 8),
    _VendorId_Type()
)
vendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorId.setStatus("current")
_InventoryType_Type = SnmpAdminString
_InventoryType_Object = MibScalar
inventoryType = _InventoryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 9),
    _InventoryType_Type()
)
inventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryType.setStatus("current")
_UniversalSerialIdent_Type = SnmpAdminString
_UniversalSerialIdent_Object = MibScalar
universalSerialIdent = _UniversalSerialIdent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 10),
    _UniversalSerialIdent_Type()
)
universalSerialIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    universalSerialIdent.setStatus("current")
_TempCPU_Type = Integer32
_TempCPU_Object = MibScalar
tempCPU = _TempCPU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 11),
    _TempCPU_Type()
)
tempCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCPU.setStatus("current")
if mibBuilder.loadTexts:
    tempCPU.setUnits("0.1 C")
_ThresholdMaxTempCPU_Type = Integer32
_ThresholdMaxTempCPU_Object = MibScalar
thresholdMaxTempCPU = _ThresholdMaxTempCPU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 12),
    _ThresholdMaxTempCPU_Type()
)
thresholdMaxTempCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMaxTempCPU.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMaxTempCPU.setUnits("0.1 C")
_TempBoard1_Type = Integer32
_TempBoard1_Object = MibScalar
tempBoard1 = _TempBoard1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 13),
    _TempBoard1_Type()
)
tempBoard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempBoard1.setStatus("current")
if mibBuilder.loadTexts:
    tempBoard1.setUnits("0.1 C")
_ThresholdMaxTempBoard1_Type = Integer32
_ThresholdMaxTempBoard1_Object = MibScalar
thresholdMaxTempBoard1 = _ThresholdMaxTempBoard1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 14),
    _ThresholdMaxTempBoard1_Type()
)
thresholdMaxTempBoard1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMaxTempBoard1.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMaxTempBoard1.setUnits("0.1 C")
_TempBoard2_Type = Integer32
_TempBoard2_Object = MibScalar
tempBoard2 = _TempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 15),
    _TempBoard2_Type()
)
tempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempBoard2.setStatus("current")
if mibBuilder.loadTexts:
    tempBoard2.setUnits("0.1 C")
_ThresholdMinTempBoard2_Type = Integer32
_ThresholdMinTempBoard2_Object = MibScalar
thresholdMinTempBoard2 = _ThresholdMinTempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 16),
    _ThresholdMinTempBoard2_Type()
)
thresholdMinTempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMinTempBoard2.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMinTempBoard2.setUnits("0.1 C")
_ThresholdMaxTempBoard2_Type = Integer32
_ThresholdMaxTempBoard2_Object = MibScalar
thresholdMaxTempBoard2 = _ThresholdMaxTempBoard2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 17),
    _ThresholdMaxTempBoard2_Type()
)
thresholdMaxTempBoard2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMaxTempBoard2.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMaxTempBoard2.setUnits("0.1 C")
_TempLaser_Type = Integer32
_TempLaser_Object = MibScalar
tempLaser = _TempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 18),
    _TempLaser_Type()
)
tempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLaser.setStatus("current")
if mibBuilder.loadTexts:
    tempLaser.setUnits("0.1 C")
_ThresholdMinTempLaser_Type = Integer32
_ThresholdMinTempLaser_Object = MibScalar
thresholdMinTempLaser = _ThresholdMinTempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 19),
    _ThresholdMinTempLaser_Type()
)
thresholdMinTempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMinTempLaser.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMinTempLaser.setUnits("0.1 C")
_ThresholdMaxTempLaser_Type = Integer32
_ThresholdMaxTempLaser_Object = MibScalar
thresholdMaxTempLaser = _ThresholdMaxTempLaser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 20),
    _ThresholdMaxTempLaser_Type()
)
thresholdMaxTempLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdMaxTempLaser.setStatus("current")
if mibBuilder.loadTexts:
    thresholdMaxTempLaser.setUnits("0.1 C")


class _AidString_Type(OctetString):
    """Custom type aidString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AidString_Type.__name__ = "OctetString"
_AidString_Object = MibScalar
aidString = _AidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 21),
    _AidString_Type()
)
aidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aidString.setStatus("current")


class _ShelfName_Type(DisplayString):
    """Custom type shelfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ShelfName_Type.__name__ = "DisplayString"
_ShelfName_Object = MibScalar
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 1, 22),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1)
)
portEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortId_Type(Integer32):
    """Custom type portId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 898),
    )


_PortId_Type.__name__ = "Integer32"
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portId.setStatus("current")


class _PortAdminState_Type(Integer32):
    """Custom type portAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("is", 2),
          ("mgt", 4),
          ("dsbld", 6))
    )


_PortAdminState_Type.__name__ = "Integer32"
_PortAdminState_Object = MibTableColumn
portAdminState = _PortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 2),
    _PortAdminState_Type()
)
portAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminState.setStatus("current")


class _PortOperState_Type(Integer32):
    """Custom type portOperState based on Integer32"""
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
        *(("undefined", 0),
          ("nr", 1),
          ("anr", 2),
          ("out", 3),
          ("un", 4))
    )


_PortOperState_Type.__name__ = "Integer32"
_PortOperState_Object = MibTableColumn
portOperState = _PortOperState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 3),
    _PortOperState_Type()
)
portOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperState.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 4),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_PortAidString_Type = IdentityTranslation
_PortAidString_Object = MibTableColumn
portAidString = _PortAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 5),
    _PortAidString_Type()
)
portAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAidString.setStatus("current")


class _PortRemark_Type(DisplayString):
    """Custom type portRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortRemark_Type.__name__ = "DisplayString"
_PortRemark_Object = MibTableColumn
portRemark = _PortRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 6),
    _PortRemark_Type()
)
portRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portRemark.setStatus("current")


class _PortFingerprintMode_Type(Integer32):
    """Custom type portFingerprintMode based on Integer32"""
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
          ("pointToPointWithRefl", 1),
          ("pointToPointWithoutRefl", 2),
          ("pon", 3),
          ("pes", 4),
          ("adl", 5))
    )


_PortFingerprintMode_Type.__name__ = "Integer32"
_PortFingerprintMode_Object = MibTableColumn
portFingerprintMode = _PortFingerprintMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 7),
    _PortFingerprintMode_Type()
)
portFingerprintMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFingerprintMode.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("high", 2))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 8),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")


class _PortGisConfigured_Type(Integer32):
    """Custom type portGisConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortGisConfigured_Type.__name__ = "Integer32"
_PortGisConfigured_Object = MibTableColumn
portGisConfigured = _PortGisConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 9),
    _PortGisConfigured_Type()
)
portGisConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portGisConfigured.setStatus("current")
_PortConnectedInternalChannel_Type = IdentityTranslation
_PortConnectedInternalChannel_Object = MibTableColumn
portConnectedInternalChannel = _PortConnectedInternalChannel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 10),
    _PortConnectedInternalChannel_Type()
)
portConnectedInternalChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConnectedInternalChannel.setStatus("current")


class _PortPmData_Type(Integer32):
    """Custom type portPmData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PortPmData_Type.__name__ = "Integer32"
_PortPmData_Object = MibTableColumn
portPmData = _PortPmData_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 2, 1, 11),
    _PortPmData_Type()
)
portPmData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPmData.setStatus("current")
_MonitoringItems_ObjectIdentity = ObjectIdentity
monitoringItems = _MonitoringItems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3)
)
_FeederLengthTable_Object = MibTable
feederLengthTable = _FeederLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 1)
)
if mibBuilder.loadTexts:
    feederLengthTable.setStatus("current")
_FeederLengthEntry_Object = MibTableRow
feederLengthEntry = _FeederLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 1, 1)
)
feederLengthEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    feederLengthEntry.setStatus("current")
_FeederLength_Type = Integer32
_FeederLength_Object = MibTableColumn
feederLength = _FeederLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 1, 1, 1),
    _FeederLength_Type()
)
feederLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feederLength.setStatus("current")
if mibBuilder.loadTexts:
    feederLength.setUnits("0.1 m")
_MonitorPointTable_Object = MibTable
monitorPointTable = _MonitorPointTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2)
)
if mibBuilder.loadTexts:
    monitorPointTable.setStatus("current")
_MonitorPointEntry_Object = MibTableRow
monitorPointEntry = _MonitorPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1)
)
monitorPointEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "mpId"),
)
if mibBuilder.loadTexts:
    monitorPointEntry.setStatus("current")


class _MpId_Type(Integer32):
    """Custom type mpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MpId_Type.__name__ = "Integer32"
_MpId_Object = MibTableColumn
mpId = _MpId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 1),
    _MpId_Type()
)
mpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpId.setStatus("current")
_MonitorPointPos_Type = Integer32
_MonitorPointPos_Object = MibTableColumn
monitorPointPos = _MonitorPointPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 2),
    _MonitorPointPos_Type()
)
monitorPointPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointPos.setStatus("current")
if mibBuilder.loadTexts:
    monitorPointPos.setUnits("0.1 m")


class _MonitorPointState_Type(Integer32):
    """Custom type monitorPointState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_MonitorPointState_Type.__name__ = "Integer32"
_MonitorPointState_Object = MibTableColumn
monitorPointState = _MonitorPointState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 3),
    _MonitorPointState_Type()
)
monitorPointState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPointState.setStatus("current")


class _MonitorPointName_Type(DisplayString):
    """Custom type monitorPointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MonitorPointName_Type.__name__ = "DisplayString"
_MonitorPointName_Object = MibTableColumn
monitorPointName = _MonitorPointName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 4),
    _MonitorPointName_Type()
)
monitorPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPointName.setStatus("current")
_MonitorPointAidString_Type = IdentityTranslation
_MonitorPointAidString_Object = MibTableColumn
monitorPointAidString = _MonitorPointAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 5),
    _MonitorPointAidString_Type()
)
monitorPointAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointAidString.setStatus("current")


class _MonitorPointRemark_Type(DisplayString):
    """Custom type monitorPointRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MonitorPointRemark_Type.__name__ = "DisplayString"
_MonitorPointRemark_Object = MibTableColumn
monitorPointRemark = _MonitorPointRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 6),
    _MonitorPointRemark_Type()
)
monitorPointRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPointRemark.setStatus("current")


class _MonitorPointExternalId_Type(DisplayString):
    """Custom type monitorPointExternalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MonitorPointExternalId_Type.__name__ = "DisplayString"
_MonitorPointExternalId_Object = MibTableColumn
monitorPointExternalId = _MonitorPointExternalId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 3, 2, 1, 7),
    _MonitorPointExternalId_Type()
)
monitorPointExternalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPointExternalId.setStatus("current")
_ExtShelfTable_Object = MibTable
extShelfTable = _ExtShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4)
)
if mibBuilder.loadTexts:
    extShelfTable.setStatus("current")
_ExtShelfEntry_Object = MibTableRow
extShelfEntry = _ExtShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1)
)
extShelfEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "extShelfNo"),
)
if mibBuilder.loadTexts:
    extShelfEntry.setStatus("current")


class _ExtShelfNo_Type(Integer32):
    """Custom type extShelfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ExtShelfNo_Type.__name__ = "Integer32"
_ExtShelfNo_Object = MibTableColumn
extShelfNo = _ExtShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 1),
    _ExtShelfNo_Type()
)
extShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extShelfNo.setStatus("current")
_ExtShelfRowStatus_Type = RowStatus
_ExtShelfRowStatus_Object = MibTableColumn
extShelfRowStatus = _ExtShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 2),
    _ExtShelfRowStatus_Type()
)
extShelfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extShelfRowStatus.setStatus("current")
_ExtShelfType_Type = SnmpAdminString
_ExtShelfType_Object = MibTableColumn
extShelfType = _ExtShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 3),
    _ExtShelfType_Type()
)
extShelfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extShelfType.setStatus("current")
_ExtShelfAidString_Type = IdentityTranslation
_ExtShelfAidString_Object = MibTableColumn
extShelfAidString = _ExtShelfAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 4),
    _ExtShelfAidString_Type()
)
extShelfAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extShelfAidString.setStatus("current")


class _ExtShelfInternalId_Type(Integer32):
    """Custom type extShelfInternalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(91, 98),
    )


_ExtShelfInternalId_Type.__name__ = "Integer32"
_ExtShelfInternalId_Object = MibTableColumn
extShelfInternalId = _ExtShelfInternalId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 5),
    _ExtShelfInternalId_Type()
)
extShelfInternalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extShelfInternalId.setStatus("current")


class _ExtShelfNrInternalPorts_Type(Integer32):
    """Custom type extShelfNrInternalPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(8, 8),
    )


_ExtShelfNrInternalPorts_Type.__name__ = "Integer32"
_ExtShelfNrInternalPorts_Object = MibTableColumn
extShelfNrInternalPorts = _ExtShelfNrInternalPorts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 6),
    _ExtShelfNrInternalPorts_Type()
)
extShelfNrInternalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extShelfNrInternalPorts.setStatus("current")


class _ExtShelfNrMonitorPorts_Type(Integer32):
    """Custom type extShelfNrMonitorPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(384, 384),
    )


_ExtShelfNrMonitorPorts_Type.__name__ = "Integer32"
_ExtShelfNrMonitorPorts_Object = MibTableColumn
extShelfNrMonitorPorts = _ExtShelfNrMonitorPorts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 7),
    _ExtShelfNrMonitorPorts_Type()
)
extShelfNrMonitorPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extShelfNrMonitorPorts.setStatus("current")


class _ExtShelfName_Type(DisplayString):
    """Custom type extShelfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExtShelfName_Type.__name__ = "DisplayString"
_ExtShelfName_Object = MibTableColumn
extShelfName = _ExtShelfName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 8),
    _ExtShelfName_Type()
)
extShelfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extShelfName.setStatus("current")


class _ExtShelfRemark_Type(DisplayString):
    """Custom type extShelfRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExtShelfRemark_Type.__name__ = "DisplayString"
_ExtShelfRemark_Object = MibTableColumn
extShelfRemark = _ExtShelfRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 4, 1, 9),
    _ExtShelfRemark_Type()
)
extShelfRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extShelfRemark.setStatus("current")
_EntityPortTable_Object = MibTable
entityPortTable = _EntityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5)
)
if mibBuilder.loadTexts:
    entityPortTable.setStatus("current")
_EntityPortEntry_Object = MibTableRow
entityPortEntry = _EntityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5, 1)
)
entityPortEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "inventoryShelfNo"),
    (0, "ADVA-FSP3000ALM-MIB", "entityPortInternalNo"),
    (0, "ADVA-FSP3000ALM-MIB", "entityPortPortNo"),
)
if mibBuilder.loadTexts:
    entityPortEntry.setStatus("current")


class _EntityPortInternalNo_Type(Integer32):
    """Custom type entityPortInternalNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(65, 72),
    )


_EntityPortInternalNo_Type.__name__ = "Integer32"
_EntityPortInternalNo_Object = MibTableColumn
entityPortInternalNo = _EntityPortInternalNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5, 1, 1),
    _EntityPortInternalNo_Type()
)
entityPortInternalNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entityPortInternalNo.setStatus("current")


class _EntityPortPortNo_Type(Integer32):
    """Custom type entityPortPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_EntityPortPortNo_Type.__name__ = "Integer32"
_EntityPortPortNo_Object = MibTableColumn
entityPortPortNo = _EntityPortPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5, 1, 2),
    _EntityPortPortNo_Type()
)
entityPortPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entityPortPortNo.setStatus("current")
_EntityPortAidString_Type = IdentityTranslation
_EntityPortAidString_Object = MibTableColumn
entityPortAidString = _EntityPortAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5, 1, 3),
    _EntityPortAidString_Type()
)
entityPortAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortAidString.setStatus("current")
_EntityPortPortId_Type = Integer32
_EntityPortPortId_Object = MibTableColumn
entityPortPortId = _EntityPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 2, 5, 1, 4),
    _EntityPortPortId_Type()
)
entityPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entityPortPortId.setStatus("current")
_Measurement_ObjectIdentity = ObjectIdentity
measurement = _Measurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3)
)
_MeasurementLossTable_Object = MibTable
measurementLossTable = _MeasurementLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    measurementLossTable.setStatus("current")
_MeasurementLossEntry_Object = MibTableRow
measurementLossEntry = _MeasurementLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1)
)
measurementLossEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementLossIndex"),
)
if mibBuilder.loadTexts:
    measurementLossEntry.setStatus("current")


class _MeasurementLossIndex_Type(Integer32):
    """Custom type measurementLossIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementLossIndex_Type.__name__ = "Integer32"
_MeasurementLossIndex_Object = MibTableColumn
measurementLossIndex = _MeasurementLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 1),
    _MeasurementLossIndex_Type()
)
measurementLossIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossIndex.setStatus("current")


class _MeasurementLossLinkLoss_Type(Integer32):
    """Custom type measurementLossLinkLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_MeasurementLossLinkLoss_Type.__name__ = "Integer32"
_MeasurementLossLinkLoss_Object = MibTableColumn
measurementLossLinkLoss = _MeasurementLossLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 2),
    _MeasurementLossLinkLoss_Type()
)
measurementLossLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkLoss.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossLinkLoss.setUnits("0.1 dB")
_MeasurementLossLinkFaultLoc_Type = Integer32
_MeasurementLossLinkFaultLoc_Object = MibTableColumn
measurementLossLinkFaultLoc = _MeasurementLossLinkFaultLoc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 3),
    _MeasurementLossLinkFaultLoc_Type()
)
measurementLossLinkFaultLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLoc.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLoc.setUnits("0.1 m")
_MeasurementLossLinkFaultLocRes_Type = Integer32
_MeasurementLossLinkFaultLocRes_Object = MibTableColumn
measurementLossLinkFaultLocRes = _MeasurementLossLinkFaultLocRes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 4),
    _MeasurementLossLinkFaultLocRes_Type()
)
measurementLossLinkFaultLocRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLocRes.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossLinkFaultLocRes.setUnits("0.1 m")
_MeasurementLossDevFast_Type = Integer32
_MeasurementLossDevFast_Object = MibTableColumn
measurementLossDevFast = _MeasurementLossDevFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 5),
    _MeasurementLossDevFast_Type()
)
measurementLossDevFast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevFast.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossDevFast.setUnits("0.1 dB")
_MeasurementLossDevMedium_Type = Integer32
_MeasurementLossDevMedium_Object = MibTableColumn
measurementLossDevMedium = _MeasurementLossDevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 6),
    _MeasurementLossDevMedium_Type()
)
measurementLossDevMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevMedium.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossDevMedium.setUnits("0.1 dB")
_MeasurementLossDevSlow_Type = Integer32
_MeasurementLossDevSlow_Object = MibTableColumn
measurementLossDevSlow = _MeasurementLossDevSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 7),
    _MeasurementLossDevSlow_Type()
)
measurementLossDevSlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDevSlow.setStatus("current")
if mibBuilder.loadTexts:
    measurementLossDevSlow.setUnits("0.1 dB")
_MeasurementLossDataTimestamp_Type = DateAndTime
_MeasurementLossDataTimestamp_Object = MibTableColumn
measurementLossDataTimestamp = _MeasurementLossDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 1, 1, 8),
    _MeasurementLossDataTimestamp_Type()
)
measurementLossDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementLossDataTimestamp.setStatus("current")
_HistMeasLoss15MinTable_Object = MibTable
histMeasLoss15MinTable = _HistMeasLoss15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4)
)
if mibBuilder.loadTexts:
    histMeasLoss15MinTable.setStatus("current")
_HistMeasLoss15MinEntry_Object = MibTableRow
histMeasLoss15MinEntry = _HistMeasLoss15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1)
)
histMeasLoss15MinEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMeasLoss15MinNumber"),
)
if mibBuilder.loadTexts:
    histMeasLoss15MinEntry.setStatus("current")


class _HistMeasLoss15MinNumber_Type(Integer32):
    """Custom type histMeasLoss15MinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_HistMeasLoss15MinNumber_Type.__name__ = "Integer32"
_HistMeasLoss15MinNumber_Object = MibTableColumn
histMeasLoss15MinNumber = _HistMeasLoss15MinNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 1),
    _HistMeasLoss15MinNumber_Type()
)
histMeasLoss15MinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMeasLoss15MinNumber.setStatus("current")
_HistMeasLoss15MinLow_Type = Integer32
_HistMeasLoss15MinLow_Object = MibTableColumn
histMeasLoss15MinLow = _HistMeasLoss15MinLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 2),
    _HistMeasLoss15MinLow_Type()
)
histMeasLoss15MinLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLow.setUnits("0.1 dB")
_HistMeasLoss15MinMean_Type = Integer32
_HistMeasLoss15MinMean_Object = MibTableColumn
histMeasLoss15MinMean = _HistMeasLoss15MinMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 3),
    _HistMeasLoss15MinMean_Type()
)
histMeasLoss15MinMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinMean.setUnits("0.1 dB")
_HistMeasLoss15MinHigh_Type = Integer32
_HistMeasLoss15MinHigh_Object = MibTableColumn
histMeasLoss15MinHigh = _HistMeasLoss15MinHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 4),
    _HistMeasLoss15MinHigh_Type()
)
histMeasLoss15MinHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinHigh.setUnits("0.1 dB")
_HistMeasLoss15MinValidFlag_Type = TruthValue
_HistMeasLoss15MinValidFlag_Object = MibTableColumn
histMeasLoss15MinValidFlag = _HistMeasLoss15MinValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 5),
    _HistMeasLoss15MinValidFlag_Type()
)
histMeasLoss15MinValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinValidFlag.setStatus("current")
_HistMeasLoss15MinTimeStamp_Type = DateAndTime
_HistMeasLoss15MinTimeStamp_Object = MibTableColumn
histMeasLoss15MinTimeStamp = _HistMeasLoss15MinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 6),
    _HistMeasLoss15MinTimeStamp_Type()
)
histMeasLoss15MinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinTimeStamp.setStatus("current")
_HistMeasLoss15MinLength_Type = Integer32
_HistMeasLoss15MinLength_Object = MibTableColumn
histMeasLoss15MinLength = _HistMeasLoss15MinLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 7),
    _HistMeasLoss15MinLength_Type()
)
histMeasLoss15MinLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLength.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLength.setUnits("0.1 m")
_HistMeasLoss15MinLossPerKmLow_Type = Integer32
_HistMeasLoss15MinLossPerKmLow_Object = MibTableColumn
histMeasLoss15MinLossPerKmLow = _HistMeasLoss15MinLossPerKmLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 8),
    _HistMeasLoss15MinLossPerKmLow_Type()
)
histMeasLoss15MinLossPerKmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmLow.setUnits("0.01 dB/km")
_HistMeasLoss15MinLossPerKmMean_Type = Integer32
_HistMeasLoss15MinLossPerKmMean_Object = MibTableColumn
histMeasLoss15MinLossPerKmMean = _HistMeasLoss15MinLossPerKmMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 9),
    _HistMeasLoss15MinLossPerKmMean_Type()
)
histMeasLoss15MinLossPerKmMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmMean.setUnits("0.01 dB/km")
_HistMeasLoss15MinLossPerKmHigh_Type = Integer32
_HistMeasLoss15MinLossPerKmHigh_Object = MibTableColumn
histMeasLoss15MinLossPerKmHigh = _HistMeasLoss15MinLossPerKmHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 4, 1, 10),
    _HistMeasLoss15MinLossPerKmHigh_Type()
)
histMeasLoss15MinLossPerKmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss15MinLossPerKmHigh.setUnits("0.01 dB/km")
_HistMeasLoss1DayTable_Object = MibTable
histMeasLoss1DayTable = _HistMeasLoss1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5)
)
if mibBuilder.loadTexts:
    histMeasLoss1DayTable.setStatus("current")
_HistMeasLoss1DayEntry_Object = MibTableRow
histMeasLoss1DayEntry = _HistMeasLoss1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1)
)
histMeasLoss1DayEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMeasLoss1DayNumber"),
)
if mibBuilder.loadTexts:
    histMeasLoss1DayEntry.setStatus("current")


class _HistMeasLoss1DayNumber_Type(Integer32):
    """Custom type histMeasLoss1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HistMeasLoss1DayNumber_Type.__name__ = "Integer32"
_HistMeasLoss1DayNumber_Object = MibTableColumn
histMeasLoss1DayNumber = _HistMeasLoss1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 1),
    _HistMeasLoss1DayNumber_Type()
)
histMeasLoss1DayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMeasLoss1DayNumber.setStatus("current")
_HistMeasLoss1DayLow_Type = Integer32
_HistMeasLoss1DayLow_Object = MibTableColumn
histMeasLoss1DayLow = _HistMeasLoss1DayLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 2),
    _HistMeasLoss1DayLow_Type()
)
histMeasLoss1DayLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLow.setUnits("0.1 dB")
_HistMeasLoss1DayMean_Type = Integer32
_HistMeasLoss1DayMean_Object = MibTableColumn
histMeasLoss1DayMean = _HistMeasLoss1DayMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 3),
    _HistMeasLoss1DayMean_Type()
)
histMeasLoss1DayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayMean.setUnits("0.1 dB")
_HistMeasLoss1DayHigh_Type = Integer32
_HistMeasLoss1DayHigh_Object = MibTableColumn
histMeasLoss1DayHigh = _HistMeasLoss1DayHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 4),
    _HistMeasLoss1DayHigh_Type()
)
histMeasLoss1DayHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayHigh.setUnits("0.1 dB")
_HistMeasLoss1DayValidFlag_Type = TruthValue
_HistMeasLoss1DayValidFlag_Object = MibTableColumn
histMeasLoss1DayValidFlag = _HistMeasLoss1DayValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 5),
    _HistMeasLoss1DayValidFlag_Type()
)
histMeasLoss1DayValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayValidFlag.setStatus("current")
_HistMeasLoss1DayTimeStamp_Type = DateAndTime
_HistMeasLoss1DayTimeStamp_Object = MibTableColumn
histMeasLoss1DayTimeStamp = _HistMeasLoss1DayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 6),
    _HistMeasLoss1DayTimeStamp_Type()
)
histMeasLoss1DayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayTimeStamp.setStatus("current")
_HistMeasLoss1DayLength_Type = Integer32
_HistMeasLoss1DayLength_Object = MibTableColumn
histMeasLoss1DayLength = _HistMeasLoss1DayLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 7),
    _HistMeasLoss1DayLength_Type()
)
histMeasLoss1DayLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLength.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLength.setUnits("0.1 m")
_HistMeasLoss1DayLossPerKmLow_Type = Integer32
_HistMeasLoss1DayLossPerKmLow_Object = MibTableColumn
histMeasLoss1DayLossPerKmLow = _HistMeasLoss1DayLossPerKmLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 8),
    _HistMeasLoss1DayLossPerKmLow_Type()
)
histMeasLoss1DayLossPerKmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmLow.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmLow.setUnits("0.01 dB/km")
_HistMeasLoss1DayLossPerKmMean_Type = Integer32
_HistMeasLoss1DayLossPerKmMean_Object = MibTableColumn
histMeasLoss1DayLossPerKmMean = _HistMeasLoss1DayLossPerKmMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 9),
    _HistMeasLoss1DayLossPerKmMean_Type()
)
histMeasLoss1DayLossPerKmMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmMean.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmMean.setUnits("0.01 dB/km")
_HistMeasLoss1DayLossPerKmHigh_Type = Integer32
_HistMeasLoss1DayLossPerKmHigh_Object = MibTableColumn
histMeasLoss1DayLossPerKmHigh = _HistMeasLoss1DayLossPerKmHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 5, 1, 10),
    _HistMeasLoss1DayLossPerKmHigh_Type()
)
histMeasLoss1DayLossPerKmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMeasLoss1DayLossPerKmHigh.setUnits("0.01 dB/km")
_PortThresTable_Object = MibTable
portThresTable = _PortThresTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6)
)
if mibBuilder.loadTexts:
    portThresTable.setStatus("current")
_PortThresEntry_Object = MibTableRow
portThresEntry = _PortThresEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1)
)
portThresEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portThresEntry.setStatus("current")
_PortThresDeviationFast_Type = Integer32
_PortThresDeviationFast_Object = MibTableColumn
portThresDeviationFast = _PortThresDeviationFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 2),
    _PortThresDeviationFast_Type()
)
portThresDeviationFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationFast.setStatus("current")
if mibBuilder.loadTexts:
    portThresDeviationFast.setUnits("0.1 dB")
_PortThresDeviationMedium_Type = Integer32
_PortThresDeviationMedium_Object = MibTableColumn
portThresDeviationMedium = _PortThresDeviationMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 3),
    _PortThresDeviationMedium_Type()
)
portThresDeviationMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationMedium.setStatus("current")
if mibBuilder.loadTexts:
    portThresDeviationMedium.setUnits("0.1 dB")
_PortThresDeviationSlow_Type = Integer32
_PortThresDeviationSlow_Object = MibTableColumn
portThresDeviationSlow = _PortThresDeviationSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 4),
    _PortThresDeviationSlow_Type()
)
portThresDeviationSlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresDeviationSlow.setStatus("current")
if mibBuilder.loadTexts:
    portThresDeviationSlow.setUnits("0.1 dB")
_PortThresBudget_Type = Integer32
_PortThresBudget_Object = MibTableColumn
portThresBudget = _PortThresBudget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 5),
    _PortThresBudget_Type()
)
portThresBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresBudget.setStatus("current")
if mibBuilder.loadTexts:
    portThresBudget.setUnits("0.1 dB")
_PortThresCloseToBudget_Type = Integer32
_PortThresCloseToBudget_Object = MibTableColumn
portThresCloseToBudget = _PortThresCloseToBudget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 6),
    _PortThresCloseToBudget_Type()
)
portThresCloseToBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresCloseToBudget.setStatus("current")
if mibBuilder.loadTexts:
    portThresCloseToBudget.setUnits("0.1 dB")
_PortMonitorThresLossBudget_Type = Integer32
_PortMonitorThresLossBudget_Object = MibTableColumn
portMonitorThresLossBudget = _PortMonitorThresLossBudget_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 7),
    _PortMonitorThresLossBudget_Type()
)
portMonitorThresLossBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonitorThresLossBudget.setStatus("current")
if mibBuilder.loadTexts:
    portMonitorThresLossBudget.setUnits("0.1 dB")
_PortMonitorThresDeviation_Type = Integer32
_PortMonitorThresDeviation_Object = MibTableColumn
portMonitorThresDeviation = _PortMonitorThresDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 8),
    _PortMonitorThresDeviation_Type()
)
portMonitorThresDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMonitorThresDeviation.setStatus("current")
if mibBuilder.loadTexts:
    portMonitorThresDeviation.setUnits("0.1 dB")
_PortSensor1Thres_Type = Integer32
_PortSensor1Thres_Object = MibTableColumn
portSensor1Thres = _PortSensor1Thres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 9),
    _PortSensor1Thres_Type()
)
portSensor1Thres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSensor1Thres.setStatus("current")
if mibBuilder.loadTexts:
    portSensor1Thres.setUnits("0.1 dB")
_PortSensor2Thres_Type = Integer32
_PortSensor2Thres_Object = MibTableColumn
portSensor2Thres = _PortSensor2Thres_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 10),
    _PortSensor2Thres_Type()
)
portSensor2Thres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSensor2Thres.setStatus("current")
if mibBuilder.loadTexts:
    portSensor2Thres.setUnits("0.1 dB")


class _PortAutoThresAdjustment_Type(Integer32):
    """Custom type portAutoThresAdjustment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PortAutoThresAdjustment_Type.__name__ = "Integer32"
_PortAutoThresAdjustment_Object = MibTableColumn
portAutoThresAdjustment = _PortAutoThresAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 11),
    _PortAutoThresAdjustment_Type()
)
portAutoThresAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutoThresAdjustment.setStatus("current")
_PortThresBudgetMargin_Type = Integer32
_PortThresBudgetMargin_Object = MibTableColumn
portThresBudgetMargin = _PortThresBudgetMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 12),
    _PortThresBudgetMargin_Type()
)
portThresBudgetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresBudgetMargin.setStatus("current")
if mibBuilder.loadTexts:
    portThresBudgetMargin.setUnits("0.1 dB")
_PortThresCloseToBudgetMargin_Type = Integer32
_PortThresCloseToBudgetMargin_Object = MibTableColumn
portThresCloseToBudgetMargin = _PortThresCloseToBudgetMargin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 13),
    _PortThresCloseToBudgetMargin_Type()
)
portThresCloseToBudgetMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresCloseToBudgetMargin.setStatus("current")
if mibBuilder.loadTexts:
    portThresCloseToBudgetMargin.setUnits("0.1 dB")
_PortThresAddDropHigh_Type = Integer32
_PortThresAddDropHigh_Object = MibTableColumn
portThresAddDropHigh = _PortThresAddDropHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 14),
    _PortThresAddDropHigh_Type()
)
portThresAddDropHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresAddDropHigh.setStatus("current")
if mibBuilder.loadTexts:
    portThresAddDropHigh.setUnits("0.1 dB")
_PortThresAddDropDeviation_Type = Integer32
_PortThresAddDropDeviation_Object = MibTableColumn
portThresAddDropDeviation = _PortThresAddDropDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 6, 1, 15),
    _PortThresAddDropDeviation_Type()
)
portThresAddDropDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portThresAddDropDeviation.setStatus("current")
if mibBuilder.loadTexts:
    portThresAddDropDeviation.setUnits("0.1 dB")
_PortPeriodLossDevTable_Object = MibTable
portPeriodLossDevTable = _PortPeriodLossDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7)
)
if mibBuilder.loadTexts:
    portPeriodLossDevTable.setStatus("current")
_PortPeriodLossDevEntry_Object = MibTableRow
portPeriodLossDevEntry = _PortPeriodLossDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1)
)
portPeriodLossDevEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portPeriodLossDevEntry.setStatus("current")
_PortPeriodLossDevFast_Type = Integer32
_PortPeriodLossDevFast_Object = MibTableColumn
portPeriodLossDevFast = _PortPeriodLossDevFast_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 1),
    _PortPeriodLossDevFast_Type()
)
portPeriodLossDevFast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevFast.setStatus("current")
if mibBuilder.loadTexts:
    portPeriodLossDevFast.setUnits("min")
_PortPeriodLossDevMedium_Type = Integer32
_PortPeriodLossDevMedium_Object = MibTableColumn
portPeriodLossDevMedium = _PortPeriodLossDevMedium_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 2),
    _PortPeriodLossDevMedium_Type()
)
portPeriodLossDevMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevMedium.setStatus("current")
if mibBuilder.loadTexts:
    portPeriodLossDevMedium.setUnits("h")
_PortPeriodLossDevSlow_Type = Integer32
_PortPeriodLossDevSlow_Object = MibTableColumn
portPeriodLossDevSlow = _PortPeriodLossDevSlow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 7, 1, 3),
    _PortPeriodLossDevSlow_Type()
)
portPeriodLossDevSlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPeriodLossDevSlow.setStatus("current")
if mibBuilder.loadTexts:
    portPeriodLossDevSlow.setUnits("d")
_MeasurementFpTable_Object = MibTable
measurementFpTable = _MeasurementFpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8)
)
if mibBuilder.loadTexts:
    measurementFpTable.setStatus("current")
_MeasurementFpEntry_Object = MibTableRow
measurementFpEntry = _MeasurementFpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1)
)
measurementFpEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementFpIndex"),
)
if mibBuilder.loadTexts:
    measurementFpEntry.setStatus("current")


class _MeasurementFpIndex_Type(Integer32):
    """Custom type measurementFpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementFpIndex_Type.__name__ = "Integer32"
_MeasurementFpIndex_Object = MibTableColumn
measurementFpIndex = _MeasurementFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 1),
    _MeasurementFpIndex_Type()
)
measurementFpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementFpIndex.setStatus("current")


class _MeasurementFpRefractiveIndex_Type(Integer32):
    """Custom type measurementFpRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MeasurementFpRefractiveIndex_Type.__name__ = "Integer32"
_MeasurementFpRefractiveIndex_Object = MibTableColumn
measurementFpRefractiveIndex = _MeasurementFpRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 2),
    _MeasurementFpRefractiveIndex_Type()
)
measurementFpRefractiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpRefractiveIndex.setStatus("current")


class _MeasurementFpExternalOffset_Type(Integer32):
    """Custom type measurementFpExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementFpExternalOffset_Type.__name__ = "Integer32"
_MeasurementFpExternalOffset_Object = MibTableColumn
measurementFpExternalOffset = _MeasurementFpExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 3),
    _MeasurementFpExternalOffset_Type()
)
measurementFpExternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpExternalOffset.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpExternalOffset.setUnits("m")


class _MeasurementFpCouplerLoss_Type(Integer32):
    """Custom type measurementFpCouplerLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementFpCouplerLoss_Type.__name__ = "Integer32"
_MeasurementFpCouplerLoss_Object = MibTableColumn
measurementFpCouplerLoss = _MeasurementFpCouplerLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 4),
    _MeasurementFpCouplerLoss_Type()
)
measurementFpCouplerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpCouplerLoss.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpCouplerLoss.setUnits("0.1 dB")
_MeasurementFpLinkLoss_Type = Integer32
_MeasurementFpLinkLoss_Object = MibTableColumn
measurementFpLinkLoss = _MeasurementFpLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 5),
    _MeasurementFpLinkLoss_Type()
)
measurementFpLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpLinkLoss.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpLinkLoss.setUnits("0.1 dB")
_MeasurementFpLineEndPos_Type = Integer32
_MeasurementFpLineEndPos_Object = MibTableColumn
measurementFpLineEndPos = _MeasurementFpLineEndPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 6),
    _MeasurementFpLineEndPos_Type()
)
measurementFpLineEndPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpLineEndPos.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpLineEndPos.setUnits("0.1 m")
_MeasurementFpDataTimestamp_Type = DateAndTime
_MeasurementFpDataTimestamp_Object = MibTableColumn
measurementFpDataTimestamp = _MeasurementFpDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 7),
    _MeasurementFpDataTimestamp_Type()
)
measurementFpDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpDataTimestamp.setStatus("current")


class _MeasurementFpNumConnectors_Type(Integer32):
    """Custom type measurementFpNumConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_MeasurementFpNumConnectors_Type.__name__ = "Integer32"
_MeasurementFpNumConnectors_Object = MibTableColumn
measurementFpNumConnectors = _MeasurementFpNumConnectors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 8),
    _MeasurementFpNumConnectors_Type()
)
measurementFpNumConnectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpNumConnectors.setStatus("current")


class _MeasurementFpNumSplices_Type(Integer32):
    """Custom type measurementFpNumSplices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_MeasurementFpNumSplices_Type.__name__ = "Integer32"
_MeasurementFpNumSplices_Object = MibTableColumn
measurementFpNumSplices = _MeasurementFpNumSplices_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 9),
    _MeasurementFpNumSplices_Type()
)
measurementFpNumSplices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpNumSplices.setStatus("current")


class _MeasurementFpMaxLaserPower_Type(Integer32):
    """Custom type measurementFpMaxLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MeasurementFpMaxLaserPower_Type.__name__ = "Integer32"
_MeasurementFpMaxLaserPower_Object = MibTableColumn
measurementFpMaxLaserPower = _MeasurementFpMaxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 10),
    _MeasurementFpMaxLaserPower_Type()
)
measurementFpMaxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpMaxLaserPower.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpMaxLaserPower.setUnits("0.01 dBm")


class _MeasurementFpFastMode_Type(Integer32):
    """Custom type measurementFpFastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MeasurementFpFastMode_Type.__name__ = "Integer32"
_MeasurementFpFastMode_Object = MibTableColumn
measurementFpFastMode = _MeasurementFpFastMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 11),
    _MeasurementFpFastMode_Type()
)
measurementFpFastMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpFastMode.setStatus("current")


class _MeasurementFpMonitoringMode_Type(Integer32):
    """Custom type measurementFpMonitoringMode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("lossCalculation", 1),
          ("trafficCheck", 2),
          ("standard", 3),
          ("highDynamic", 4),
          ("highResolution", 5),
          ("cabinetSensorShort", 6),
          ("cabinetSensorLong", 7),
          ("dpaCustom", 8),
          ("dpaFast", 9),
          ("dpaBalanced", 10),
          ("dpaHighSensitivity", 11))
    )


_MeasurementFpMonitoringMode_Type.__name__ = "Integer32"
_MeasurementFpMonitoringMode_Object = MibTableColumn
measurementFpMonitoringMode = _MeasurementFpMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 12),
    _MeasurementFpMonitoringMode_Type()
)
measurementFpMonitoringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpMonitoringMode.setStatus("current")


class _MeasurementFpTrafficDetected_Type(Integer32):
    """Custom type measurementFpTrafficDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )


_MeasurementFpTrafficDetected_Type.__name__ = "Integer32"
_MeasurementFpTrafficDetected_Object = MibTableColumn
measurementFpTrafficDetected = _MeasurementFpTrafficDetected_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 8, 1, 13),
    _MeasurementFpTrafficDetected_Type()
)
measurementFpTrafficDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpTrafficDetected.setStatus("current")
_MeasurementFaTable_Object = MibTable
measurementFaTable = _MeasurementFaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9)
)
if mibBuilder.loadTexts:
    measurementFaTable.setStatus("current")
_MeasurementFaEntry_Object = MibTableRow
measurementFaEntry = _MeasurementFaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1)
)
measurementFaEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementFaIndex"),
)
if mibBuilder.loadTexts:
    measurementFaEntry.setStatus("current")


class _MeasurementFaIndex_Type(Integer32):
    """Custom type measurementFaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementFaIndex_Type.__name__ = "Integer32"
_MeasurementFaIndex_Object = MibTableColumn
measurementFaIndex = _MeasurementFaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 1),
    _MeasurementFaIndex_Type()
)
measurementFaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementFaIndex.setStatus("current")
_MeasurementFaLinkLoss_Type = Integer32
_MeasurementFaLinkLoss_Object = MibTableColumn
measurementFaLinkLoss = _MeasurementFaLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 2),
    _MeasurementFaLinkLoss_Type()
)
measurementFaLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaLinkLoss.setStatus("current")
if mibBuilder.loadTexts:
    measurementFaLinkLoss.setUnits("0.1 dB")
_MeasurementFaFaultPos_Type = Integer32
_MeasurementFaFaultPos_Object = MibTableColumn
measurementFaFaultPos = _MeasurementFaFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 3),
    _MeasurementFaFaultPos_Type()
)
measurementFaFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    measurementFaFaultPos.setUnits("0.1 m")


class _MeasurementFaDeprecated_Type(Integer32):
    """Custom type measurementFaDeprecated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )


_MeasurementFaDeprecated_Type.__name__ = "Integer32"
_MeasurementFaDeprecated_Object = MibTableColumn
measurementFaDeprecated = _MeasurementFaDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 4),
    _MeasurementFaDeprecated_Type()
)
measurementFaDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaDeprecated.setStatus("current")
_MeasurementFaDataTimestamp_Type = DateAndTime
_MeasurementFaDataTimestamp_Object = MibTableColumn
measurementFaDataTimestamp = _MeasurementFaDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 5),
    _MeasurementFaDataTimestamp_Type()
)
measurementFaDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaDataTimestamp.setStatus("current")
_MeasurementFaCorrectedFaultPos_Type = Integer32
_MeasurementFaCorrectedFaultPos_Object = MibTableColumn
measurementFaCorrectedFaultPos = _MeasurementFaCorrectedFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 6),
    _MeasurementFaCorrectedFaultPos_Type()
)
measurementFaCorrectedFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaCorrectedFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    measurementFaCorrectedFaultPos.setUnits("0.1 m")


class _MeasurementFaFaultPosLatitude_Type(DisplayString):
    """Custom type measurementFaFaultPosLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MeasurementFaFaultPosLatitude_Type.__name__ = "DisplayString"
_MeasurementFaFaultPosLatitude_Object = MibTableColumn
measurementFaFaultPosLatitude = _MeasurementFaFaultPosLatitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 7),
    _MeasurementFaFaultPosLatitude_Type()
)
measurementFaFaultPosLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaFaultPosLatitude.setStatus("current")
if mibBuilder.loadTexts:
    measurementFaFaultPosLatitude.setUnits("deg")


class _MeasurementFaFaultPosLongitude_Type(DisplayString):
    """Custom type measurementFaFaultPosLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MeasurementFaFaultPosLongitude_Type.__name__ = "DisplayString"
_MeasurementFaFaultPosLongitude_Object = MibTableColumn
measurementFaFaultPosLongitude = _MeasurementFaFaultPosLongitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 9, 1, 8),
    _MeasurementFaFaultPosLongitude_Type()
)
measurementFaFaultPosLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFaFaultPosLongitude.setStatus("current")
if mibBuilder.loadTexts:
    measurementFaFaultPosLongitude.setUnits("deg")
_MeasurementOtdrTable_Object = MibTable
measurementOtdrTable = _MeasurementOtdrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10)
)
if mibBuilder.loadTexts:
    measurementOtdrTable.setStatus("current")
_MeasurementOtdrEntry_Object = MibTableRow
measurementOtdrEntry = _MeasurementOtdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1)
)
measurementOtdrEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementOtdrIndex"),
)
if mibBuilder.loadTexts:
    measurementOtdrEntry.setStatus("current")


class _MeasurementOtdrIndex_Type(Integer32):
    """Custom type measurementOtdrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MeasurementOtdrIndex_Type.__name__ = "Integer32"
_MeasurementOtdrIndex_Object = MibTableColumn
measurementOtdrIndex = _MeasurementOtdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 1),
    _MeasurementOtdrIndex_Type()
)
measurementOtdrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementOtdrIndex.setStatus("current")


class _MeasurementOtdrLength_Type(Integer32):
    """Custom type measurementOtdrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200000),
    )


_MeasurementOtdrLength_Type.__name__ = "Integer32"
_MeasurementOtdrLength_Object = MibTableColumn
measurementOtdrLength = _MeasurementOtdrLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 2),
    _MeasurementOtdrLength_Type()
)
measurementOtdrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrLength.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrLength.setUnits("0.1 m")


class _MeasurementOtdrExternalOffset_Type(Integer32):
    """Custom type measurementOtdrExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MeasurementOtdrExternalOffset_Type.__name__ = "Integer32"
_MeasurementOtdrExternalOffset_Object = MibTableColumn
measurementOtdrExternalOffset = _MeasurementOtdrExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 3),
    _MeasurementOtdrExternalOffset_Type()
)
measurementOtdrExternalOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrExternalOffset.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrExternalOffset.setUnits("m")


class _MeasurementOtdrRefractiveIndex_Type(Integer32):
    """Custom type measurementOtdrRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MeasurementOtdrRefractiveIndex_Type.__name__ = "Integer32"
_MeasurementOtdrRefractiveIndex_Object = MibTableColumn
measurementOtdrRefractiveIndex = _MeasurementOtdrRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 4),
    _MeasurementOtdrRefractiveIndex_Type()
)
measurementOtdrRefractiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrRefractiveIndex.setStatus("current")


class _MeasurementOtdrPowerLevel_Type(Integer32):
    """Custom type measurementOtdrPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_MeasurementOtdrPowerLevel_Type.__name__ = "Integer32"
_MeasurementOtdrPowerLevel_Object = MibTableColumn
measurementOtdrPowerLevel = _MeasurementOtdrPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 5),
    _MeasurementOtdrPowerLevel_Type()
)
measurementOtdrPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrPowerLevel.setUnits("0.01 dBm")


class _MeasurementOtdrPulseWidth_Type(Integer32):
    """Custom type measurementOtdrPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20000),
    )


_MeasurementOtdrPulseWidth_Type.__name__ = "Integer32"
_MeasurementOtdrPulseWidth_Object = MibTableColumn
measurementOtdrPulseWidth = _MeasurementOtdrPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 6),
    _MeasurementOtdrPulseWidth_Type()
)
measurementOtdrPulseWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrPulseWidth.setUnits("ns")


class _MeasurementOtdrAverageRate_Type(Integer32):
    """Custom type measurementOtdrAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MeasurementOtdrAverageRate_Type.__name__ = "Integer32"
_MeasurementOtdrAverageRate_Object = MibTableColumn
measurementOtdrAverageRate = _MeasurementOtdrAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 7),
    _MeasurementOtdrAverageRate_Type()
)
measurementOtdrAverageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrAverageRate.setStatus("current")
_MeasurementOtdrDataTimestamp_Type = DateAndTime
_MeasurementOtdrDataTimestamp_Object = MibTableColumn
measurementOtdrDataTimestamp = _MeasurementOtdrDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 8),
    _MeasurementOtdrDataTimestamp_Type()
)
measurementOtdrDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrDataTimestamp.setStatus("current")


class _MeasurementOtdrMaxLaserPower_Type(Integer32):
    """Custom type measurementOtdrMaxLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MeasurementOtdrMaxLaserPower_Type.__name__ = "Integer32"
_MeasurementOtdrMaxLaserPower_Object = MibTableColumn
measurementOtdrMaxLaserPower = _MeasurementOtdrMaxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 9),
    _MeasurementOtdrMaxLaserPower_Type()
)
measurementOtdrMaxLaserPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrMaxLaserPower.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrMaxLaserPower.setUnits("0.01 dBm")


class _MeasurementOtdrLinkLength_Type(Integer32):
    """Custom type measurementOtdrLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200000),
    )


_MeasurementOtdrLinkLength_Type.__name__ = "Integer32"
_MeasurementOtdrLinkLength_Object = MibTableColumn
measurementOtdrLinkLength = _MeasurementOtdrLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 10),
    _MeasurementOtdrLinkLength_Type()
)
measurementOtdrLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrLinkLength.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrLinkLength.setUnits("m")


class _MeasurementOtdrMeasTime_Type(Integer32):
    """Custom type measurementOtdrMeasTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_MeasurementOtdrMeasTime_Type.__name__ = "Integer32"
_MeasurementOtdrMeasTime_Object = MibTableColumn
measurementOtdrMeasTime = _MeasurementOtdrMeasTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 10, 1, 11),
    _MeasurementOtdrMeasTime_Type()
)
measurementOtdrMeasTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementOtdrMeasTime.setStatus("current")
if mibBuilder.loadTexts:
    measurementOtdrMeasTime.setUnits("s")
_MeasurementAutoFaTable_Object = MibTable
measurementAutoFaTable = _MeasurementAutoFaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11)
)
if mibBuilder.loadTexts:
    measurementAutoFaTable.setStatus("current")
_MeasurementAutoFaEntry_Object = MibTableRow
measurementAutoFaEntry = _MeasurementAutoFaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1)
)
measurementAutoFaEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementAutoFaIndex"),
)
if mibBuilder.loadTexts:
    measurementAutoFaEntry.setStatus("current")


class _MeasurementAutoFaIndex_Type(Integer32):
    """Custom type measurementAutoFaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MeasurementAutoFaIndex_Type.__name__ = "Integer32"
_MeasurementAutoFaIndex_Object = MibTableColumn
measurementAutoFaIndex = _MeasurementAutoFaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 1),
    _MeasurementAutoFaIndex_Type()
)
measurementAutoFaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementAutoFaIndex.setStatus("current")
_MeasurementAutoFaReference_Type = Integer32
_MeasurementAutoFaReference_Object = MibTableColumn
measurementAutoFaReference = _MeasurementAutoFaReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 2),
    _MeasurementAutoFaReference_Type()
)
measurementAutoFaReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaReference.setStatus("current")
_MeasurementAutoFaLinkLoss_Type = Integer32
_MeasurementAutoFaLinkLoss_Object = MibTableColumn
measurementAutoFaLinkLoss = _MeasurementAutoFaLinkLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 3),
    _MeasurementAutoFaLinkLoss_Type()
)
measurementAutoFaLinkLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaLinkLoss.setStatus("current")
if mibBuilder.loadTexts:
    measurementAutoFaLinkLoss.setUnits("0.1 dB")
_MeasurementAutoFaFaultPos_Type = Integer32
_MeasurementAutoFaFaultPos_Object = MibTableColumn
measurementAutoFaFaultPos = _MeasurementAutoFaFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 4),
    _MeasurementAutoFaFaultPos_Type()
)
measurementAutoFaFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPos.setUnits("0.1 m")


class _MeasurementAutoFaDeprecated_Type(Integer32):
    """Custom type measurementAutoFaDeprecated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("no", 1),
          ("yes", 2))
    )


_MeasurementAutoFaDeprecated_Type.__name__ = "Integer32"
_MeasurementAutoFaDeprecated_Object = MibTableColumn
measurementAutoFaDeprecated = _MeasurementAutoFaDeprecated_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 5),
    _MeasurementAutoFaDeprecated_Type()
)
measurementAutoFaDeprecated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaDeprecated.setStatus("current")
_MeasurementAutoFaDataTimestamp_Type = DateAndTime
_MeasurementAutoFaDataTimestamp_Object = MibTableColumn
measurementAutoFaDataTimestamp = _MeasurementAutoFaDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 6),
    _MeasurementAutoFaDataTimestamp_Type()
)
measurementAutoFaDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaDataTimestamp.setStatus("current")
_MeasurementAutoFaCorrectedFaultPos_Type = Integer32
_MeasurementAutoFaCorrectedFaultPos_Object = MibTableColumn
measurementAutoFaCorrectedFaultPos = _MeasurementAutoFaCorrectedFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 7),
    _MeasurementAutoFaCorrectedFaultPos_Type()
)
measurementAutoFaCorrectedFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaCorrectedFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    measurementAutoFaCorrectedFaultPos.setUnits("0.1 m")


class _MeasurementAutoFaFaultPosLatitude_Type(DisplayString):
    """Custom type measurementAutoFaFaultPosLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MeasurementAutoFaFaultPosLatitude_Type.__name__ = "DisplayString"
_MeasurementAutoFaFaultPosLatitude_Object = MibTableColumn
measurementAutoFaFaultPosLatitude = _MeasurementAutoFaFaultPosLatitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 8),
    _MeasurementAutoFaFaultPosLatitude_Type()
)
measurementAutoFaFaultPosLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPosLatitude.setStatus("current")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPosLatitude.setUnits("deg")


class _MeasurementAutoFaFaultPosLongitude_Type(DisplayString):
    """Custom type measurementAutoFaFaultPosLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MeasurementAutoFaFaultPosLongitude_Type.__name__ = "DisplayString"
_MeasurementAutoFaFaultPosLongitude_Object = MibTableColumn
measurementAutoFaFaultPosLongitude = _MeasurementAutoFaFaultPosLongitude_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 11, 1, 9),
    _MeasurementAutoFaFaultPosLongitude_Type()
)
measurementAutoFaFaultPosLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPosLongitude.setStatus("current")
if mibBuilder.loadTexts:
    measurementAutoFaFaultPosLongitude.setUnits("deg")
_MonitorPointLossTable_Object = MibTable
monitorPointLossTable = _MonitorPointLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 12)
)
if mibBuilder.loadTexts:
    monitorPointLossTable.setStatus("current")
_MonitorPointLossEntry_Object = MibTableRow
monitorPointLossEntry = _MonitorPointLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 12, 1)
)
monitorPointLossEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "mpId"),
)
if mibBuilder.loadTexts:
    monitorPointLossEntry.setStatus("current")
_MonitorPointLossCurrentLoss_Type = Integer32
_MonitorPointLossCurrentLoss_Object = MibTableColumn
monitorPointLossCurrentLoss = _MonitorPointLossCurrentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 12, 1, 1),
    _MonitorPointLossCurrentLoss_Type()
)
monitorPointLossCurrentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointLossCurrentLoss.setStatus("current")
if mibBuilder.loadTexts:
    monitorPointLossCurrentLoss.setUnits("0.1 dB")
_MonitorPointLossFpLoss_Type = Integer32
_MonitorPointLossFpLoss_Object = MibTableColumn
monitorPointLossFpLoss = _MonitorPointLossFpLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 12, 1, 2),
    _MonitorPointLossFpLoss_Type()
)
monitorPointLossFpLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointLossFpLoss.setStatus("current")
if mibBuilder.loadTexts:
    monitorPointLossFpLoss.setUnits("0.1 dB")
_MonitorPointLossDataTimestamp_Type = DateAndTime
_MonitorPointLossDataTimestamp_Object = MibTableColumn
monitorPointLossDataTimestamp = _MonitorPointLossDataTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 12, 1, 3),
    _MonitorPointLossDataTimestamp_Type()
)
monitorPointLossDataTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPointLossDataTimestamp.setStatus("current")
_HistMonitorPointLoss15MinTable_Object = MibTable
histMonitorPointLoss15MinTable = _HistMonitorPointLoss15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13)
)
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinTable.setStatus("current")
_HistMonitorPointLoss15MinEntry_Object = MibTableRow
histMonitorPointLoss15MinEntry = _HistMonitorPointLoss15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1)
)
histMonitorPointLoss15MinEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "mpId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMonitorPointLoss15MinNumber"),
)
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinEntry.setStatus("current")


class _HistMonitorPointLoss15MinNumber_Type(Integer32):
    """Custom type histMonitorPointLoss15MinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_HistMonitorPointLoss15MinNumber_Type.__name__ = "Integer32"
_HistMonitorPointLoss15MinNumber_Object = MibTableColumn
histMonitorPointLoss15MinNumber = _HistMonitorPointLoss15MinNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 1),
    _HistMonitorPointLoss15MinNumber_Type()
)
histMonitorPointLoss15MinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinNumber.setStatus("current")
_HistMonitorPointLoss15MinLow_Type = Integer32
_HistMonitorPointLoss15MinLow_Object = MibTableColumn
histMonitorPointLoss15MinLow = _HistMonitorPointLoss15MinLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 2),
    _HistMonitorPointLoss15MinLow_Type()
)
histMonitorPointLoss15MinLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinLow.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinLow.setUnits("0.1 dB")
_HistMonitorPointLoss15MinMean_Type = Integer32
_HistMonitorPointLoss15MinMean_Object = MibTableColumn
histMonitorPointLoss15MinMean = _HistMonitorPointLoss15MinMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 3),
    _HistMonitorPointLoss15MinMean_Type()
)
histMonitorPointLoss15MinMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinMean.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinMean.setUnits("0.1 dB")
_HistMonitorPointLoss15MinHigh_Type = Integer32
_HistMonitorPointLoss15MinHigh_Object = MibTableColumn
histMonitorPointLoss15MinHigh = _HistMonitorPointLoss15MinHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 4),
    _HistMonitorPointLoss15MinHigh_Type()
)
histMonitorPointLoss15MinHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinHigh.setUnits("0.1 dB")
_HistMonitorPointLoss15MinValid_Type = TruthValue
_HistMonitorPointLoss15MinValid_Object = MibTableColumn
histMonitorPointLoss15MinValid = _HistMonitorPointLoss15MinValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 5),
    _HistMonitorPointLoss15MinValid_Type()
)
histMonitorPointLoss15MinValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinValid.setStatus("current")
_HistMonitorPointLoss15MinTimeStamp_Type = DateAndTime
_HistMonitorPointLoss15MinTimeStamp_Object = MibTableColumn
histMonitorPointLoss15MinTimeStamp = _HistMonitorPointLoss15MinTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 13, 1, 6),
    _HistMonitorPointLoss15MinTimeStamp_Type()
)
histMonitorPointLoss15MinTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss15MinTimeStamp.setStatus("current")
_HistMonitorPointLoss1DayTable_Object = MibTable
histMonitorPointLoss1DayTable = _HistMonitorPointLoss1DayTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14)
)
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayTable.setStatus("current")
_HistMonitorPointLoss1DayEntry_Object = MibTableRow
histMonitorPointLoss1DayEntry = _HistMonitorPointLoss1DayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1)
)
histMonitorPointLoss1DayEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "mpId"),
    (0, "ADVA-FSP3000ALM-MIB", "histMonitorPointLoss1DayNumber"),
)
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayEntry.setStatus("current")


class _HistMonitorPointLoss1DayNumber_Type(Integer32):
    """Custom type histMonitorPointLoss1DayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HistMonitorPointLoss1DayNumber_Type.__name__ = "Integer32"
_HistMonitorPointLoss1DayNumber_Object = MibTableColumn
histMonitorPointLoss1DayNumber = _HistMonitorPointLoss1DayNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 1),
    _HistMonitorPointLoss1DayNumber_Type()
)
histMonitorPointLoss1DayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayNumber.setStatus("current")
_HistMonitorPointLoss1DayLow_Type = Integer32
_HistMonitorPointLoss1DayLow_Object = MibTableColumn
histMonitorPointLoss1DayLow = _HistMonitorPointLoss1DayLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 2),
    _HistMonitorPointLoss1DayLow_Type()
)
histMonitorPointLoss1DayLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayLow.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayLow.setUnits("0.1 dB")
_HistMonitorPointLoss1DayMean_Type = Integer32
_HistMonitorPointLoss1DayMean_Object = MibTableColumn
histMonitorPointLoss1DayMean = _HistMonitorPointLoss1DayMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 3),
    _HistMonitorPointLoss1DayMean_Type()
)
histMonitorPointLoss1DayMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayMean.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayMean.setUnits("0.1 dB")
_HistMonitorPointLoss1DayHigh_Type = Integer32
_HistMonitorPointLoss1DayHigh_Object = MibTableColumn
histMonitorPointLoss1DayHigh = _HistMonitorPointLoss1DayHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 4),
    _HistMonitorPointLoss1DayHigh_Type()
)
histMonitorPointLoss1DayHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayHigh.setStatus("current")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayHigh.setUnits("0.1 dB")
_HistMonitorPointLoss1DayValid_Type = TruthValue
_HistMonitorPointLoss1DayValid_Object = MibTableColumn
histMonitorPointLoss1DayValid = _HistMonitorPointLoss1DayValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 5),
    _HistMonitorPointLoss1DayValid_Type()
)
histMonitorPointLoss1DayValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayValid.setStatus("current")
_HistMonitorPointLoss1DayTimeStamp_Type = DateAndTime
_HistMonitorPointLoss1DayTimeStamp_Object = MibTableColumn
histMonitorPointLoss1DayTimeStamp = _HistMonitorPointLoss1DayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 14, 1, 6),
    _HistMonitorPointLoss1DayTimeStamp_Type()
)
histMonitorPointLoss1DayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMonitorPointLoss1DayTimeStamp.setStatus("current")
_MeasurementFpEventTable_Object = MibTable
measurementFpEventTable = _MeasurementFpEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15)
)
if mibBuilder.loadTexts:
    measurementFpEventTable.setStatus("current")
_MeasurementFpEventEntry_Object = MibTableRow
measurementFpEventEntry = _MeasurementFpEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1)
)
measurementFpEventEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "measurementFpEventId"),
)
if mibBuilder.loadTexts:
    measurementFpEventEntry.setStatus("current")


class _MeasurementFpEventId_Type(Integer32):
    """Custom type measurementFpEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MeasurementFpEventId_Type.__name__ = "Integer32"
_MeasurementFpEventId_Object = MibTableColumn
measurementFpEventId = _MeasurementFpEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1, 1),
    _MeasurementFpEventId_Type()
)
measurementFpEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measurementFpEventId.setStatus("current")
_MeasurementFpEventPosition_Type = Integer32
_MeasurementFpEventPosition_Object = MibTableColumn
measurementFpEventPosition = _MeasurementFpEventPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1, 2),
    _MeasurementFpEventPosition_Type()
)
measurementFpEventPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpEventPosition.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpEventPosition.setUnits("0.1 m")
_MeasurementFpEventReflectance_Type = Integer32
_MeasurementFpEventReflectance_Object = MibTableColumn
measurementFpEventReflectance = _MeasurementFpEventReflectance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1, 3),
    _MeasurementFpEventReflectance_Type()
)
measurementFpEventReflectance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpEventReflectance.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpEventReflectance.setUnits("0.1 dB")
_MeasurementFpEventAttenuation_Type = Integer32
_MeasurementFpEventAttenuation_Object = MibTableColumn
measurementFpEventAttenuation = _MeasurementFpEventAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1, 4),
    _MeasurementFpEventAttenuation_Type()
)
measurementFpEventAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measurementFpEventAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    measurementFpEventAttenuation.setUnits("0.1 dB")


class _MeasurementFpEventRemark_Type(DisplayString):
    """Custom type measurementFpEventRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MeasurementFpEventRemark_Type.__name__ = "DisplayString"
_MeasurementFpEventRemark_Object = MibTableColumn
measurementFpEventRemark = _MeasurementFpEventRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 15, 1, 5),
    _MeasurementFpEventRemark_Type()
)
measurementFpEventRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measurementFpEventRemark.setStatus("current")
_CustomizedFpEventTable_Object = MibTable
customizedFpEventTable = _CustomizedFpEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16)
)
if mibBuilder.loadTexts:
    customizedFpEventTable.setStatus("current")
_CustomizedFpEventEntry_Object = MibTableRow
customizedFpEventEntry = _CustomizedFpEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1)
)
customizedFpEventEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "customizedFpEventId"),
)
if mibBuilder.loadTexts:
    customizedFpEventEntry.setStatus("current")


class _CustomizedFpEventId_Type(Integer32):
    """Custom type customizedFpEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CustomizedFpEventId_Type.__name__ = "Integer32"
_CustomizedFpEventId_Object = MibTableColumn
customizedFpEventId = _CustomizedFpEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 1),
    _CustomizedFpEventId_Type()
)
customizedFpEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    customizedFpEventId.setStatus("current")
_CustomizedFpEventRowStatus_Type = RowStatus
_CustomizedFpEventRowStatus_Object = MibTableColumn
customizedFpEventRowStatus = _CustomizedFpEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 2),
    _CustomizedFpEventRowStatus_Type()
)
customizedFpEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customizedFpEventRowStatus.setStatus("current")
_CustomizedFpEventCorrectedPosition_Type = Integer32
_CustomizedFpEventCorrectedPosition_Object = MibTableColumn
customizedFpEventCorrectedPosition = _CustomizedFpEventCorrectedPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 3),
    _CustomizedFpEventCorrectedPosition_Type()
)
customizedFpEventCorrectedPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customizedFpEventCorrectedPosition.setStatus("current")
if mibBuilder.loadTexts:
    customizedFpEventCorrectedPosition.setUnits("0.1 m")
_CustomizedFpEventRemark_Type = SnmpAdminString
_CustomizedFpEventRemark_Object = MibTableColumn
customizedFpEventRemark = _CustomizedFpEventRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 4),
    _CustomizedFpEventRemark_Type()
)
customizedFpEventRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customizedFpEventRemark.setStatus("current")
_CustomizedFpEventOtdrId_Type = Integer32
_CustomizedFpEventOtdrId_Object = MibTableColumn
customizedFpEventOtdrId = _CustomizedFpEventOtdrId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 5),
    _CustomizedFpEventOtdrId_Type()
)
customizedFpEventOtdrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customizedFpEventOtdrId.setStatus("current")
_CustomizedFpEventOtdrPosition_Type = Integer32
_CustomizedFpEventOtdrPosition_Object = MibTableColumn
customizedFpEventOtdrPosition = _CustomizedFpEventOtdrPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 6),
    _CustomizedFpEventOtdrPosition_Type()
)
customizedFpEventOtdrPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customizedFpEventOtdrPosition.setStatus("current")
if mibBuilder.loadTexts:
    customizedFpEventOtdrPosition.setUnits("0.1 m")
_CustomizedFpEventLayoutId_Type = Integer32
_CustomizedFpEventLayoutId_Object = MibTableColumn
customizedFpEventLayoutId = _CustomizedFpEventLayoutId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 16, 1, 7),
    _CustomizedFpEventLayoutId_Type()
)
customizedFpEventLayoutId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customizedFpEventLayoutId.setStatus("current")
_MergedFpEventTable_Object = MibTable
mergedFpEventTable = _MergedFpEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17)
)
if mibBuilder.loadTexts:
    mergedFpEventTable.setStatus("current")
_MergedFpEventEntry_Object = MibTableRow
mergedFpEventEntry = _MergedFpEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1)
)
mergedFpEventEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "mergedFpEventId"),
)
if mibBuilder.loadTexts:
    mergedFpEventEntry.setStatus("current")


class _MergedFpEventId_Type(Integer32):
    """Custom type mergedFpEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_MergedFpEventId_Type.__name__ = "Integer32"
_MergedFpEventId_Object = MibTableColumn
mergedFpEventId = _MergedFpEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 1),
    _MergedFpEventId_Type()
)
mergedFpEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mergedFpEventId.setStatus("current")
_MergedFpEventCustomizedEventId_Type = Integer32
_MergedFpEventCustomizedEventId_Object = MibTableColumn
mergedFpEventCustomizedEventId = _MergedFpEventCustomizedEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 2),
    _MergedFpEventCustomizedEventId_Type()
)
mergedFpEventCustomizedEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mergedFpEventCustomizedEventId.setStatus("current")
_MergedFpEventOtdrId_Type = Integer32
_MergedFpEventOtdrId_Object = MibTableColumn
mergedFpEventOtdrId = _MergedFpEventOtdrId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 3),
    _MergedFpEventOtdrId_Type()
)
mergedFpEventOtdrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mergedFpEventOtdrId.setStatus("current")
_MergedFpEventCorrectedPosition_Type = Integer32
_MergedFpEventCorrectedPosition_Object = MibTableColumn
mergedFpEventCorrectedPosition = _MergedFpEventCorrectedPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 4),
    _MergedFpEventCorrectedPosition_Type()
)
mergedFpEventCorrectedPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mergedFpEventCorrectedPosition.setStatus("current")
if mibBuilder.loadTexts:
    mergedFpEventCorrectedPosition.setUnits("0.1 m")
_MergedFpEventOtdrPosition_Type = Integer32
_MergedFpEventOtdrPosition_Object = MibTableColumn
mergedFpEventOtdrPosition = _MergedFpEventOtdrPosition_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 5),
    _MergedFpEventOtdrPosition_Type()
)
mergedFpEventOtdrPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mergedFpEventOtdrPosition.setStatus("current")
if mibBuilder.loadTexts:
    mergedFpEventOtdrPosition.setUnits("0.1 m")
_MergedFpEventRemark_Type = SnmpAdminString
_MergedFpEventRemark_Object = MibTableColumn
mergedFpEventRemark = _MergedFpEventRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 17, 1, 6),
    _MergedFpEventRemark_Type()
)
mergedFpEventRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mergedFpEventRemark.setStatus("current")
_LinkLayoutEventTable_Object = MibTable
linkLayoutEventTable = _LinkLayoutEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18)
)
if mibBuilder.loadTexts:
    linkLayoutEventTable.setStatus("current")
_LinkLayoutEventEntry_Object = MibTableRow
linkLayoutEventEntry = _LinkLayoutEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1)
)
linkLayoutEventEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "linkLayoutEventId"),
)
if mibBuilder.loadTexts:
    linkLayoutEventEntry.setStatus("current")


class _LinkLayoutEventId_Type(Integer32):
    """Custom type linkLayoutEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LinkLayoutEventId_Type.__name__ = "Integer32"
_LinkLayoutEventId_Object = MibTableColumn
linkLayoutEventId = _LinkLayoutEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 1),
    _LinkLayoutEventId_Type()
)
linkLayoutEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    linkLayoutEventId.setStatus("current")
_LinkLayoutEventRowStatus_Type = RowStatus
_LinkLayoutEventRowStatus_Object = MibTableColumn
linkLayoutEventRowStatus = _LinkLayoutEventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 2),
    _LinkLayoutEventRowStatus_Type()
)
linkLayoutEventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkLayoutEventRowStatus.setStatus("current")
_LinkLayoutEventMpId_Type = Integer32
_LinkLayoutEventMpId_Object = MibTableColumn
linkLayoutEventMpId = _LinkLayoutEventMpId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 3),
    _LinkLayoutEventMpId_Type()
)
linkLayoutEventMpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkLayoutEventMpId.setStatus("current")
_LinkLayoutEventFpEventId_Type = Integer32
_LinkLayoutEventFpEventId_Object = MibTableColumn
linkLayoutEventFpEventId = _LinkLayoutEventFpEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 4),
    _LinkLayoutEventFpEventId_Type()
)
linkLayoutEventFpEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkLayoutEventFpEventId.setStatus("current")
_LinkLayoutEventCustomizedEventId_Type = Integer32
_LinkLayoutEventCustomizedEventId_Object = MibTableColumn
linkLayoutEventCustomizedEventId = _LinkLayoutEventCustomizedEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 5),
    _LinkLayoutEventCustomizedEventId_Type()
)
linkLayoutEventCustomizedEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    linkLayoutEventCustomizedEventId.setStatus("current")
_LinkLayoutEventFaultPos_Type = Integer32
_LinkLayoutEventFaultPos_Object = MibTableColumn
linkLayoutEventFaultPos = _LinkLayoutEventFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 6),
    _LinkLayoutEventFaultPos_Type()
)
linkLayoutEventFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLayoutEventFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    linkLayoutEventFaultPos.setUnits("0.1 m")
_LinkLayoutEventCorrectedFaultPos_Type = Integer32
_LinkLayoutEventCorrectedFaultPos_Object = MibTableColumn
linkLayoutEventCorrectedFaultPos = _LinkLayoutEventCorrectedFaultPos_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 18, 1, 7),
    _LinkLayoutEventCorrectedFaultPos_Type()
)
linkLayoutEventCorrectedFaultPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLayoutEventCorrectedFaultPos.setStatus("current")
if mibBuilder.loadTexts:
    linkLayoutEventCorrectedFaultPos.setUnits("0.1 m")
_SegmentTable_Object = MibTable
segmentTable = _SegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19)
)
if mibBuilder.loadTexts:
    segmentTable.setStatus("current")
_SegmentEntry_Object = MibTableRow
segmentEntry = _SegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1)
)
segmentEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "segmentId"),
)
if mibBuilder.loadTexts:
    segmentEntry.setStatus("current")


class _SegmentId_Type(Integer32):
    """Custom type segmentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SegmentId_Type.__name__ = "Integer32"
_SegmentId_Object = MibTableColumn
segmentId = _SegmentId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 1),
    _SegmentId_Type()
)
segmentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    segmentId.setStatus("current")
_SegmentRowStatus_Type = RowStatus
_SegmentRowStatus_Object = MibTableColumn
segmentRowStatus = _SegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 2),
    _SegmentRowStatus_Type()
)
segmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentRowStatus.setStatus("current")
_SegmentStartEventId_Type = Integer32
_SegmentStartEventId_Object = MibTableColumn
segmentStartEventId = _SegmentStartEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 3),
    _SegmentStartEventId_Type()
)
segmentStartEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentStartEventId.setStatus("current")
_SegmentStopEventId_Type = Integer32
_SegmentStopEventId_Object = MibTableColumn
segmentStopEventId = _SegmentStopEventId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 4),
    _SegmentStopEventId_Type()
)
segmentStopEventId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentStopEventId.setStatus("current")
_SegmentStartCorrection_Type = Integer32
_SegmentStartCorrection_Object = MibTableColumn
segmentStartCorrection = _SegmentStartCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 5),
    _SegmentStartCorrection_Type()
)
segmentStartCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentStartCorrection.setStatus("current")
if mibBuilder.loadTexts:
    segmentStartCorrection.setUnits("0.1 m")
_SegmentStopCorrection_Type = Integer32
_SegmentStopCorrection_Object = MibTableColumn
segmentStopCorrection = _SegmentStopCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 6),
    _SegmentStopCorrection_Type()
)
segmentStopCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentStopCorrection.setStatus("current")
if mibBuilder.loadTexts:
    segmentStopCorrection.setUnits("0.1 m")
_SegmentRemark_Type = SnmpAdminString
_SegmentRemark_Object = MibTableColumn
segmentRemark = _SegmentRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 7),
    _SegmentRemark_Type()
)
segmentRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    segmentRemark.setStatus("current")
_SegmentFpLength_Type = Integer32
_SegmentFpLength_Object = MibTableColumn
segmentFpLength = _SegmentFpLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 8),
    _SegmentFpLength_Type()
)
segmentFpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentFpLength.setStatus("current")
if mibBuilder.loadTexts:
    segmentFpLength.setUnits("0.1 m")
_SegmentFpLoss_Type = Integer32
_SegmentFpLoss_Object = MibTableColumn
segmentFpLoss = _SegmentFpLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 9),
    _SegmentFpLoss_Type()
)
segmentFpLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentFpLoss.setStatus("current")
if mibBuilder.loadTexts:
    segmentFpLoss.setUnits("0.1 dB")
_SegmentFpLossPerKm_Type = Integer32
_SegmentFpLossPerKm_Object = MibTableColumn
segmentFpLossPerKm = _SegmentFpLossPerKm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 19, 1, 10),
    _SegmentFpLossPerKm_Type()
)
segmentFpLossPerKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentFpLossPerKm.setStatus("current")
if mibBuilder.loadTexts:
    segmentFpLossPerKm.setUnits("0.01 dB")
_HistSegmentTable_Object = MibTable
histSegmentTable = _HistSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20)
)
if mibBuilder.loadTexts:
    histSegmentTable.setStatus("current")
_HistSegmentEntry_Object = MibTableRow
histSegmentEntry = _HistSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1)
)
histSegmentEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
    (0, "ADVA-FSP3000ALM-MIB", "segmentId"),
    (0, "ADVA-FSP3000ALM-MIB", "histSegmentNumber"),
)
if mibBuilder.loadTexts:
    histSegmentEntry.setStatus("current")


class _HistSegmentNumber_Type(Integer32):
    """Custom type histSegmentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HistSegmentNumber_Type.__name__ = "Integer32"
_HistSegmentNumber_Object = MibTableColumn
histSegmentNumber = _HistSegmentNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 1),
    _HistSegmentNumber_Type()
)
histSegmentNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    histSegmentNumber.setStatus("current")
_HistSegmentLength_Type = Integer32
_HistSegmentLength_Object = MibTableColumn
histSegmentLength = _HistSegmentLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 2),
    _HistSegmentLength_Type()
)
histSegmentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histSegmentLength.setStatus("current")
if mibBuilder.loadTexts:
    histSegmentLength.setUnits("0.1 m")
_HistSegmentLoss_Type = Integer32
_HistSegmentLoss_Object = MibTableColumn
histSegmentLoss = _HistSegmentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 3),
    _HistSegmentLoss_Type()
)
histSegmentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histSegmentLoss.setStatus("current")
if mibBuilder.loadTexts:
    histSegmentLoss.setUnits("0.1 dB")
_HistSegmentLossPerKm_Type = Integer32
_HistSegmentLossPerKm_Object = MibTableColumn
histSegmentLossPerKm = _HistSegmentLossPerKm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 4),
    _HistSegmentLossPerKm_Type()
)
histSegmentLossPerKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histSegmentLossPerKm.setStatus("current")
if mibBuilder.loadTexts:
    histSegmentLossPerKm.setUnits("0.01 dB")
_HistSegmentUncertain_Type = TruthValue
_HistSegmentUncertain_Object = MibTableColumn
histSegmentUncertain = _HistSegmentUncertain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 5),
    _HistSegmentUncertain_Type()
)
histSegmentUncertain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histSegmentUncertain.setStatus("current")
_HistSegmentTimeStamp_Type = DateAndTime
_HistSegmentTimeStamp_Object = MibTableColumn
histSegmentTimeStamp = _HistSegmentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 20, 1, 6),
    _HistSegmentTimeStamp_Type()
)
histSegmentTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histSegmentTimeStamp.setStatus("current")
_InternalChannelLossTable_Object = MibTable
internalChannelLossTable = _InternalChannelLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 21)
)
if mibBuilder.loadTexts:
    internalChannelLossTable.setStatus("current")
_InternalChannelLossEntry_Object = MibTableRow
internalChannelLossEntry = _InternalChannelLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 21, 1)
)
internalChannelLossEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    internalChannelLossEntry.setStatus("current")


class _InternalChannelLossValue_Type(Integer32):
    """Custom type internalChannelLossValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 420),
    )


_InternalChannelLossValue_Type.__name__ = "Integer32"
_InternalChannelLossValue_Object = MibTableColumn
internalChannelLossValue = _InternalChannelLossValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 21, 1, 1),
    _InternalChannelLossValue_Type()
)
internalChannelLossValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChannelLossValue.setStatus("current")
if mibBuilder.loadTexts:
    internalChannelLossValue.setUnits("0.1 dB")
_InternalChannelLossTimeStamp_Type = DateAndTime
_InternalChannelLossTimeStamp_Object = MibTableColumn
internalChannelLossTimeStamp = _InternalChannelLossTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 3, 21, 1, 2),
    _InternalChannelLossTimeStamp_Type()
)
internalChannelLossTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChannelLossTimeStamp.setStatus("current")
_EventLogs_ObjectIdentity = ObjectIdentity
eventLogs = _EventLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4)
)
_EventsLogged_Type = Unsigned32
_EventsLogged_Object = MibScalar
eventsLogged = _EventsLogged_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 1),
    _EventsLogged_Type()
)
eventsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventsLogged.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1)
)
eventLogEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventLogIndex_Type = Unsigned32
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("current")
_EventLogTimeStamp_Type = DateAndTime
_EventLogTimeStamp_Object = MibTableColumn
eventLogTimeStamp = _EventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 2),
    _EventLogTimeStamp_Type()
)
eventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTimeStamp.setStatus("current")
_EventLogNotificationOID_Type = ObjectIdentifier
_EventLogNotificationOID_Object = MibTableColumn
eventLogNotificationOID = _EventLogNotificationOID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 3),
    _EventLogNotificationOID_Type()
)
eventLogNotificationOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogNotificationOID.setStatus("current")
_EventLogIdentityTranslation_Type = IdentityTranslation
_EventLogIdentityTranslation_Object = MibTableColumn
eventLogIdentityTranslation = _EventLogIdentityTranslation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 2, 1, 4),
    _EventLogIdentityTranslation_Type()
)
eventLogIdentityTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIdentityTranslation.setStatus("current")
_EventLogVarTable_Object = MibTable
eventLogVarTable = _EventLogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3)
)
if mibBuilder.loadTexts:
    eventLogVarTable.setStatus("current")
_EventLogVarEntry_Object = MibTableRow
eventLogVarEntry = _EventLogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1)
)
eventLogVarEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "eventLogIndex"),
    (0, "ADVA-FSP3000ALM-MIB", "eventLogVarIndex"),
)
if mibBuilder.loadTexts:
    eventLogVarEntry.setStatus("current")
_EventLogVarIndex_Type = Unsigned32
_EventLogVarIndex_Object = MibTableColumn
eventLogVarIndex = _EventLogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 1),
    _EventLogVarIndex_Type()
)
eventLogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventLogVarIndex.setStatus("current")
_EventLogVarId_Type = ObjectIdentifier
_EventLogVarId_Object = MibTableColumn
eventLogVarId = _EventLogVarId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 2),
    _EventLogVarId_Type()
)
eventLogVarId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarId.setStatus("current")


class _EventLogVarType_Type(Integer32):
    """Custom type eventLogVarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("integer32", 1),
          ("ipAddress", 2),
          ("octetString", 3),
          ("objectId", 4),
          ("counter64", 5),
          ("unsigned32", 7))
    )


_EventLogVarType_Type.__name__ = "Integer32"
_EventLogVarType_Object = MibTableColumn
eventLogVarType = _EventLogVarType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 3),
    _EventLogVarType_Type()
)
eventLogVarType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarType.setStatus("current")
_EventLogVarInteger32Val_Type = Integer32
_EventLogVarInteger32Val_Object = MibTableColumn
eventLogVarInteger32Val = _EventLogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 4),
    _EventLogVarInteger32Val_Type()
)
eventLogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarInteger32Val.setStatus("current")
_EventLogVarIpAddressVal_Type = IpAddress
_EventLogVarIpAddressVal_Object = MibTableColumn
eventLogVarIpAddressVal = _EventLogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 5),
    _EventLogVarIpAddressVal_Type()
)
eventLogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarIpAddressVal.setStatus("current")


class _EventLogVarOctetStringVal_Type(OctetString):
    """Custom type eventLogVarOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventLogVarOctetStringVal_Type.__name__ = "OctetString"
_EventLogVarOctetStringVal_Object = MibTableColumn
eventLogVarOctetStringVal = _EventLogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 6),
    _EventLogVarOctetStringVal_Type()
)
eventLogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarOctetStringVal.setStatus("current")
_EventLogVarOidVal_Type = ObjectIdentifier
_EventLogVarOidVal_Object = MibTableColumn
eventLogVarOidVal = _EventLogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 7),
    _EventLogVarOidVal_Type()
)
eventLogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarOidVal.setStatus("current")
_EventLogVarCounter64Val_Type = Counter64
_EventLogVarCounter64Val_Object = MibTableColumn
eventLogVarCounter64Val = _EventLogVarCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 8),
    _EventLogVarCounter64Val_Type()
)
eventLogVarCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarCounter64Val.setStatus("current")
_EventLogVarUnsigned32Val_Type = Unsigned32
_EventLogVarUnsigned32Val_Object = MibTableColumn
eventLogVarUnsigned32Val = _EventLogVarUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 3, 1, 10),
    _EventLogVarUnsigned32Val_Type()
)
eventLogVarUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogVarUnsigned32Val.setStatus("current")
_TrapsinkTable_Object = MibTable
trapsinkTable = _TrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4)
)
if mibBuilder.loadTexts:
    trapsinkTable.setStatus("current")
_TrapsinkEntry_Object = MibTableRow
trapsinkEntry = _TrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1)
)
trapsinkEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "trapsinkAddress"),
    (0, "ADVA-FSP3000ALM-MIB", "trapsinkPort"),
)
if mibBuilder.loadTexts:
    trapsinkEntry.setStatus("current")
_TrapsinkAddress_Type = IpAddress
_TrapsinkAddress_Object = MibTableColumn
trapsinkAddress = _TrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 1),
    _TrapsinkAddress_Type()
)
trapsinkAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapsinkAddress.setStatus("current")


class _TrapsinkPort_Type(Integer32):
    """Custom type trapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsinkPort_Type.__name__ = "Integer32"
_TrapsinkPort_Object = MibTableColumn
trapsinkPort = _TrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 2),
    _TrapsinkPort_Type()
)
trapsinkPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapsinkPort.setStatus("current")


class _TrapsinkCommunity_Type(DisplayString):
    """Custom type trapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TrapsinkCommunity_Type.__name__ = "DisplayString"
_TrapsinkCommunity_Object = MibTableColumn
trapsinkCommunity = _TrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 3),
    _TrapsinkCommunity_Type()
)
trapsinkCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkCommunity.setStatus("current")
_TrapsinkRowStatus_Type = RowStatus
_TrapsinkRowStatus_Object = MibTableColumn
trapsinkRowStatus = _TrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 4),
    _TrapsinkRowStatus_Type()
)
trapsinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkRowStatus.setStatus("current")


class _TrapsinkVersion_Type(Integer32):
    """Custom type trapsinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_TrapsinkVersion_Type.__name__ = "Integer32"
_TrapsinkVersion_Object = MibTableColumn
trapsinkVersion = _TrapsinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 5),
    _TrapsinkVersion_Type()
)
trapsinkVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkVersion.setStatus("current")


class _TrapsinkUserName_Type(DisplayString):
    """Custom type trapsinkUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapsinkUserName_Type.__name__ = "DisplayString"
_TrapsinkUserName_Object = MibTableColumn
trapsinkUserName = _TrapsinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 6),
    _TrapsinkUserName_Type()
)
trapsinkUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkUserName.setStatus("current")


class _TrapsinkRemark_Type(OctetString):
    """Custom type trapsinkRemark based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_TrapsinkRemark_Type.__name__ = "OctetString"
_TrapsinkRemark_Object = MibTableColumn
trapsinkRemark = _TrapsinkRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 7),
    _TrapsinkRemark_Type()
)
trapsinkRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkRemark.setStatus("current")


class _TrapsinkLifetime_Type(Integer32):
    """Custom type trapsinkLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("duration1hour", 1),
          ("duration1day", 2),
          ("duration3days", 3),
          ("duration1week", 4),
          ("duration1month", 5),
          ("unlimited", 6))
    )


_TrapsinkLifetime_Type.__name__ = "Integer32"
_TrapsinkLifetime_Object = MibTableColumn
trapsinkLifetime = _TrapsinkLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 4, 1, 8),
    _TrapsinkLifetime_Type()
)
trapsinkLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsinkLifetime.setStatus("current")
_Ipv6TrapsinkTable_Object = MibTable
ipv6TrapsinkTable = _Ipv6TrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5)
)
if mibBuilder.loadTexts:
    ipv6TrapsinkTable.setStatus("current")
_Ipv6TrapsinkEntry_Object = MibTableRow
ipv6TrapsinkEntry = _Ipv6TrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1)
)
ipv6TrapsinkEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "ipv6TrapsinkId"),
)
if mibBuilder.loadTexts:
    ipv6TrapsinkEntry.setStatus("current")


class _Ipv6TrapsinkId_Type(Integer32):
    """Custom type ipv6TrapsinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Ipv6TrapsinkId_Type.__name__ = "Integer32"
_Ipv6TrapsinkId_Object = MibTableColumn
ipv6TrapsinkId = _Ipv6TrapsinkId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 1),
    _Ipv6TrapsinkId_Type()
)
ipv6TrapsinkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ipv6TrapsinkId.setStatus("current")
_Ipv6TrapsinkAddress_Type = DisplayString
_Ipv6TrapsinkAddress_Object = MibTableColumn
ipv6TrapsinkAddress = _Ipv6TrapsinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 2),
    _Ipv6TrapsinkAddress_Type()
)
ipv6TrapsinkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkAddress.setStatus("current")


class _Ipv6TrapsinkPort_Type(Integer32):
    """Custom type ipv6TrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6TrapsinkPort_Type.__name__ = "Integer32"
_Ipv6TrapsinkPort_Object = MibTableColumn
ipv6TrapsinkPort = _Ipv6TrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 3),
    _Ipv6TrapsinkPort_Type()
)
ipv6TrapsinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkPort.setStatus("current")


class _Ipv6TrapsinkCommunity_Type(DisplayString):
    """Custom type ipv6TrapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Ipv6TrapsinkCommunity_Type.__name__ = "DisplayString"
_Ipv6TrapsinkCommunity_Object = MibTableColumn
ipv6TrapsinkCommunity = _Ipv6TrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 4),
    _Ipv6TrapsinkCommunity_Type()
)
ipv6TrapsinkCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkCommunity.setStatus("current")
_Ipv6TrapsinkRowStatus_Type = RowStatus
_Ipv6TrapsinkRowStatus_Object = MibTableColumn
ipv6TrapsinkRowStatus = _Ipv6TrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 5),
    _Ipv6TrapsinkRowStatus_Type()
)
ipv6TrapsinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkRowStatus.setStatus("current")


class _Ipv6TrapsinkVersion_Type(Integer32):
    """Custom type ipv6TrapsinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_Ipv6TrapsinkVersion_Type.__name__ = "Integer32"
_Ipv6TrapsinkVersion_Object = MibTableColumn
ipv6TrapsinkVersion = _Ipv6TrapsinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 6),
    _Ipv6TrapsinkVersion_Type()
)
ipv6TrapsinkVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkVersion.setStatus("current")


class _Ipv6TrapsinkUserName_Type(DisplayString):
    """Custom type ipv6TrapsinkUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ipv6TrapsinkUserName_Type.__name__ = "DisplayString"
_Ipv6TrapsinkUserName_Object = MibTableColumn
ipv6TrapsinkUserName = _Ipv6TrapsinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 7),
    _Ipv6TrapsinkUserName_Type()
)
ipv6TrapsinkUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkUserName.setStatus("current")


class _Ipv6TrapsinkRemark_Type(OctetString):
    """Custom type ipv6TrapsinkRemark based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_Ipv6TrapsinkRemark_Type.__name__ = "OctetString"
_Ipv6TrapsinkRemark_Object = MibTableColumn
ipv6TrapsinkRemark = _Ipv6TrapsinkRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 8),
    _Ipv6TrapsinkRemark_Type()
)
ipv6TrapsinkRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkRemark.setStatus("current")


class _Ipv6TrapsinkLifetime_Type(Integer32):
    """Custom type ipv6TrapsinkLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("duration1hour", 1),
          ("duration1day", 2),
          ("duration3days", 3),
          ("duration1week", 4),
          ("duration1month", 5),
          ("unlimited", 6))
    )


_Ipv6TrapsinkLifetime_Type.__name__ = "Integer32"
_Ipv6TrapsinkLifetime_Object = MibTableColumn
ipv6TrapsinkLifetime = _Ipv6TrapsinkLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 5, 1, 9),
    _Ipv6TrapsinkLifetime_Type()
)
ipv6TrapsinkLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6TrapsinkLifetime.setStatus("current")
_SysLogRecipients_ObjectIdentity = ObjectIdentity
sysLogRecipients = _SysLogRecipients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 6)
)


class _SysLogRecipient1Address_Type(DisplayString):
    """Custom type sysLogRecipient1Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_SysLogRecipient1Address_Type.__name__ = "DisplayString"
_SysLogRecipient1Address_Object = MibScalar
sysLogRecipient1Address = _SysLogRecipient1Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 6, 1),
    _SysLogRecipient1Address_Type()
)
sysLogRecipient1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRecipient1Address.setStatus("current")


class _SysLogRecipient2Address_Type(DisplayString):
    """Custom type sysLogRecipient2Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_SysLogRecipient2Address_Type.__name__ = "DisplayString"
_SysLogRecipient2Address_Object = MibScalar
sysLogRecipient2Address = _SysLogRecipient2Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 6, 2),
    _SysLogRecipient2Address_Type()
)
sysLogRecipient2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRecipient2Address.setStatus("current")


class _SysLogRecipient3Address_Type(DisplayString):
    """Custom type sysLogRecipient3Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_SysLogRecipient3Address_Type.__name__ = "DisplayString"
_SysLogRecipient3Address_Object = MibScalar
sysLogRecipient3Address = _SysLogRecipient3Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 6, 3),
    _SysLogRecipient3Address_Type()
)
sysLogRecipient3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogRecipient3Address.setStatus("current")
_DnsTrapsinkTable_Object = MibTable
dnsTrapsinkTable = _DnsTrapsinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7)
)
if mibBuilder.loadTexts:
    dnsTrapsinkTable.setStatus("current")
_DnsTrapsinkEntry_Object = MibTableRow
dnsTrapsinkEntry = _DnsTrapsinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1)
)
dnsTrapsinkEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "dnsTrapsinkId"),
)
if mibBuilder.loadTexts:
    dnsTrapsinkEntry.setStatus("current")


class _DnsTrapsinkId_Type(Integer32):
    """Custom type dnsTrapsinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DnsTrapsinkId_Type.__name__ = "Integer32"
_DnsTrapsinkId_Object = MibTableColumn
dnsTrapsinkId = _DnsTrapsinkId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 1),
    _DnsTrapsinkId_Type()
)
dnsTrapsinkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dnsTrapsinkId.setStatus("current")
_DnsTrapsinkHostName_Type = DisplayString
_DnsTrapsinkHostName_Object = MibTableColumn
dnsTrapsinkHostName = _DnsTrapsinkHostName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 2),
    _DnsTrapsinkHostName_Type()
)
dnsTrapsinkHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkHostName.setStatus("current")


class _DnsTrapsinkPort_Type(Integer32):
    """Custom type dnsTrapsinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DnsTrapsinkPort_Type.__name__ = "Integer32"
_DnsTrapsinkPort_Object = MibTableColumn
dnsTrapsinkPort = _DnsTrapsinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 3),
    _DnsTrapsinkPort_Type()
)
dnsTrapsinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkPort.setStatus("current")


class _DnsTrapsinkCommunity_Type(DisplayString):
    """Custom type dnsTrapsinkCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DnsTrapsinkCommunity_Type.__name__ = "DisplayString"
_DnsTrapsinkCommunity_Object = MibTableColumn
dnsTrapsinkCommunity = _DnsTrapsinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 4),
    _DnsTrapsinkCommunity_Type()
)
dnsTrapsinkCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkCommunity.setStatus("current")
_DnsTrapsinkRowStatus_Type = RowStatus
_DnsTrapsinkRowStatus_Object = MibTableColumn
dnsTrapsinkRowStatus = _DnsTrapsinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 5),
    _DnsTrapsinkRowStatus_Type()
)
dnsTrapsinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkRowStatus.setStatus("current")


class _DnsTrapsinkVersion_Type(Integer32):
    """Custom type dnsTrapsinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_DnsTrapsinkVersion_Type.__name__ = "Integer32"
_DnsTrapsinkVersion_Object = MibTableColumn
dnsTrapsinkVersion = _DnsTrapsinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 6),
    _DnsTrapsinkVersion_Type()
)
dnsTrapsinkVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkVersion.setStatus("current")


class _DnsTrapsinkUserName_Type(DisplayString):
    """Custom type dnsTrapsinkUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DnsTrapsinkUserName_Type.__name__ = "DisplayString"
_DnsTrapsinkUserName_Object = MibTableColumn
dnsTrapsinkUserName = _DnsTrapsinkUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 7),
    _DnsTrapsinkUserName_Type()
)
dnsTrapsinkUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkUserName.setStatus("current")


class _DnsTrapsinkRemark_Type(OctetString):
    """Custom type dnsTrapsinkRemark based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_DnsTrapsinkRemark_Type.__name__ = "OctetString"
_DnsTrapsinkRemark_Object = MibTableColumn
dnsTrapsinkRemark = _DnsTrapsinkRemark_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 8),
    _DnsTrapsinkRemark_Type()
)
dnsTrapsinkRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkRemark.setStatus("current")


class _DnsTrapsinkLifetime_Type(Integer32):
    """Custom type dnsTrapsinkLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("duration1hour", 1),
          ("duration1day", 2),
          ("duration3days", 3),
          ("duration1week", 4),
          ("duration1month", 5),
          ("unlimited", 6))
    )


_DnsTrapsinkLifetime_Type.__name__ = "Integer32"
_DnsTrapsinkLifetime_Object = MibTableColumn
dnsTrapsinkLifetime = _DnsTrapsinkLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 7, 1, 9),
    _DnsTrapsinkLifetime_Type()
)
dnsTrapsinkLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsTrapsinkLifetime.setStatus("current")


class _SysLogFacility_Type(Integer32):
    """Custom type sysLogFacility based on Integer32"""
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
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_SysLogFacility_Type.__name__ = "Integer32"
_SysLogFacility_Object = MibScalar
sysLogFacility = _SysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 4, 8),
    _SysLogFacility_Type()
)
sysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFacility.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5)
)
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1)
)
_SoftwareVersion_Type = SnmpAdminString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 1),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_LocalDateAndTime_Type = DateAndTime
_LocalDateAndTime_Object = MibScalar
localDateAndTime = _LocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 2),
    _LocalDateAndTime_Type()
)
localDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localDateAndTime.setStatus("current")
_ReleaseNumber_Type = Integer32
_ReleaseNumber_Object = MibScalar
releaseNumber = _ReleaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 3),
    _ReleaseNumber_Type()
)
releaseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releaseNumber.setStatus("current")
_ExpectedSoftwareVersion_Type = SnmpAdminString
_ExpectedSoftwareVersion_Object = MibScalar
expectedSoftwareVersion = _ExpectedSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 1, 4),
    _ExpectedSoftwareVersion_Type()
)
expectedSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expectedSoftwareVersion.setStatus("current")
_IpSettings_ObjectIdentity = ObjectIdentity
ipSettings = _IpSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 3),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_Dns1_Type = IpAddress
_Dns1_Object = MibScalar
dns1 = _Dns1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 4),
    _Dns1_Type()
)
dns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns1.setStatus("current")
_Dns2_Type = IpAddress
_Dns2_Object = MibScalar
dns2 = _Dns2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 5),
    _Dns2_Type()
)
dns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dns2.setStatus("current")


class _Dhcp_Type(Integer32):
    """Custom type dhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Dhcp_Type.__name__ = "Integer32"
_Dhcp_Object = MibScalar
dhcp = _Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 6),
    _Dhcp_Type()
)
dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp.setStatus("current")
_Ipv6Address_Type = SnmpAdminString
_Ipv6Address_Object = MibScalar
ipv6Address = _Ipv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 7),
    _Ipv6Address_Type()
)
ipv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Address.setStatus("current")
_Ipv6Dns1_Type = SnmpAdminString
_Ipv6Dns1_Object = MibScalar
ipv6Dns1 = _Ipv6Dns1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 8),
    _Ipv6Dns1_Type()
)
ipv6Dns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Dns1.setStatus("current")
_Ipv6Dns2_Type = SnmpAdminString
_Ipv6Dns2_Object = MibScalar
ipv6Dns2 = _Ipv6Dns2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 9),
    _Ipv6Dns2_Type()
)
ipv6Dns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Dns2.setStatus("current")
_IpSettingsUsb_ObjectIdentity = ObjectIdentity
ipSettingsUsb = _IpSettingsUsb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10)
)


class _IpSettingsUsbMode_Type(Integer32):
    """Custom type ipSettingsUsbMode based on Integer32"""
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
        *(("disabled", 1),
          ("lan", 2),
          ("mobile", 3),
          ("serial", 4),
          ("lanAdapter", 5),
          ("portExtender", 6))
    )


_IpSettingsUsbMode_Type.__name__ = "Integer32"
_IpSettingsUsbMode_Object = MibScalar
ipSettingsUsbMode = _IpSettingsUsbMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 1),
    _IpSettingsUsbMode_Type()
)
ipSettingsUsbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMode.setStatus("current")
_IpSettingsUsbMobileDialInNumber_Type = SnmpAdminString
_IpSettingsUsbMobileDialInNumber_Object = MibScalar
ipSettingsUsbMobileDialInNumber = _IpSettingsUsbMobileDialInNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 2),
    _IpSettingsUsbMobileDialInNumber_Type()
)
ipSettingsUsbMobileDialInNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileDialInNumber.setStatus("current")
_IpSettingsUsbMobileAPN_Type = SnmpAdminString
_IpSettingsUsbMobileAPN_Object = MibScalar
ipSettingsUsbMobileAPN = _IpSettingsUsbMobileAPN_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 3),
    _IpSettingsUsbMobileAPN_Type()
)
ipSettingsUsbMobileAPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileAPN.setStatus("current")
_IpSettingsUsbMobileUserName_Type = SnmpAdminString
_IpSettingsUsbMobileUserName_Object = MibScalar
ipSettingsUsbMobileUserName = _IpSettingsUsbMobileUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 4),
    _IpSettingsUsbMobileUserName_Type()
)
ipSettingsUsbMobileUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileUserName.setStatus("current")
_IpSettingsUsbMobileUserPassword_Type = SnmpAdminString
_IpSettingsUsbMobileUserPassword_Object = MibScalar
ipSettingsUsbMobileUserPassword = _IpSettingsUsbMobileUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 5),
    _IpSettingsUsbMobileUserPassword_Type()
)
ipSettingsUsbMobileUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileUserPassword.setStatus("current")
_IpSettingsUsbMobileSIMPin_Type = SnmpAdminString
_IpSettingsUsbMobileSIMPin_Object = MibScalar
ipSettingsUsbMobileSIMPin = _IpSettingsUsbMobileSIMPin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 6),
    _IpSettingsUsbMobileSIMPin_Type()
)
ipSettingsUsbMobileSIMPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileSIMPin.setStatus("current")
_IpSettingsUsbMobileIPAddress_Type = SnmpAdminString
_IpSettingsUsbMobileIPAddress_Object = MibScalar
ipSettingsUsbMobileIPAddress = _IpSettingsUsbMobileIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 7),
    _IpSettingsUsbMobileIPAddress_Type()
)
ipSettingsUsbMobileIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileIPAddress.setStatus("current")
_IpSettingsUsbMobileRoutingNetAddress_Type = SnmpAdminString
_IpSettingsUsbMobileRoutingNetAddress_Object = MibScalar
ipSettingsUsbMobileRoutingNetAddress = _IpSettingsUsbMobileRoutingNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 8),
    _IpSettingsUsbMobileRoutingNetAddress_Type()
)
ipSettingsUsbMobileRoutingNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileRoutingNetAddress.setStatus("current")
_IpSettingsUsbMobileRoutingNetMask_Type = SnmpAdminString
_IpSettingsUsbMobileRoutingNetMask_Object = MibScalar
ipSettingsUsbMobileRoutingNetMask = _IpSettingsUsbMobileRoutingNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 9),
    _IpSettingsUsbMobileRoutingNetMask_Type()
)
ipSettingsUsbMobileRoutingNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbMobileRoutingNetMask.setStatus("current")
_IpSettingsUsbLanAdapterIPAddress_Type = SnmpAdminString
_IpSettingsUsbLanAdapterIPAddress_Object = MibScalar
ipSettingsUsbLanAdapterIPAddress = _IpSettingsUsbLanAdapterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 10),
    _IpSettingsUsbLanAdapterIPAddress_Type()
)
ipSettingsUsbLanAdapterIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbLanAdapterIPAddress.setStatus("current")
_IpSettingsUsbLanAdapterSubnetMask_Type = SnmpAdminString
_IpSettingsUsbLanAdapterSubnetMask_Object = MibScalar
ipSettingsUsbLanAdapterSubnetMask = _IpSettingsUsbLanAdapterSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 11),
    _IpSettingsUsbLanAdapterSubnetMask_Type()
)
ipSettingsUsbLanAdapterSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbLanAdapterSubnetMask.setStatus("current")
_IpSettingsUsbLanAdapterGateway_Type = SnmpAdminString
_IpSettingsUsbLanAdapterGateway_Object = MibScalar
ipSettingsUsbLanAdapterGateway = _IpSettingsUsbLanAdapterGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 12),
    _IpSettingsUsbLanAdapterGateway_Type()
)
ipSettingsUsbLanAdapterGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbLanAdapterGateway.setStatus("current")
_IpSettingsUsbLanAdapterRoutingNetAddress_Type = SnmpAdminString
_IpSettingsUsbLanAdapterRoutingNetAddress_Object = MibScalar
ipSettingsUsbLanAdapterRoutingNetAddress = _IpSettingsUsbLanAdapterRoutingNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 13),
    _IpSettingsUsbLanAdapterRoutingNetAddress_Type()
)
ipSettingsUsbLanAdapterRoutingNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbLanAdapterRoutingNetAddress.setStatus("current")
_IpSettingsUsbLanAdapterRoutingNetMask_Type = SnmpAdminString
_IpSettingsUsbLanAdapterRoutingNetMask_Object = MibScalar
ipSettingsUsbLanAdapterRoutingNetMask = _IpSettingsUsbLanAdapterRoutingNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 10, 14),
    _IpSettingsUsbLanAdapterRoutingNetMask_Type()
)
ipSettingsUsbLanAdapterRoutingNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSettingsUsbLanAdapterRoutingNetMask.setStatus("current")
_EthernetPortTable_Object = MibTable
ethernetPortTable = _EthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11)
)
if mibBuilder.loadTexts:
    ethernetPortTable.setStatus("current")
_EthernetPortEntry_Object = MibTableRow
ethernetPortEntry = _EthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1)
)
ethernetPortEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "ethernetPortId"),
)
if mibBuilder.loadTexts:
    ethernetPortEntry.setStatus("current")


class _EthernetPortId_Type(Integer32):
    """Custom type ethernetPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_EthernetPortId_Type.__name__ = "Integer32"
_EthernetPortId_Object = MibTableColumn
ethernetPortId = _EthernetPortId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 1),
    _EthernetPortId_Type()
)
ethernetPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethernetPortId.setStatus("current")
_EthernetPortIdentifier_Type = SnmpAdminString
_EthernetPortIdentifier_Object = MibTableColumn
ethernetPortIdentifier = _EthernetPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 2),
    _EthernetPortIdentifier_Type()
)
ethernetPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPortIdentifier.setStatus("current")


class _EthernetPortMode_Type(Integer32):
    """Custom type ethernetPortMode based on Integer32"""
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
        *(("autoneg", 1),
          ("half10", 2),
          ("full10", 3),
          ("half100", 4),
          ("full100", 5),
          ("full1000", 6))
    )


_EthernetPortMode_Type.__name__ = "Integer32"
_EthernetPortMode_Object = MibTableColumn
ethernetPortMode = _EthernetPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 3),
    _EthernetPortMode_Type()
)
ethernetPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortMode.setStatus("current")


class _EthernetPortBitrate_Type(Integer32):
    """Custom type ethernetPortBitrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bitrate10", 1),
          ("bitrate100", 2),
          ("bitrate1000", 3))
    )


_EthernetPortBitrate_Type.__name__ = "Integer32"
_EthernetPortBitrate_Object = MibTableColumn
ethernetPortBitrate = _EthernetPortBitrate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 4),
    _EthernetPortBitrate_Type()
)
ethernetPortBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPortBitrate.setStatus("current")


class _EthernetPortDuplex_Type(Integer32):
    """Custom type ethernetPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_EthernetPortDuplex_Type.__name__ = "Integer32"
_EthernetPortDuplex_Object = MibTableColumn
ethernetPortDuplex = _EthernetPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 5),
    _EthernetPortDuplex_Type()
)
ethernetPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetPortDuplex.setStatus("current")


class _EthernetPortMtu_Type(Integer32):
    """Custom type ethernetPortMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 1500),
    )


_EthernetPortMtu_Type.__name__ = "Integer32"
_EthernetPortMtu_Object = MibTableColumn
ethernetPortMtu = _EthernetPortMtu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 2, 11, 1, 6),
    _EthernetPortMtu_Type()
)
ethernetPortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPortMtu.setStatus("current")
_SoftwareMgmt_ObjectIdentity = ObjectIdentity
softwareMgmt = _SoftwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3)
)
_SoftwareMgmtFileTable_Object = MibTable
softwareMgmtFileTable = _SoftwareMgmtFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1)
)
if mibBuilder.loadTexts:
    softwareMgmtFileTable.setStatus("current")
_SoftwareMgmtFileEntry_Object = MibTableRow
softwareMgmtFileEntry = _SoftwareMgmtFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1)
)
softwareMgmtFileEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "softwareMgmtFileIndex"),
)
if mibBuilder.loadTexts:
    softwareMgmtFileEntry.setStatus("current")


class _SoftwareMgmtFileIndex_Type(Integer32):
    """Custom type softwareMgmtFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SoftwareMgmtFileIndex_Type.__name__ = "Integer32"
_SoftwareMgmtFileIndex_Object = MibTableColumn
softwareMgmtFileIndex = _SoftwareMgmtFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 1),
    _SoftwareMgmtFileIndex_Type()
)
softwareMgmtFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    softwareMgmtFileIndex.setStatus("current")
_SoftwareMgmtFileSize_Type = Unsigned32
_SoftwareMgmtFileSize_Object = MibTableColumn
softwareMgmtFileSize = _SoftwareMgmtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 2),
    _SoftwareMgmtFileSize_Type()
)
softwareMgmtFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileSize.setStatus("current")
if mibBuilder.loadTexts:
    softwareMgmtFileSize.setUnits("Byte")
_SoftwareMgmtFileCreationTime_Type = DateAndTime
_SoftwareMgmtFileCreationTime_Object = MibTableColumn
softwareMgmtFileCreationTime = _SoftwareMgmtFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 3),
    _SoftwareMgmtFileCreationTime_Type()
)
softwareMgmtFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileCreationTime.setStatus("current")
_SoftwareMgmtFileVersion_Type = SnmpAdminString
_SoftwareMgmtFileVersion_Object = MibTableColumn
softwareMgmtFileVersion = _SoftwareMgmtFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 4),
    _SoftwareMgmtFileVersion_Type()
)
softwareMgmtFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileVersion.setStatus("current")
_SoftwareMgmtFileFileName_Type = SnmpAdminString
_SoftwareMgmtFileFileName_Object = MibTableColumn
softwareMgmtFileFileName = _SoftwareMgmtFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 5),
    _SoftwareMgmtFileFileName_Type()
)
softwareMgmtFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtFileFileName.setStatus("current")
_SoftwareMgmtFileRowStatus_Type = RowStatus
_SoftwareMgmtFileRowStatus_Object = MibTableColumn
softwareMgmtFileRowStatus = _SoftwareMgmtFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 1, 1, 6),
    _SoftwareMgmtFileRowStatus_Type()
)
softwareMgmtFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFileRowStatus.setStatus("current")


class _SoftwareMgmtRequest_Type(Integer32):
    """Custom type softwareMgmtRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("download", 2),
          ("installActivate", 3),
          ("reboot", 6),
          ("downloadInstallActivate", 8))
    )


_SoftwareMgmtRequest_Type.__name__ = "Integer32"
_SoftwareMgmtRequest_Object = MibScalar
softwareMgmtRequest = _SoftwareMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 2),
    _SoftwareMgmtRequest_Type()
)
softwareMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtRequest.setStatus("current")


class _SoftwareMgmtState_Type(Integer32):
    """Custom type softwareMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("downloading", 2),
          ("downloadReadyForInstallation", 3),
          ("installingSoftware", 4),
          ("rebooting", 7),
          ("failure", 8))
    )


_SoftwareMgmtState_Type.__name__ = "Integer32"
_SoftwareMgmtState_Object = MibScalar
softwareMgmtState = _SoftwareMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 3),
    _SoftwareMgmtState_Type()
)
softwareMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtState.setStatus("current")


class _SoftwareMgmtLastError_Type(Integer32):
    """Custom type softwareMgmtLastError based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("downloadLoginFailed", 2),
          ("downloadFileNotFound", 3),
          ("downloadFileNoAccess", 4),
          ("downloadServerUnreachable", 5),
          ("downloadFailed", 6),
          ("installationFailed", 7),
          ("restoreFailed", 8),
          ("noSpaceLeft", 9),
          ("internalError", 10),
          ("invalidBackupFile", 11),
          ("installationVersionMismatch", 12),
          ("installationFileNotExist", 13),
          ("installationChecksumError", 14),
          ("invalidBackupPassword", 15))
    )


_SoftwareMgmtLastError_Type.__name__ = "Integer32"
_SoftwareMgmtLastError_Object = MibScalar
softwareMgmtLastError = _SoftwareMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 4),
    _SoftwareMgmtLastError_Type()
)
softwareMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtLastError.setStatus("current")


class _SoftwareMgmtDatabaseUsage_Type(Integer32):
    """Custom type softwareMgmtDatabaseUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("storage", 2),
          ("factoryDefault", 3))
    )


_SoftwareMgmtDatabaseUsage_Type.__name__ = "Integer32"
_SoftwareMgmtDatabaseUsage_Object = MibScalar
softwareMgmtDatabaseUsage = _SoftwareMgmtDatabaseUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 5),
    _SoftwareMgmtDatabaseUsage_Type()
)
softwareMgmtDatabaseUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtDatabaseUsage.setStatus("current")
_SoftwareMgmtDatabaseFileName_Type = SnmpAdminString
_SoftwareMgmtDatabaseFileName_Object = MibScalar
softwareMgmtDatabaseFileName = _SoftwareMgmtDatabaseFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 6),
    _SoftwareMgmtDatabaseFileName_Type()
)
softwareMgmtDatabaseFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtDatabaseFileName.setStatus("current")
_SoftwareMgmtServerAddress_Type = IpAddress
_SoftwareMgmtServerAddress_Object = MibScalar
softwareMgmtServerAddress = _SoftwareMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 7),
    _SoftwareMgmtServerAddress_Type()
)
softwareMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerAddress.setStatus("current")
_SoftwareMgmtServerLogin_Type = SnmpAdminString
_SoftwareMgmtServerLogin_Object = MibScalar
softwareMgmtServerLogin = _SoftwareMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 8),
    _SoftwareMgmtServerLogin_Type()
)
softwareMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerLogin.setStatus("current")
_SoftwareMgmtServerPasswd_Type = SnmpAdminString
_SoftwareMgmtServerPasswd_Object = MibScalar
softwareMgmtServerPasswd = _SoftwareMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 9),
    _SoftwareMgmtServerPasswd_Type()
)
softwareMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerPasswd.setStatus("current")
_SoftwareMgmtServerDirectory_Type = SnmpAdminString
_SoftwareMgmtServerDirectory_Object = MibScalar
softwareMgmtServerDirectory = _SoftwareMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 10),
    _SoftwareMgmtServerDirectory_Type()
)
softwareMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtServerDirectory.setStatus("current")
_SoftwareMgmtFileName_Type = SnmpAdminString
_SoftwareMgmtFileName_Object = MibScalar
softwareMgmtFileName = _SoftwareMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 11),
    _SoftwareMgmtFileName_Type()
)
softwareMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFileName.setStatus("current")


class _SoftwareMgmtTransferProtocol_Type(Integer32):
    """Custom type softwareMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_SoftwareMgmtTransferProtocol_Type.__name__ = "Integer32"
_SoftwareMgmtTransferProtocol_Object = MibScalar
softwareMgmtTransferProtocol = _SoftwareMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 12),
    _SoftwareMgmtTransferProtocol_Type()
)
softwareMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtTransferProtocol.setStatus("current")


class _SoftwareMgmtFtpPort_Type(Integer32):
    """Custom type softwareMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SoftwareMgmtFtpPort_Type.__name__ = "Integer32"
_SoftwareMgmtFtpPort_Object = MibScalar
softwareMgmtFtpPort = _SoftwareMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 13),
    _SoftwareMgmtFtpPort_Type()
)
softwareMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtFtpPort.setStatus("current")


class _SoftwareMgmtActionProgress_Type(Integer32):
    """Custom type softwareMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_SoftwareMgmtActionProgress_Type.__name__ = "Integer32"
_SoftwareMgmtActionProgress_Object = MibScalar
softwareMgmtActionProgress = _SoftwareMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 14),
    _SoftwareMgmtActionProgress_Type()
)
softwareMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    softwareMgmtActionProgress.setUnits("%")
_SoftwareMgmtIpv6Address_Type = SnmpAdminString
_SoftwareMgmtIpv6Address_Object = MibScalar
softwareMgmtIpv6Address = _SoftwareMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 15),
    _SoftwareMgmtIpv6Address_Type()
)
softwareMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtIpv6Address.setStatus("current")


class _SoftwareMgmtScpPort_Type(Integer32):
    """Custom type softwareMgmtScpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SoftwareMgmtScpPort_Type.__name__ = "Integer32"
_SoftwareMgmtScpPort_Object = MibScalar
softwareMgmtScpPort = _SoftwareMgmtScpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 16),
    _SoftwareMgmtScpPort_Type()
)
softwareMgmtScpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtScpPort.setStatus("current")
_SoftwareMgmtBackupPassword_Type = SnmpAdminString
_SoftwareMgmtBackupPassword_Object = MibScalar
softwareMgmtBackupPassword = _SoftwareMgmtBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 3, 17),
    _SoftwareMgmtBackupPassword_Type()
)
softwareMgmtBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softwareMgmtBackupPassword.setStatus("current")
_DatabaseMgmt_ObjectIdentity = ObjectIdentity
databaseMgmt = _DatabaseMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4)
)
_DatabaseMgmtFileTable_Object = MibTable
databaseMgmtFileTable = _DatabaseMgmtFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1)
)
if mibBuilder.loadTexts:
    databaseMgmtFileTable.setStatus("current")
_DatabaseMgmtFileEntry_Object = MibTableRow
databaseMgmtFileEntry = _DatabaseMgmtFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1)
)
databaseMgmtFileEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "databaseMgmtFileIndex"),
)
if mibBuilder.loadTexts:
    databaseMgmtFileEntry.setStatus("current")


class _DatabaseMgmtFileIndex_Type(Integer32):
    """Custom type databaseMgmtFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DatabaseMgmtFileIndex_Type.__name__ = "Integer32"
_DatabaseMgmtFileIndex_Object = MibTableColumn
databaseMgmtFileIndex = _DatabaseMgmtFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 1),
    _DatabaseMgmtFileIndex_Type()
)
databaseMgmtFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    databaseMgmtFileIndex.setStatus("current")
_DatabaseMgmtFileSize_Type = Unsigned32
_DatabaseMgmtFileSize_Object = MibTableColumn
databaseMgmtFileSize = _DatabaseMgmtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 2),
    _DatabaseMgmtFileSize_Type()
)
databaseMgmtFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileSize.setStatus("current")
if mibBuilder.loadTexts:
    databaseMgmtFileSize.setUnits("Byte")
_DatabaseMgmtFileCreationTime_Type = DateAndTime
_DatabaseMgmtFileCreationTime_Object = MibTableColumn
databaseMgmtFileCreationTime = _DatabaseMgmtFileCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 3),
    _DatabaseMgmtFileCreationTime_Type()
)
databaseMgmtFileCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileCreationTime.setStatus("current")
_DatabaseMgmtFileVersion_Type = SnmpAdminString
_DatabaseMgmtFileVersion_Object = MibTableColumn
databaseMgmtFileVersion = _DatabaseMgmtFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 4),
    _DatabaseMgmtFileVersion_Type()
)
databaseMgmtFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileVersion.setStatus("current")
_DatabaseMgmtFileFileName_Type = SnmpAdminString
_DatabaseMgmtFileFileName_Object = MibTableColumn
databaseMgmtFileFileName = _DatabaseMgmtFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 5),
    _DatabaseMgmtFileFileName_Type()
)
databaseMgmtFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtFileFileName.setStatus("current")
_DatabaseMgmtFileRowStatus_Type = RowStatus
_DatabaseMgmtFileRowStatus_Object = MibTableColumn
databaseMgmtFileRowStatus = _DatabaseMgmtFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 1, 1, 6),
    _DatabaseMgmtFileRowStatus_Type()
)
databaseMgmtFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFileRowStatus.setStatus("current")


class _DatabaseMgmtRequest_Type(Integer32):
    """Custom type databaseMgmtRequest based on Integer32"""
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
        *(("none", 1),
          ("download", 2),
          ("upload", 3),
          ("runBackup", 4),
          ("runBackupUpload", 5),
          ("runRestore", 6),
          ("runDownloadRestore", 7),
          ("resetToFactory", 8))
    )


_DatabaseMgmtRequest_Type.__name__ = "Integer32"
_DatabaseMgmtRequest_Object = MibScalar
databaseMgmtRequest = _DatabaseMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 2),
    _DatabaseMgmtRequest_Type()
)
databaseMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtRequest.setStatus("current")


class _DatabaseMgmtState_Type(Integer32):
    """Custom type databaseMgmtState based on Integer32"""
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
        *(("idle", 1),
          ("downloading", 2),
          ("uploading", 3),
          ("runningBackup", 4),
          ("runningRestore", 5),
          ("resettingToFactory", 6),
          ("failure", 7))
    )


_DatabaseMgmtState_Type.__name__ = "Integer32"
_DatabaseMgmtState_Object = MibScalar
databaseMgmtState = _DatabaseMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 3),
    _DatabaseMgmtState_Type()
)
databaseMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtState.setStatus("current")


class _DatabaseMgmtLastError_Type(Integer32):
    """Custom type databaseMgmtLastError based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("transferLoginFailed", 2),
          ("transferFileNotFound", 3),
          ("transferFileNoAccess", 4),
          ("transferServerUnreachable", 5),
          ("transferFailed", 6),
          ("backupFailed", 7),
          ("restoreFailed", 8),
          ("noSpaceLeft", 9),
          ("internalError", 10),
          ("invalidBackupFile", 11),
          ("invalidBackupPassword", 15))
    )


_DatabaseMgmtLastError_Type.__name__ = "Integer32"
_DatabaseMgmtLastError_Object = MibScalar
databaseMgmtLastError = _DatabaseMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 4),
    _DatabaseMgmtLastError_Type()
)
databaseMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtLastError.setStatus("current")
_DatabaseMgmtServerAddress_Type = IpAddress
_DatabaseMgmtServerAddress_Object = MibScalar
databaseMgmtServerAddress = _DatabaseMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 5),
    _DatabaseMgmtServerAddress_Type()
)
databaseMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerAddress.setStatus("current")
_DatabaseMgmtServerLogin_Type = SnmpAdminString
_DatabaseMgmtServerLogin_Object = MibScalar
databaseMgmtServerLogin = _DatabaseMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 6),
    _DatabaseMgmtServerLogin_Type()
)
databaseMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerLogin.setStatus("current")
_DatabaseMgmtServerPasswd_Type = SnmpAdminString
_DatabaseMgmtServerPasswd_Object = MibScalar
databaseMgmtServerPasswd = _DatabaseMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 7),
    _DatabaseMgmtServerPasswd_Type()
)
databaseMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerPasswd.setStatus("current")
_DatabaseMgmtServerDirectory_Type = SnmpAdminString
_DatabaseMgmtServerDirectory_Object = MibScalar
databaseMgmtServerDirectory = _DatabaseMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 8),
    _DatabaseMgmtServerDirectory_Type()
)
databaseMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtServerDirectory.setStatus("current")
_DatabaseMgmtFileName_Type = SnmpAdminString
_DatabaseMgmtFileName_Object = MibScalar
databaseMgmtFileName = _DatabaseMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 9),
    _DatabaseMgmtFileName_Type()
)
databaseMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFileName.setStatus("current")


class _DatabaseMgmtTransferProtocol_Type(Integer32):
    """Custom type databaseMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_DatabaseMgmtTransferProtocol_Type.__name__ = "Integer32"
_DatabaseMgmtTransferProtocol_Object = MibScalar
databaseMgmtTransferProtocol = _DatabaseMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 10),
    _DatabaseMgmtTransferProtocol_Type()
)
databaseMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtTransferProtocol.setStatus("current")


class _DatabaseMgmtFtpPort_Type(Integer32):
    """Custom type databaseMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DatabaseMgmtFtpPort_Type.__name__ = "Integer32"
_DatabaseMgmtFtpPort_Object = MibScalar
databaseMgmtFtpPort = _DatabaseMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 11),
    _DatabaseMgmtFtpPort_Type()
)
databaseMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtFtpPort.setStatus("current")


class _DatabaseMgmtActionProgress_Type(Integer32):
    """Custom type databaseMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_DatabaseMgmtActionProgress_Type.__name__ = "Integer32"
_DatabaseMgmtActionProgress_Object = MibScalar
databaseMgmtActionProgress = _DatabaseMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 12),
    _DatabaseMgmtActionProgress_Type()
)
databaseMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    databaseMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    databaseMgmtActionProgress.setUnits("%")
_DatabaseMgmtIpv6Address_Type = SnmpAdminString
_DatabaseMgmtIpv6Address_Object = MibScalar
databaseMgmtIpv6Address = _DatabaseMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 13),
    _DatabaseMgmtIpv6Address_Type()
)
databaseMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtIpv6Address.setStatus("current")


class _DatabaseMgmtScpPort_Type(Integer32):
    """Custom type databaseMgmtScpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DatabaseMgmtScpPort_Type.__name__ = "Integer32"
_DatabaseMgmtScpPort_Object = MibScalar
databaseMgmtScpPort = _DatabaseMgmtScpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 14),
    _DatabaseMgmtScpPort_Type()
)
databaseMgmtScpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtScpPort.setStatus("current")
_DatabaseMgmtBackupPassword_Type = SnmpAdminString
_DatabaseMgmtBackupPassword_Object = MibScalar
databaseMgmtBackupPassword = _DatabaseMgmtBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 4, 15),
    _DatabaseMgmtBackupPassword_Type()
)
databaseMgmtBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    databaseMgmtBackupPassword.setStatus("current")
_NtpMgmt_ObjectIdentity = ObjectIdentity
ntpMgmt = _NtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5)
)


class _NtpClientConfig_Type(Integer32):
    """Custom type ntpClientConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NtpClientConfig_Type.__name__ = "Integer32"
_NtpClientConfig_Object = MibScalar
ntpClientConfig = _NtpClientConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 1),
    _NtpClientConfig_Type()
)
ntpClientConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientConfig.setStatus("current")
_NtpServerName_Type = DisplayString
_NtpServerName_Object = MibScalar
ntpServerName = _NtpServerName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 2),
    _NtpServerName_Type()
)
ntpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerName.setStatus("current")
_NtpServerName2_Type = DisplayString
_NtpServerName2_Object = MibScalar
ntpServerName2 = _NtpServerName2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 3),
    _NtpServerName2_Type()
)
ntpServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerName2.setStatus("current")
_NtpServerName3_Type = DisplayString
_NtpServerName3_Object = MibScalar
ntpServerName3 = _NtpServerName3_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 4),
    _NtpServerName3_Type()
)
ntpServerName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerName3.setStatus("current")
_NtpTimeChangeReason_Type = DisplayString
_NtpTimeChangeReason_Object = MibScalar
ntpTimeChangeReason = _NtpTimeChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 5, 5),
    _NtpTimeChangeReason_Type()
)
ntpTimeChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntpTimeChangeReason.setStatus("current")
_GeneralSettings_ObjectIdentity = ObjectIdentity
generalSettings = _GeneralSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6)
)


class _OperationMode_Type(Integer32):
    """Custom type operationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("controller", 2))
    )


_OperationMode_Type.__name__ = "Integer32"
_OperationMode_Object = MibScalar
operationMode = _OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 1),
    _OperationMode_Type()
)
operationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationMode.setStatus("current")


class _HttpsPort_Type(Integer32):
    """Custom type httpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpsPort_Type.__name__ = "Integer32"
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 2),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")
_Access_ObjectIdentity = ObjectIdentity
access = _Access_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3)
)


class _SshInterface_Type(Integer32):
    """Custom type sshInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SshInterface_Type.__name__ = "Integer32"
_SshInterface_Object = MibScalar
sshInterface = _SshInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 1),
    _SshInterface_Type()
)
sshInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshInterface.setStatus("current")


class _NetconfInterface_Type(Integer32):
    """Custom type netconfInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NetconfInterface_Type.__name__ = "Integer32"
_NetconfInterface_Object = MibScalar
netconfInterface = _NetconfInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 2),
    _NetconfInterface_Type()
)
netconfInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netconfInterface.setStatus("current")


class _SshPasswordAuthentication_Type(Integer32):
    """Custom type sshPasswordAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SshPasswordAuthentication_Type.__name__ = "Integer32"
_SshPasswordAuthentication_Object = MibScalar
sshPasswordAuthentication = _SshPasswordAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 3),
    _SshPasswordAuthentication_Type()
)
sshPasswordAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPasswordAuthentication.setStatus("current")


class _GeneralSessionTimeout_Type(Integer32):
    """Custom type generalSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_GeneralSessionTimeout_Type.__name__ = "Integer32"
_GeneralSessionTimeout_Object = MibScalar
generalSessionTimeout = _GeneralSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 4),
    _GeneralSessionTimeout_Type()
)
generalSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generalSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    generalSessionTimeout.setUnits("min")


class _SnmpSessionTimeout_Type(Integer32):
    """Custom type snmpSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_SnmpSessionTimeout_Type.__name__ = "Integer32"
_SnmpSessionTimeout_Object = MibScalar
snmpSessionTimeout = _SnmpSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 5),
    _SnmpSessionTimeout_Type()
)
snmpSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    snmpSessionTimeout.setUnits("min")


class _MaxLoginFailureDelay_Type(Integer32):
    """Custom type maxLoginFailureDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_MaxLoginFailureDelay_Type.__name__ = "Integer32"
_MaxLoginFailureDelay_Object = MibScalar
maxLoginFailureDelay = _MaxLoginFailureDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 6),
    _MaxLoginFailureDelay_Type()
)
maxLoginFailureDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLoginFailureDelay.setStatus("current")
if mibBuilder.loadTexts:
    maxLoginFailureDelay.setUnits("s")


class _PasswordStrength_Type(Integer32):
    """Custom type passwordStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_PasswordStrength_Type.__name__ = "Integer32"
_PasswordStrength_Object = MibScalar
passwordStrength = _PasswordStrength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 7),
    _PasswordStrength_Type()
)
passwordStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwordStrength.setStatus("current")


class _UserInfoDeletionPeriod_Type(Integer32):
    """Custom type userInfoDeletionPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1096),
    )


_UserInfoDeletionPeriod_Type.__name__ = "Integer32"
_UserInfoDeletionPeriod_Object = MibScalar
userInfoDeletionPeriod = _UserInfoDeletionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 8),
    _UserInfoDeletionPeriod_Type()
)
userInfoDeletionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userInfoDeletionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    userInfoDeletionPeriod.setUnits("d")


class _DefaultTrapsinkLifetime_Type(Integer32):
    """Custom type defaultTrapsinkLifetime based on Integer32"""
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
        *(("duration1hour", 1),
          ("duration1day", 2),
          ("duration3days", 3),
          ("duration1week", 4),
          ("duration1month", 5),
          ("unlimited", 6))
    )


_DefaultTrapsinkLifetime_Type.__name__ = "Integer32"
_DefaultTrapsinkLifetime_Object = MibScalar
defaultTrapsinkLifetime = _DefaultTrapsinkLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 3, 9),
    _DefaultTrapsinkLifetime_Type()
)
defaultTrapsinkLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultTrapsinkLifetime.setStatus("current")
_Pki_ObjectIdentity = ObjectIdentity
pki = _Pki_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4)
)
_CaTable_Object = MibTable
caTable = _CaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1)
)
if mibBuilder.loadTexts:
    caTable.setStatus("current")
_CaEntry_Object = MibTableRow
caEntry = _CaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1)
)
caEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "caId"),
)
if mibBuilder.loadTexts:
    caEntry.setStatus("current")
_CaId_Type = Unsigned32
_CaId_Object = MibTableColumn
caId = _CaId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 1),
    _CaId_Type()
)
caId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    caId.setStatus("current")
_CaRowStatus_Type = RowStatus
_CaRowStatus_Object = MibTableColumn
caRowStatus = _CaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 2),
    _CaRowStatus_Type()
)
caRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caRowStatus.setStatus("current")
_CaAlias_Type = SnmpAdminString
_CaAlias_Object = MibTableColumn
caAlias = _CaAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 3),
    _CaAlias_Type()
)
caAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caAlias.setStatus("current")
_CaScepUrl_Type = SnmpAdminString
_CaScepUrl_Object = MibTableColumn
caScepUrl = _CaScepUrl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 4),
    _CaScepUrl_Type()
)
caScepUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepUrl.setStatus("current")
_CaScepDomainName_Type = SnmpAdminString
_CaScepDomainName_Object = MibTableColumn
caScepDomainName = _CaScepDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 5),
    _CaScepDomainName_Type()
)
caScepDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepDomainName.setStatus("current")
_CaScepUserName_Type = SnmpAdminString
_CaScepUserName_Object = MibTableColumn
caScepUserName = _CaScepUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 6),
    _CaScepUserName_Type()
)
caScepUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepUserName.setStatus("current")
_CaScepPassword_Type = SnmpAdminString
_CaScepPassword_Object = MibTableColumn
caScepPassword = _CaScepPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 7),
    _CaScepPassword_Type()
)
caScepPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepPassword.setStatus("current")


class _CaScepCertValidation_Type(Integer32):
    """Custom type caScepCertValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CaScepCertValidation_Type.__name__ = "Integer32"
_CaScepCertValidation_Object = MibTableColumn
caScepCertValidation = _CaScepCertValidation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 8),
    _CaScepCertValidation_Type()
)
caScepCertValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepCertValidation.setStatus("current")
_CaScepQueryMessage_Type = SnmpAdminString
_CaScepQueryMessage_Object = MibTableColumn
caScepQueryMessage = _CaScepQueryMessage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 9),
    _CaScepQueryMessage_Type()
)
caScepQueryMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepQueryMessage.setStatus("current")


class _CaScepCipherAlgorithm_Type(Integer32):
    """Custom type caScepCipherAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipherAes128", 1),
          ("cipher3des", 2))
    )


_CaScepCipherAlgorithm_Type.__name__ = "Integer32"
_CaScepCipherAlgorithm_Object = MibTableColumn
caScepCipherAlgorithm = _CaScepCipherAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 10),
    _CaScepCipherAlgorithm_Type()
)
caScepCipherAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepCipherAlgorithm.setStatus("current")


class _CaScepDigestAlgorithm_Type(Integer32):
    """Custom type caScepDigestAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sha1", 1),
          ("sha256", 2),
          ("sha512", 3))
    )


_CaScepDigestAlgorithm_Type.__name__ = "Integer32"
_CaScepDigestAlgorithm_Object = MibTableColumn
caScepDigestAlgorithm = _CaScepDigestAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 11),
    _CaScepDigestAlgorithm_Type()
)
caScepDigestAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepDigestAlgorithm.setStatus("current")


class _CaScepRequestMethod_Type(Integer32):
    """Custom type caScepRequestMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("post", 2))
    )


_CaScepRequestMethod_Type.__name__ = "Integer32"
_CaScepRequestMethod_Object = MibTableColumn
caScepRequestMethod = _CaScepRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 1, 1, 12),
    _CaScepRequestMethod_Type()
)
caScepRequestMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caScepRequestMethod.setStatus("current")
_KeyTable_Object = MibTable
keyTable = _KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2)
)
if mibBuilder.loadTexts:
    keyTable.setStatus("current")
_KeyEntry_Object = MibTableRow
keyEntry = _KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1)
)
keyEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "keyId"),
)
if mibBuilder.loadTexts:
    keyEntry.setStatus("current")
_KeyId_Type = Unsigned32
_KeyId_Object = MibTableColumn
keyId = _KeyId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 1),
    _KeyId_Type()
)
keyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    keyId.setStatus("current")
_KeyRowStatus_Type = RowStatus
_KeyRowStatus_Object = MibTableColumn
keyRowStatus = _KeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 2),
    _KeyRowStatus_Type()
)
keyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyRowStatus.setStatus("current")
_KeyAlias_Type = SnmpAdminString
_KeyAlias_Object = MibTableColumn
keyAlias = _KeyAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 3),
    _KeyAlias_Type()
)
keyAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyAlias.setStatus("current")


class _KeyProfile_Type(Integer32):
    """Custom type keyProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("web", 2))
    )


_KeyProfile_Type.__name__ = "Integer32"
_KeyProfile_Object = MibTableColumn
keyProfile = _KeyProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 4),
    _KeyProfile_Type()
)
keyProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyProfile.setStatus("current")


class _KeyAlgorithm_Type(Integer32):
    """Custom type keyAlgorithm based on Integer32"""
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
        *(("undefined", 0),
          ("rsa", 1),
          ("dsa", 2),
          ("ecdsa", 3))
    )


_KeyAlgorithm_Type.__name__ = "Integer32"
_KeyAlgorithm_Object = MibTableColumn
keyAlgorithm = _KeyAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 5),
    _KeyAlgorithm_Type()
)
keyAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyAlgorithm.setStatus("current")


class _KeyLength_Type(Integer32):
    """Custom type keyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("len256", 1),
          ("len384", 2),
          ("len1024", 3),
          ("len2048", 4),
          ("len3072", 5),
          ("len4096", 6))
    )


_KeyLength_Type.__name__ = "Integer32"
_KeyLength_Object = MibTableColumn
keyLength = _KeyLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 6),
    _KeyLength_Type()
)
keyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyLength.setStatus("current")


class _KeySha1_Type(OctetString):
    """Custom type keySha1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KeySha1_Type.__name__ = "OctetString"
_KeySha1_Object = MibTableColumn
keySha1 = _KeySha1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 7),
    _KeySha1_Type()
)
keySha1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySha1.setStatus("current")


class _KeySha256_Type(OctetString):
    """Custom type keySha256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KeySha256_Type.__name__ = "OctetString"
_KeySha256_Object = MibTableColumn
keySha256 = _KeySha256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 8),
    _KeySha256_Type()
)
keySha256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySha256.setStatus("current")
_KeyCertCommonName_Type = SnmpAdminString
_KeyCertCommonName_Object = MibTableColumn
keyCertCommonName = _KeyCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 9),
    _KeyCertCommonName_Type()
)
keyCertCommonName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertCommonName.setStatus("current")
_KeyCertAlternativeNameIp_Type = SnmpAdminString
_KeyCertAlternativeNameIp_Object = MibTableColumn
keyCertAlternativeNameIp = _KeyCertAlternativeNameIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 10),
    _KeyCertAlternativeNameIp_Type()
)
keyCertAlternativeNameIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertAlternativeNameIp.setStatus("current")
_KeyCertAlternativeNameDns_Type = SnmpAdminString
_KeyCertAlternativeNameDns_Object = MibTableColumn
keyCertAlternativeNameDns = _KeyCertAlternativeNameDns_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 11),
    _KeyCertAlternativeNameDns_Type()
)
keyCertAlternativeNameDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertAlternativeNameDns.setStatus("current")
_KeyCertKeyUsage_Type = SnmpAdminString
_KeyCertKeyUsage_Object = MibTableColumn
keyCertKeyUsage = _KeyCertKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 12),
    _KeyCertKeyUsage_Type()
)
keyCertKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCertKeyUsage.setStatus("current")
_KeyCertExtKeyUsage_Type = SnmpAdminString
_KeyCertExtKeyUsage_Object = MibTableColumn
keyCertExtKeyUsage = _KeyCertExtKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 13),
    _KeyCertExtKeyUsage_Type()
)
keyCertExtKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCertExtKeyUsage.setStatus("current")
_KeyCertValidityPeriod_Type = Integer32
_KeyCertValidityPeriod_Object = MibTableColumn
keyCertValidityPeriod = _KeyCertValidityPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 14),
    _KeyCertValidityPeriod_Type()
)
keyCertValidityPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertValidityPeriod.setStatus("current")
if mibBuilder.loadTexts:
    keyCertValidityPeriod.setUnits("y")
_KeyCertRequestChallenge_Type = SnmpAdminString
_KeyCertRequestChallenge_Object = MibTableColumn
keyCertRequestChallenge = _KeyCertRequestChallenge_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 15),
    _KeyCertRequestChallenge_Type()
)
keyCertRequestChallenge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertRequestChallenge.setStatus("current")


class _KeyCertRenewMode_Type(Integer32):
    """Custom type keyCertRenewMode based on Integer32"""
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
        *(("manual", 1),
          ("autoSelfSinged", 2),
          ("autoNoChallengeNewKey", 3),
          ("autoChallengeNoNewKey", 4),
          ("autoNoChallengeNoNewKey", 5),
          ("autoChallengeNewKey", 6))
    )


_KeyCertRenewMode_Type.__name__ = "Integer32"
_KeyCertRenewMode_Object = MibTableColumn
keyCertRenewMode = _KeyCertRenewMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 16),
    _KeyCertRenewMode_Type()
)
keyCertRenewMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertRenewMode.setStatus("current")
_KeyCertRenewInterval_Type = Integer32
_KeyCertRenewInterval_Object = MibTableColumn
keyCertRenewInterval = _KeyCertRenewInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 17),
    _KeyCertRenewInterval_Type()
)
keyCertRenewInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertRenewInterval.setStatus("current")
if mibBuilder.loadTexts:
    keyCertRenewInterval.setUnits("%|min")
_KeyCertRenewRetryInterval_Type = Integer32
_KeyCertRenewRetryInterval_Object = MibTableColumn
keyCertRenewRetryInterval = _KeyCertRenewRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 18),
    _KeyCertRenewRetryInterval_Type()
)
keyCertRenewRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertRenewRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    keyCertRenewRetryInterval.setUnits("min")
_KeyCertRenewDate_Type = DateAndTime
_KeyCertRenewDate_Object = MibTableColumn
keyCertRenewDate = _KeyCertRenewDate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 19),
    _KeyCertRenewDate_Type()
)
keyCertRenewDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCertRenewDate.setStatus("current")
_KeyCertWarnInterval_Type = Integer32
_KeyCertWarnInterval_Object = MibTableColumn
keyCertWarnInterval = _KeyCertWarnInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 20),
    _KeyCertWarnInterval_Type()
)
keyCertWarnInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    keyCertWarnInterval.setStatus("current")


class _KeyCertRequest_Type(Integer32):
    """Custom type keyCertRequest based on Integer32"""
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
          ("newCert", 2),
          ("renewCert", 3))
    )


_KeyCertRequest_Type.__name__ = "Integer32"
_KeyCertRequest_Object = MibTableColumn
keyCertRequest = _KeyCertRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 21),
    _KeyCertRequest_Type()
)
keyCertRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyCertRequest.setStatus("current")


class _KeyCertRequestStatus_Type(Integer32):
    """Custom type keyCertRequestStatus based on Integer32"""
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
        *(("idle", 1),
          ("running", 2),
          ("generalError", 3),
          ("applyError", 4),
          ("networkError", 5),
          ("scepCapsError", 6),
          ("scepProtoError", 7),
          ("authError", 8),
          ("urlError", 9),
          ("hostError", 10),
          ("timeoutError", 11),
          ("certAttributeError", 12),
          ("certError", 13))
    )


_KeyCertRequestStatus_Type.__name__ = "Integer32"
_KeyCertRequestStatus_Object = MibTableColumn
keyCertRequestStatus = _KeyCertRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 22),
    _KeyCertRequestStatus_Type()
)
keyCertRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCertRequestStatus.setStatus("current")
_KeyCaEntity_Type = SnmpAdminString
_KeyCaEntity_Object = MibTableColumn
keyCaEntity = _KeyCaEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 23),
    _KeyCaEntity_Type()
)
keyCaEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCaEntity.setStatus("current")
_KeyCertificates_Type = SnmpAdminString
_KeyCertificates_Object = MibTableColumn
keyCertificates = _KeyCertificates_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 2, 1, 24),
    _KeyCertificates_Type()
)
keyCertificates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyCertificates.setStatus("current")
_CertificateTable_Object = MibTable
certificateTable = _CertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3)
)
if mibBuilder.loadTexts:
    certificateTable.setStatus("current")
_CertificateEntry_Object = MibTableRow
certificateEntry = _CertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1)
)
certificateEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "certificateId"),
)
if mibBuilder.loadTexts:
    certificateEntry.setStatus("current")
_CertificateId_Type = Unsigned32
_CertificateId_Object = MibTableColumn
certificateId = _CertificateId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 1),
    _CertificateId_Type()
)
certificateId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    certificateId.setStatus("current")


class _CertificateType_Type(Integer32):
    """Custom type certificateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              13,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("selfSigned", 13),
          ("endEntity", 15),
          ("manual", 16))
    )


_CertificateType_Type.__name__ = "Integer32"
_CertificateType_Object = MibTableColumn
certificateType = _CertificateType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 2),
    _CertificateType_Type()
)
certificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateType.setStatus("current")


class _CertificateValidityStatus_Type(Integer32):
    """Custom type certificateValidityStatus based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("capUndefined", 0),
          ("capNone", 1),
          ("capOkay", 2),
          ("capIssuerError", 3),
          ("capDateError", 4),
          ("capRevoked", 5),
          ("capSignatureError", 6),
          ("capAttributeError", 7),
          ("capGeneralFail", 8),
          ("capDateExpired", 9),
          ("capDateNotReached", 10),
          ("capIssuerUknown", 11),
          ("capIssuerNotTrusted", 12),
          ("capConstraintsError", 13))
    )


_CertificateValidityStatus_Type.__name__ = "Integer32"
_CertificateValidityStatus_Object = MibTableColumn
certificateValidityStatus = _CertificateValidityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 3),
    _CertificateValidityStatus_Type()
)
certificateValidityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateValidityStatus.setStatus("current")


class _CertificatePurpose_Type(Integer32):
    """Custom type certificatePurpose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("webService", 2))
    )


_CertificatePurpose_Type.__name__ = "Integer32"
_CertificatePurpose_Object = MibTableColumn
certificatePurpose = _CertificatePurpose_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 4),
    _CertificatePurpose_Type()
)
certificatePurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificatePurpose.setStatus("current")


class _CertificateStatus_Type(Integer32):
    """Custom type certificateStatus based on Integer32"""
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
          ("active", 2),
          ("needrenew", 3),
          ("applyerror", 4))
    )


_CertificateStatus_Type.__name__ = "Integer32"
_CertificateStatus_Object = MibTableColumn
certificateStatus = _CertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 5),
    _CertificateStatus_Type()
)
certificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateStatus.setStatus("current")
_CertificateIssuer_Type = SnmpAdminString
_CertificateIssuer_Object = MibTableColumn
certificateIssuer = _CertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 6),
    _CertificateIssuer_Type()
)
certificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateIssuer.setStatus("current")
_CertificateSerialNo_Type = SnmpAdminString
_CertificateSerialNo_Object = MibTableColumn
certificateSerialNo = _CertificateSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 7),
    _CertificateSerialNo_Type()
)
certificateSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSerialNo.setStatus("current")
_CertificateSubject_Type = SnmpAdminString
_CertificateSubject_Object = MibTableColumn
certificateSubject = _CertificateSubject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 8),
    _CertificateSubject_Type()
)
certificateSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSubject.setStatus("current")
_CertificateCommonName_Type = SnmpAdminString
_CertificateCommonName_Object = MibTableColumn
certificateCommonName = _CertificateCommonName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 9),
    _CertificateCommonName_Type()
)
certificateCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateCommonName.setStatus("current")
_CertificateValidFrom_Type = DateAndTime
_CertificateValidFrom_Object = MibTableColumn
certificateValidFrom = _CertificateValidFrom_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 10),
    _CertificateValidFrom_Type()
)
certificateValidFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateValidFrom.setStatus("current")
_CertificateValidTo_Type = DateAndTime
_CertificateValidTo_Object = MibTableColumn
certificateValidTo = _CertificateValidTo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 11),
    _CertificateValidTo_Type()
)
certificateValidTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateValidTo.setStatus("current")


class _CertificateSignAlgorithm_Type(Integer32):
    """Custom type certificateSignAlgorithm based on Integer32"""
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
        *(("undefined", 0),
          ("none", 1),
          ("md5", 2),
          ("sha1", 3),
          ("sha224", 4),
          ("sha256", 5),
          ("sha384", 6),
          ("sha512", 7),
          ("other", 8))
    )


_CertificateSignAlgorithm_Type.__name__ = "Integer32"
_CertificateSignAlgorithm_Object = MibTableColumn
certificateSignAlgorithm = _CertificateSignAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 12),
    _CertificateSignAlgorithm_Type()
)
certificateSignAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSignAlgorithm.setStatus("current")


class _CertificateSha1_Type(OctetString):
    """Custom type certificateSha1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CertificateSha1_Type.__name__ = "OctetString"
_CertificateSha1_Object = MibTableColumn
certificateSha1 = _CertificateSha1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 13),
    _CertificateSha1_Type()
)
certificateSha1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSha1.setStatus("current")


class _CertificateSha256_Type(OctetString):
    """Custom type certificateSha256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CertificateSha256_Type.__name__ = "OctetString"
_CertificateSha256_Object = MibTableColumn
certificateSha256 = _CertificateSha256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 14),
    _CertificateSha256_Type()
)
certificateSha256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateSha256.setStatus("current")
_CertificateAlternativeNameIp_Type = SnmpAdminString
_CertificateAlternativeNameIp_Object = MibTableColumn
certificateAlternativeNameIp = _CertificateAlternativeNameIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 15),
    _CertificateAlternativeNameIp_Type()
)
certificateAlternativeNameIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateAlternativeNameIp.setStatus("current")
_CertificateAlternativeNameDns_Type = SnmpAdminString
_CertificateAlternativeNameDns_Object = MibTableColumn
certificateAlternativeNameDns = _CertificateAlternativeNameDns_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 16),
    _CertificateAlternativeNameDns_Type()
)
certificateAlternativeNameDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateAlternativeNameDns.setStatus("current")
_CertificateKeyUsage_Type = SnmpAdminString
_CertificateKeyUsage_Object = MibTableColumn
certificateKeyUsage = _CertificateKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 17),
    _CertificateKeyUsage_Type()
)
certificateKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateKeyUsage.setStatus("current")
_CertificateExtKeyUsage_Type = SnmpAdminString
_CertificateExtKeyUsage_Object = MibTableColumn
certificateExtKeyUsage = _CertificateExtKeyUsage_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 18),
    _CertificateExtKeyUsage_Type()
)
certificateExtKeyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateExtKeyUsage.setStatus("current")
_CertificateBasicConstraints_Type = SnmpAdminString
_CertificateBasicConstraints_Object = MibTableColumn
certificateBasicConstraints = _CertificateBasicConstraints_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 19),
    _CertificateBasicConstraints_Type()
)
certificateBasicConstraints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateBasicConstraints.setStatus("current")
_CertificateCrlDistrPoints_Type = SnmpAdminString
_CertificateCrlDistrPoints_Object = MibTableColumn
certificateCrlDistrPoints = _CertificateCrlDistrPoints_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 20),
    _CertificateCrlDistrPoints_Type()
)
certificateCrlDistrPoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateCrlDistrPoints.setStatus("current")
_CertificateCaEntity_Type = SnmpAdminString
_CertificateCaEntity_Object = MibTableColumn
certificateCaEntity = _CertificateCaEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 21),
    _CertificateCaEntity_Type()
)
certificateCaEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateCaEntity.setStatus("current")
_CertificateKeyEntity_Type = SnmpAdminString
_CertificateKeyEntity_Object = MibTableColumn
certificateKeyEntity = _CertificateKeyEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 6, 4, 3, 1, 22),
    _CertificateKeyEntity_Type()
)
certificateKeyEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateKeyEntity.setStatus("current")
_EmailNotifySettings_ObjectIdentity = ObjectIdentity
emailNotifySettings = _EmailNotifySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7)
)


class _EmailNotifyConfig_Type(Integer32):
    """Custom type emailNotifyConfig based on Integer32"""
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
        *(("disabled", 1),
          ("enabledMails", 2),
          ("enabledTraps", 3),
          ("enabledMailsAndTraps", 4))
    )


_EmailNotifyConfig_Type.__name__ = "Integer32"
_EmailNotifyConfig_Object = MibScalar
emailNotifyConfig = _EmailNotifyConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 1),
    _EmailNotifyConfig_Type()
)
emailNotifyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailNotifyConfig.setStatus("current")
_SmtpServerName_Type = DisplayString
_SmtpServerName_Object = MibScalar
smtpServerName = _SmtpServerName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 2),
    _SmtpServerName_Type()
)
smtpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerName.setStatus("current")


class _SmtpServerPort_Type(Integer32):
    """Custom type smtpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmtpServerPort_Type.__name__ = "Integer32"
_SmtpServerPort_Object = MibScalar
smtpServerPort = _SmtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 3),
    _SmtpServerPort_Type()
)
smtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerPort.setStatus("current")


class _SmtpServerConnectionSecurity_Type(Integer32):
    """Custom type smtpServerConnectionSecurity based on Integer32"""
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
          ("sslTls", 2),
          ("startTls", 3))
    )


_SmtpServerConnectionSecurity_Type.__name__ = "Integer32"
_SmtpServerConnectionSecurity_Object = MibScalar
smtpServerConnectionSecurity = _SmtpServerConnectionSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 4),
    _SmtpServerConnectionSecurity_Type()
)
smtpServerConnectionSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerConnectionSecurity.setStatus("current")


class _SmtpServerAuthConfig_Type(Integer32):
    """Custom type smtpServerAuthConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("auth", 2))
    )


_SmtpServerAuthConfig_Type.__name__ = "Integer32"
_SmtpServerAuthConfig_Object = MibScalar
smtpServerAuthConfig = _SmtpServerAuthConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 5),
    _SmtpServerAuthConfig_Type()
)
smtpServerAuthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAuthConfig.setStatus("current")


class _SmtpServerAccount_Type(SnmpAdminString):
    """Custom type smtpServerAccount based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SmtpServerAccount_Type.__name__ = "SnmpAdminString"
_SmtpServerAccount_Object = MibScalar
smtpServerAccount = _SmtpServerAccount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 6),
    _SmtpServerAccount_Type()
)
smtpServerAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerAccount.setStatus("current")


class _SmtpServerPasswd_Type(SnmpAdminString):
    """Custom type smtpServerPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SmtpServerPasswd_Type.__name__ = "SnmpAdminString"
_SmtpServerPasswd_Object = MibScalar
smtpServerPasswd = _SmtpServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 7),
    _SmtpServerPasswd_Type()
)
smtpServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpServerPasswd.setStatus("current")
_EmailRecipientTable_Object = MibTable
emailRecipientTable = _EmailRecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8)
)
if mibBuilder.loadTexts:
    emailRecipientTable.setStatus("current")
_EmailRecipientEntry_Object = MibTableRow
emailRecipientEntry = _EmailRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1)
)
emailRecipientEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "emailRecipientId"),
)
if mibBuilder.loadTexts:
    emailRecipientEntry.setStatus("current")


class _EmailRecipientId_Type(Integer32):
    """Custom type emailRecipientId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EmailRecipientId_Type.__name__ = "Integer32"
_EmailRecipientId_Object = MibTableColumn
emailRecipientId = _EmailRecipientId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 1),
    _EmailRecipientId_Type()
)
emailRecipientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emailRecipientId.setStatus("current")
_EmailRecipientAddress_Type = DisplayString
_EmailRecipientAddress_Object = MibTableColumn
emailRecipientAddress = _EmailRecipientAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 2),
    _EmailRecipientAddress_Type()
)
emailRecipientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientAddress.setStatus("current")


class _EmailRecipientType_Type(Integer32):
    """Custom type emailRecipientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("to", 1),
          ("cc", 2),
          ("bcc", 3))
    )


_EmailRecipientType_Type.__name__ = "Integer32"
_EmailRecipientType_Object = MibTableColumn
emailRecipientType = _EmailRecipientType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 3),
    _EmailRecipientType_Type()
)
emailRecipientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientType.setStatus("current")
_EmailRecipientRowStatus_Type = RowStatus
_EmailRecipientRowStatus_Object = MibTableColumn
emailRecipientRowStatus = _EmailRecipientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 4),
    _EmailRecipientRowStatus_Type()
)
emailRecipientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientRowStatus.setStatus("current")


class _EmailRecipientFormat_Type(Integer32):
    """Custom type emailRecipientFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("xml", 1),
          ("text", 2),
          ("longText", 3))
    )


_EmailRecipientFormat_Type.__name__ = "Integer32"
_EmailRecipientFormat_Object = MibTableColumn
emailRecipientFormat = _EmailRecipientFormat_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 5),
    _EmailRecipientFormat_Type()
)
emailRecipientFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientFormat.setStatus("current")


class _EmailRecipientMinSeverity_Type(Integer32):
    """Custom type emailRecipientMinSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("med", 2),
          ("high", 3))
    )


_EmailRecipientMinSeverity_Type.__name__ = "Integer32"
_EmailRecipientMinSeverity_Object = MibTableColumn
emailRecipientMinSeverity = _EmailRecipientMinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 6),
    _EmailRecipientMinSeverity_Type()
)
emailRecipientMinSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientMinSeverity.setStatus("current")


class _EmailRecipientAttachment_Type(Integer32):
    """Custom type emailRecipientAttachment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_EmailRecipientAttachment_Type.__name__ = "Integer32"
_EmailRecipientAttachment_Object = MibTableColumn
emailRecipientAttachment = _EmailRecipientAttachment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 8, 1, 7),
    _EmailRecipientAttachment_Type()
)
emailRecipientAttachment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    emailRecipientAttachment.setStatus("current")
_ExternalIdTable_Object = MibTable
externalIdTable = _ExternalIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 9)
)
if mibBuilder.loadTexts:
    externalIdTable.setStatus("current")
_ExternalIdEntry_Object = MibTableRow
externalIdEntry = _ExternalIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 9, 1)
)
externalIdEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    externalIdEntry.setStatus("current")


class _ExternalId_Type(DisplayString):
    """Custom type externalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExternalId_Type.__name__ = "DisplayString"
_ExternalId_Object = MibTableColumn
externalId = _ExternalId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 9, 1, 1),
    _ExternalId_Type()
)
externalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalId.setStatus("current")
_SmtpSenderAddress_Type = DisplayString
_SmtpSenderAddress_Object = MibScalar
smtpSenderAddress = _SmtpSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 10),
    _SmtpSenderAddress_Type()
)
smtpSenderAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSenderAddress.setStatus("current")
_SmtpExtendedHello_Type = DisplayString
_SmtpExtendedHello_Object = MibScalar
smtpExtendedHello = _SmtpExtendedHello_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 7, 11),
    _SmtpExtendedHello_Type()
)
smtpExtendedHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpExtendedHello.setStatus("current")
_AdvaSecurity_ObjectIdentity = ObjectIdentity
advaSecurity = _AdvaSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8)
)
_AuthTrapUserName_Type = SnmpAdminString
_AuthTrapUserName_Object = MibScalar
authTrapUserName = _AuthTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 1),
    _AuthTrapUserName_Type()
)
authTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapUserName.setStatus("current")
_AuthTrapLctIp_Type = IpAddress
_AuthTrapLctIp_Object = MibScalar
authTrapLctIp = _AuthTrapLctIp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 2),
    _AuthTrapLctIp_Type()
)
authTrapLctIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapLctIp.setStatus("current")


class _AuthTrapStatus_Type(Integer32):
    """Custom type authTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("success", 2),
          ("authenticationError", 3),
          ("sessionError", 4),
          ("logout", 5))
    )


_AuthTrapStatus_Type.__name__ = "Integer32"
_AuthTrapStatus_Object = MibScalar
authTrapStatus = _AuthTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 3),
    _AuthTrapStatus_Type()
)
authTrapStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapStatus.setStatus("current")
_AuthTrapSessionId_Type = SnmpAdminString
_AuthTrapSessionId_Object = MibScalar
authTrapSessionId = _AuthTrapSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 4),
    _AuthTrapSessionId_Type()
)
authTrapSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapSessionId.setStatus("current")


class _AuthTrapProtocol_Type(Integer32):
    """Custom type authTrapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              11)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("ssh", 4),
          ("snmp", 6),
          ("https", 8),
          ("netconf", 11))
    )


_AuthTrapProtocol_Type.__name__ = "Integer32"
_AuthTrapProtocol_Object = MibScalar
authTrapProtocol = _AuthTrapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 5),
    _AuthTrapProtocol_Type()
)
authTrapProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapProtocol.setStatus("current")
_AuthTrapSuccessfulAuthCount_Type = Unsigned32
_AuthTrapSuccessfulAuthCount_Object = MibScalar
authTrapSuccessfulAuthCount = _AuthTrapSuccessfulAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 6),
    _AuthTrapSuccessfulAuthCount_Type()
)
authTrapSuccessfulAuthCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapSuccessfulAuthCount.setStatus("current")
_AuthTrapUnsuccessfulAuthCount_Type = Unsigned32
_AuthTrapUnsuccessfulAuthCount_Object = MibScalar
authTrapUnsuccessfulAuthCount = _AuthTrapUnsuccessfulAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 7),
    _AuthTrapUnsuccessfulAuthCount_Type()
)
authTrapUnsuccessfulAuthCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapUnsuccessfulAuthCount.setStatus("current")
_AuthTrapLogoutCount_Type = Unsigned32
_AuthTrapLogoutCount_Object = MibScalar
authTrapLogoutCount = _AuthTrapLogoutCount_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 8),
    _AuthTrapLogoutCount_Type()
)
authTrapLogoutCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapLogoutCount.setStatus("current")
_AuthTrapLctIpv6_Type = SnmpAdminString
_AuthTrapLctIpv6_Object = MibScalar
authTrapLctIpv6 = _AuthTrapLctIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 8, 9),
    _AuthTrapLctIpv6_Type()
)
authTrapLctIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    authTrapLctIpv6.setStatus("current")
_LossGuidance_ObjectIdentity = ObjectIdentity
lossGuidance = _LossGuidance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9)
)


class _LossGuidanceConfig_Type(Integer32):
    """Custom type lossGuidanceConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LossGuidanceConfig_Type.__name__ = "Integer32"
_LossGuidanceConfig_Object = MibScalar
lossGuidanceConfig = _LossGuidanceConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 1),
    _LossGuidanceConfig_Type()
)
lossGuidanceConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lossGuidanceConfig.setStatus("current")


class _MinLoss_Type(Integer32):
    """Custom type minLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_MinLoss_Type.__name__ = "Integer32"
_MinLoss_Object = MibScalar
minLoss = _MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 2),
    _MinLoss_Type()
)
minLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minLoss.setStatus("current")
if mibBuilder.loadTexts:
    minLoss.setUnits("0.1 dB")


class _AlwDev_Type(Integer32):
    """Custom type alwDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_AlwDev_Type.__name__ = "Integer32"
_AlwDev_Object = MibScalar
alwDev = _AlwDev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 3),
    _AlwDev_Type()
)
alwDev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alwDev.setStatus("current")
if mibBuilder.loadTexts:
    alwDev.setUnits("0.1 dB")


class _LossKm_Type(Integer32):
    """Custom type lossKm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
    )


_LossKm_Type.__name__ = "Integer32"
_LossKm_Object = MibScalar
lossKm = _LossKm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 4),
    _LossKm_Type()
)
lossKm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lossKm.setStatus("current")
if mibBuilder.loadTexts:
    lossKm.setUnits("0.01 dB")


class _LossConnectors_Type(Integer32):
    """Custom type lossConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LossConnectors_Type.__name__ = "Integer32"
_LossConnectors_Object = MibScalar
lossConnectors = _LossConnectors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 5),
    _LossConnectors_Type()
)
lossConnectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lossConnectors.setStatus("current")
if mibBuilder.loadTexts:
    lossConnectors.setUnits("0.1 dB")


class _LossSplices_Type(Integer32):
    """Custom type lossSplices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_LossSplices_Type.__name__ = "Integer32"
_LossSplices_Object = MibScalar
lossSplices = _LossSplices_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 6),
    _LossSplices_Type()
)
lossSplices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lossSplices.setStatus("current")
if mibBuilder.loadTexts:
    lossSplices.setUnits("0.1 dB")


class _NumConnectors_Type(Integer32):
    """Custom type numConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumConnectors_Type.__name__ = "Integer32"
_NumConnectors_Object = MibScalar
numConnectors = _NumConnectors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 7),
    _NumConnectors_Type()
)
numConnectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numConnectors.setStatus("current")


class _NumSplices_Type(Integer32):
    """Custom type numSplices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_NumSplices_Type.__name__ = "Integer32"
_NumSplices_Object = MibScalar
numSplices = _NumSplices_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 9, 8),
    _NumSplices_Type()
)
numSplices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numSplices.setStatus("current")
_UserManagement_ObjectIdentity = ObjectIdentity
userManagement = _UserManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10)
)
_UserManagementTable_Object = MibTable
userManagementTable = _UserManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1)
)
if mibBuilder.loadTexts:
    userManagementTable.setStatus("current")
_UserManagementEntry_Object = MibTableRow
userManagementEntry = _UserManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1)
)
userManagementEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "userManagementUsername"),
)
if mibBuilder.loadTexts:
    userManagementEntry.setStatus("current")
_UserManagementRowStatus_Type = RowStatus
_UserManagementRowStatus_Object = MibTableColumn
userManagementRowStatus = _UserManagementRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 1),
    _UserManagementRowStatus_Type()
)
userManagementRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementRowStatus.setStatus("current")
_UserManagementUsername_Type = SnmpAdminString
_UserManagementUsername_Object = MibTableColumn
userManagementUsername = _UserManagementUsername_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 2),
    _UserManagementUsername_Type()
)
userManagementUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementUsername.setStatus("current")
_UserManagementEmailAddress_Type = SnmpAdminString
_UserManagementEmailAddress_Object = MibTableColumn
userManagementEmailAddress = _UserManagementEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 3),
    _UserManagementEmailAddress_Type()
)
userManagementEmailAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementEmailAddress.setStatus("current")


class _UserManagementPrivilegeLevel_Type(Integer32):
    """Custom type userManagementPrivilegeLevel based on Integer32"""
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
        *(("admin", 1),
          ("operator", 2),
          ("observer", 3),
          ("netadmin", 4))
    )


_UserManagementPrivilegeLevel_Type.__name__ = "Integer32"
_UserManagementPrivilegeLevel_Object = MibTableColumn
userManagementPrivilegeLevel = _UserManagementPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 4),
    _UserManagementPrivilegeLevel_Type()
)
userManagementPrivilegeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementPrivilegeLevel.setStatus("current")


class _UserManagementSecurityLevel_Type(Integer32):
    """Custom type userManagementSecurityLevel based on Integer32"""
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
        *(("undefined", 0),
          ("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_UserManagementSecurityLevel_Type.__name__ = "Integer32"
_UserManagementSecurityLevel_Object = MibTableColumn
userManagementSecurityLevel = _UserManagementSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 5),
    _UserManagementSecurityLevel_Type()
)
userManagementSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementSecurityLevel.setStatus("current")
_UserManagementAuthPrivKey_Type = SnmpAdminString
_UserManagementAuthPrivKey_Object = MibTableColumn
userManagementAuthPrivKey = _UserManagementAuthPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 6),
    _UserManagementAuthPrivKey_Type()
)
userManagementAuthPrivKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementAuthPrivKey.setStatus("current")
_UserManagementAuthPrivKeyOld_Type = SnmpAdminString
_UserManagementAuthPrivKeyOld_Object = MibTableColumn
userManagementAuthPrivKeyOld = _UserManagementAuthPrivKeyOld_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 7),
    _UserManagementAuthPrivKeyOld_Type()
)
userManagementAuthPrivKeyOld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementAuthPrivKeyOld.setStatus("current")


class _UserManagementUdpSessionStatus_Type(Integer32):
    """Custom type userManagementUdpSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("active", 1),
          ("inactive", 2))
    )


_UserManagementUdpSessionStatus_Type.__name__ = "Integer32"
_UserManagementUdpSessionStatus_Object = MibTableColumn
userManagementUdpSessionStatus = _UserManagementUdpSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 8),
    _UserManagementUdpSessionStatus_Type()
)
userManagementUdpSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userManagementUdpSessionStatus.setStatus("current")


class _UserManagementSso2fa_Type(Integer32):
    """Custom type userManagementSso2fa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_UserManagementSso2fa_Type.__name__ = "Integer32"
_UserManagementSso2fa_Object = MibTableColumn
userManagementSso2fa = _UserManagementSso2fa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 9),
    _UserManagementSso2fa_Type()
)
userManagementSso2fa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementSso2fa.setStatus("current")


class _UserManagementSnmpAuthProtocol_Type(Integer32):
    """Custom type userManagementSnmpAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha256", 2),
          ("sha512", 3))
    )


_UserManagementSnmpAuthProtocol_Type.__name__ = "Integer32"
_UserManagementSnmpAuthProtocol_Object = MibTableColumn
userManagementSnmpAuthProtocol = _UserManagementSnmpAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 10),
    _UserManagementSnmpAuthProtocol_Type()
)
userManagementSnmpAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementSnmpAuthProtocol.setStatus("current")


class _UserManagementPrivacyKeyType_Type(Integer32):
    """Custom type userManagementPrivacyKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authkey", 1),
          ("userdefined", 2))
    )


_UserManagementPrivacyKeyType_Type.__name__ = "Integer32"
_UserManagementPrivacyKeyType_Object = MibTableColumn
userManagementPrivacyKeyType = _UserManagementPrivacyKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 11),
    _UserManagementPrivacyKeyType_Type()
)
userManagementPrivacyKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementPrivacyKeyType.setStatus("current")
_UserManagementPrivacyKey_Type = SnmpAdminString
_UserManagementPrivacyKey_Object = MibTableColumn
userManagementPrivacyKey = _UserManagementPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 10, 1, 1, 12),
    _UserManagementPrivacyKey_Type()
)
userManagementPrivacyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    userManagementPrivacyKey.setStatus("current")
_ExportMgmt_ObjectIdentity = ObjectIdentity
exportMgmt = _ExportMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11)
)


class _ExportMgmtRequest_Type(Integer32):
    """Custom type exportMgmtRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("exportAllLogs", 2))
    )


_ExportMgmtRequest_Type.__name__ = "Integer32"
_ExportMgmtRequest_Object = MibScalar
exportMgmtRequest = _ExportMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 1),
    _ExportMgmtRequest_Type()
)
exportMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtRequest.setStatus("current")


class _ExportMgmtState_Type(Integer32):
    """Custom type exportMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("exporting", 2),
          ("failure", 7))
    )


_ExportMgmtState_Type.__name__ = "Integer32"
_ExportMgmtState_Object = MibScalar
exportMgmtState = _ExportMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 2),
    _ExportMgmtState_Type()
)
exportMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exportMgmtState.setStatus("current")


class _ExportMgmtLastError_Type(Integer32):
    """Custom type exportMgmtLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("transferLoginFailed", 2),
          ("transferFileNotFound", 3),
          ("transferFileNoAccess", 4),
          ("transferServerUnreachable", 5),
          ("transferFailed", 6),
          ("internalError", 10))
    )


_ExportMgmtLastError_Type.__name__ = "Integer32"
_ExportMgmtLastError_Object = MibScalar
exportMgmtLastError = _ExportMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 3),
    _ExportMgmtLastError_Type()
)
exportMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exportMgmtLastError.setStatus("current")
_ExportMgmtServerAddress_Type = IpAddress
_ExportMgmtServerAddress_Object = MibScalar
exportMgmtServerAddress = _ExportMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 4),
    _ExportMgmtServerAddress_Type()
)
exportMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtServerAddress.setStatus("current")
_ExportMgmtServerLogin_Type = SnmpAdminString
_ExportMgmtServerLogin_Object = MibScalar
exportMgmtServerLogin = _ExportMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 5),
    _ExportMgmtServerLogin_Type()
)
exportMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtServerLogin.setStatus("current")
_ExportMgmtServerPasswd_Type = SnmpAdminString
_ExportMgmtServerPasswd_Object = MibScalar
exportMgmtServerPasswd = _ExportMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 6),
    _ExportMgmtServerPasswd_Type()
)
exportMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtServerPasswd.setStatus("current")
_ExportMgmtServerDirectory_Type = SnmpAdminString
_ExportMgmtServerDirectory_Object = MibScalar
exportMgmtServerDirectory = _ExportMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 7),
    _ExportMgmtServerDirectory_Type()
)
exportMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtServerDirectory.setStatus("current")
_ExportMgmtFileName_Type = SnmpAdminString
_ExportMgmtFileName_Object = MibScalar
exportMgmtFileName = _ExportMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 8),
    _ExportMgmtFileName_Type()
)
exportMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtFileName.setStatus("current")


class _ExportMgmtTransferProtocol_Type(Integer32):
    """Custom type exportMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_ExportMgmtTransferProtocol_Type.__name__ = "Integer32"
_ExportMgmtTransferProtocol_Object = MibScalar
exportMgmtTransferProtocol = _ExportMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 9),
    _ExportMgmtTransferProtocol_Type()
)
exportMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtTransferProtocol.setStatus("current")


class _ExportMgmtFtpPort_Type(Integer32):
    """Custom type exportMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExportMgmtFtpPort_Type.__name__ = "Integer32"
_ExportMgmtFtpPort_Object = MibScalar
exportMgmtFtpPort = _ExportMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 10),
    _ExportMgmtFtpPort_Type()
)
exportMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtFtpPort.setStatus("current")


class _ExportMgmtActionProgress_Type(Integer32):
    """Custom type exportMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_ExportMgmtActionProgress_Type.__name__ = "Integer32"
_ExportMgmtActionProgress_Object = MibScalar
exportMgmtActionProgress = _ExportMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 11),
    _ExportMgmtActionProgress_Type()
)
exportMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exportMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    exportMgmtActionProgress.setUnits("%")
_ExportMgmtIpv6Address_Type = SnmpAdminString
_ExportMgmtIpv6Address_Object = MibScalar
exportMgmtIpv6Address = _ExportMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 12),
    _ExportMgmtIpv6Address_Type()
)
exportMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtIpv6Address.setStatus("current")


class _ExportMgmtScpPort_Type(Integer32):
    """Custom type exportMgmtScpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExportMgmtScpPort_Type.__name__ = "Integer32"
_ExportMgmtScpPort_Object = MibScalar
exportMgmtScpPort = _ExportMgmtScpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 11, 13),
    _ExportMgmtScpPort_Type()
)
exportMgmtScpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exportMgmtScpPort.setStatus("current")
_BidirSettings_ObjectIdentity = ObjectIdentity
bidirSettings = _BidirSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 12)
)


class _BidirSettingsTimeSlotConfig_Type(Integer32):
    """Custom type bidirSettingsTimeSlotConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              21,
              22,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("none", 11),
          ("numSlots2unitSlot1", 21),
          ("numSlots2unitSlot2", 22),
          ("numSlots3unitSlot1", 31),
          ("numSlots3unitSlot2", 32),
          ("numSlots3unitSlot3", 33))
    )


_BidirSettingsTimeSlotConfig_Type.__name__ = "Integer32"
_BidirSettingsTimeSlotConfig_Object = MibScalar
bidirSettingsTimeSlotConfig = _BidirSettingsTimeSlotConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 12, 1),
    _BidirSettingsTimeSlotConfig_Type()
)
bidirSettingsTimeSlotConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bidirSettingsTimeSlotConfig.setStatus("current")


class _BidirSettingsInactiveUserCmds_Type(Integer32):
    """Custom type bidirSettingsInactiveUserCmds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BidirSettingsInactiveUserCmds_Type.__name__ = "Integer32"
_BidirSettingsInactiveUserCmds_Object = MibScalar
bidirSettingsInactiveUserCmds = _BidirSettingsInactiveUserCmds_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 12, 2),
    _BidirSettingsInactiveUserCmds_Type()
)
bidirSettingsInactiveUserCmds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bidirSettingsInactiveUserCmds.setStatus("current")


class _DwdmExtraWaitTimeSlot_Type(Integer32):
    """Custom type dwdmExtraWaitTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DwdmExtraWaitTimeSlot_Type.__name__ = "Integer32"
_DwdmExtraWaitTimeSlot_Object = MibScalar
dwdmExtraWaitTimeSlot = _DwdmExtraWaitTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 12, 3),
    _DwdmExtraWaitTimeSlot_Type()
)
dwdmExtraWaitTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dwdmExtraWaitTimeSlot.setStatus("current")
_RemoteAuth_ObjectIdentity = ObjectIdentity
remoteAuth = _RemoteAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13)
)


class _Authmode_Type(Integer32):
    """Custom type authmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_Authmode_Type.__name__ = "Integer32"
_Authmode_Object = MibScalar
authmode = _Authmode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 1),
    _Authmode_Type()
)
authmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authmode.setStatus("current")


class _Loginmode_Type(Integer32):
    """Custom type loginmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pap", 1),
          ("chap", 2))
    )


_Loginmode_Type.__name__ = "Integer32"
_Loginmode_Object = MibScalar
loginmode = _Loginmode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 2),
    _Loginmode_Type()
)
loginmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginmode.setStatus("current")


class _Sso2fa_Type(Integer32):
    """Custom type sso2fa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Sso2fa_Type.__name__ = "Integer32"
_Sso2fa_Object = MibScalar
sso2fa = _Sso2fa_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 3),
    _Sso2fa_Type()
)
sso2fa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sso2fa.setStatus("current")
_RemoteAuthServersTable_Object = MibTable
remoteAuthServersTable = _RemoteAuthServersTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4)
)
if mibBuilder.loadTexts:
    remoteAuthServersTable.setStatus("current")
_RemoteAuthServersEntry_Object = MibTableRow
remoteAuthServersEntry = _RemoteAuthServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1)
)
remoteAuthServersEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "remoteAuthServersId"),
)
if mibBuilder.loadTexts:
    remoteAuthServersEntry.setStatus("current")


class _RemoteAuthServersId_Type(Integer32):
    """Custom type remoteAuthServersId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RemoteAuthServersId_Type.__name__ = "Integer32"
_RemoteAuthServersId_Object = MibTableColumn
remoteAuthServersId = _RemoteAuthServersId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 1),
    _RemoteAuthServersId_Type()
)
remoteAuthServersId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteAuthServersId.setStatus("current")
_RemoteAuthServersIpAddress_Type = DisplayString
_RemoteAuthServersIpAddress_Object = MibTableColumn
remoteAuthServersIpAddress = _RemoteAuthServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 2),
    _RemoteAuthServersIpAddress_Type()
)
remoteAuthServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAuthServersIpAddress.setStatus("current")


class _RemoteAuthServersPort_Type(Integer32):
    """Custom type remoteAuthServersPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RemoteAuthServersPort_Type.__name__ = "Integer32"
_RemoteAuthServersPort_Object = MibTableColumn
remoteAuthServersPort = _RemoteAuthServersPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 3),
    _RemoteAuthServersPort_Type()
)
remoteAuthServersPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAuthServersPort.setStatus("current")
_RemoteAuthServersSecret_Type = DisplayString
_RemoteAuthServersSecret_Object = MibTableColumn
remoteAuthServersSecret = _RemoteAuthServersSecret_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 4),
    _RemoteAuthServersSecret_Type()
)
remoteAuthServersSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAuthServersSecret.setStatus("current")


class _RemoteAuthServersTimeout_Type(Integer32):
    """Custom type remoteAuthServersTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RemoteAuthServersTimeout_Type.__name__ = "Integer32"
_RemoteAuthServersTimeout_Object = MibTableColumn
remoteAuthServersTimeout = _RemoteAuthServersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 5),
    _RemoteAuthServersTimeout_Type()
)
remoteAuthServersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAuthServersTimeout.setStatus("current")
if mibBuilder.loadTexts:
    remoteAuthServersTimeout.setUnits("s")


class _RemoteAuthServersActive_Type(Integer32):
    """Custom type remoteAuthServersActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RemoteAuthServersActive_Type.__name__ = "Integer32"
_RemoteAuthServersActive_Object = MibTableColumn
remoteAuthServersActive = _RemoteAuthServersActive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 13, 4, 1, 6),
    _RemoteAuthServersActive_Type()
)
remoteAuthServersActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteAuthServersActive.setStatus("current")
_PrioSettings_ObjectIdentity = ObjectIdentity
prioSettings = _PrioSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 14)
)


class _PrioSettingsConfig_Type(Integer32):
    """Custom type prioSettingsConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PrioSettingsConfig_Type.__name__ = "Integer32"
_PrioSettingsConfig_Object = MibScalar
prioSettingsConfig = _PrioSettingsConfig_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 5, 14, 1),
    _PrioSettingsConfig_Type()
)
prioSettingsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioSettingsConfig.setStatus("current")
_Maintain_ObjectIdentity = ObjectIdentity
maintain = _Maintain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6)
)
_MaintainTable_Object = MibTable
maintainTable = _MaintainTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1)
)
if mibBuilder.loadTexts:
    maintainTable.setStatus("current")
_MaintainEntry_Object = MibTableRow
maintainEntry = _MaintainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1)
)
maintainEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    maintainEntry.setStatus("current")


class _MaintainOperationRequest_Type(Integer32):
    """Custom type maintainOperationRequest based on Integer32"""
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
        *(("none", 1),
          ("runFingerprintGeneration", 2),
          ("runOtdrMeasurement", 3),
          ("runFaultAnalysis", 4),
          ("runFingerprintGpon", 5),
          ("runFingerprintWithoutReflector", 6),
          ("runResetMeanValues", 7),
          ("runFingerprintPes", 8),
          ("runLossCalculationPointUpdate", 9),
          ("runFiberIdentification", 10),
          ("runFingerprintAdl", 11),
          ("runFingerprintDpa", 12))
    )


_MaintainOperationRequest_Type.__name__ = "Integer32"
_MaintainOperationRequest_Object = MibTableColumn
maintainOperationRequest = _MaintainOperationRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 1),
    _MaintainOperationRequest_Type()
)
maintainOperationRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationRequest.setStatus("current")


class _MaintainOperationRefractiveIndex_Type(Integer32):
    """Custom type maintainOperationRefractiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1550000),
    )


_MaintainOperationRefractiveIndex_Type.__name__ = "Integer32"
_MaintainOperationRefractiveIndex_Object = MibTableColumn
maintainOperationRefractiveIndex = _MaintainOperationRefractiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 2),
    _MaintainOperationRefractiveIndex_Type()
)
maintainOperationRefractiveIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationRefractiveIndex.setStatus("current")


class _MaintainOperationExternalOffset_Type(Integer32):
    """Custom type maintainOperationExternalOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaintainOperationExternalOffset_Type.__name__ = "Integer32"
_MaintainOperationExternalOffset_Object = MibTableColumn
maintainOperationExternalOffset = _MaintainOperationExternalOffset_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 3),
    _MaintainOperationExternalOffset_Type()
)
maintainOperationExternalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationExternalOffset.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationExternalOffset.setUnits("m")


class _MaintainOperationCouplerLoss_Type(Integer32):
    """Custom type maintainOperationCouplerLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaintainOperationCouplerLoss_Type.__name__ = "Integer32"
_MaintainOperationCouplerLoss_Object = MibTableColumn
maintainOperationCouplerLoss = _MaintainOperationCouplerLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 4),
    _MaintainOperationCouplerLoss_Type()
)
maintainOperationCouplerLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationCouplerLoss.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationCouplerLoss.setUnits("0.1 dB")


class _MaintainOperationOtdrLength_Type(Integer32):
    """Custom type maintainOperationOtdrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200000),
    )


_MaintainOperationOtdrLength_Type.__name__ = "Integer32"
_MaintainOperationOtdrLength_Object = MibTableColumn
maintainOperationOtdrLength = _MaintainOperationOtdrLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 5),
    _MaintainOperationOtdrLength_Type()
)
maintainOperationOtdrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrLength.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationOtdrLength.setUnits("m")


class _MaintainOperationOtdrPowerLevel_Type(Integer32):
    """Custom type maintainOperationOtdrPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_MaintainOperationOtdrPowerLevel_Type.__name__ = "Integer32"
_MaintainOperationOtdrPowerLevel_Object = MibTableColumn
maintainOperationOtdrPowerLevel = _MaintainOperationOtdrPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 6),
    _MaintainOperationOtdrPowerLevel_Type()
)
maintainOperationOtdrPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationOtdrPowerLevel.setUnits("0.01 dBm")


class _MaintainOperationOtdrPulseWidth_Type(Integer32):
    """Custom type maintainOperationOtdrPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20000),
    )


_MaintainOperationOtdrPulseWidth_Type.__name__ = "Integer32"
_MaintainOperationOtdrPulseWidth_Object = MibTableColumn
maintainOperationOtdrPulseWidth = _MaintainOperationOtdrPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 7),
    _MaintainOperationOtdrPulseWidth_Type()
)
maintainOperationOtdrPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationOtdrPulseWidth.setUnits("ns")


class _MaintainOperationOtdrAverageRate_Type(Integer32):
    """Custom type maintainOperationOtdrAverageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MaintainOperationOtdrAverageRate_Type.__name__ = "Integer32"
_MaintainOperationOtdrAverageRate_Object = MibTableColumn
maintainOperationOtdrAverageRate = _MaintainOperationOtdrAverageRate_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 8),
    _MaintainOperationOtdrAverageRate_Type()
)
maintainOperationOtdrAverageRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrAverageRate.setStatus("current")


class _MaintainOperationState_Type(Integer32):
    """Custom type maintainOperationState based on Integer32"""
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
        *(("idle", 1),
          ("waiting", 2),
          ("fingerprintGenerationRunning", 3),
          ("otdrMeasurementRunning", 4),
          ("faultAnalysisRunning", 5),
          ("failure", 6))
    )


_MaintainOperationState_Type.__name__ = "Integer32"
_MaintainOperationState_Object = MibTableColumn
maintainOperationState = _MaintainOperationState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 9),
    _MaintainOperationState_Type()
)
maintainOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintainOperationState.setStatus("current")


class _MaintainOperationLastError_Type(Integer32):
    """Custom type maintainOperationLastError based on Integer32"""
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
        *(("noError", 1),
          ("reflectionPointNotFound", 2),
          ("noSpaceLeft", 3),
          ("internalError", 4),
          ("lossCalculationPointNotFound", 5),
          ("deprecatedFingerprintVersion", 6))
    )


_MaintainOperationLastError_Type.__name__ = "Integer32"
_MaintainOperationLastError_Object = MibTableColumn
maintainOperationLastError = _MaintainOperationLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 10),
    _MaintainOperationLastError_Type()
)
maintainOperationLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintainOperationLastError.setStatus("current")


class _MaintainOperationNumConnectors_Type(Integer32):
    """Custom type maintainOperationNumConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MaintainOperationNumConnectors_Type.__name__ = "Integer32"
_MaintainOperationNumConnectors_Object = MibTableColumn
maintainOperationNumConnectors = _MaintainOperationNumConnectors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 11),
    _MaintainOperationNumConnectors_Type()
)
maintainOperationNumConnectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationNumConnectors.setStatus("current")


class _MaintainOperationNumSplices_Type(Integer32):
    """Custom type maintainOperationNumSplices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MaintainOperationNumSplices_Type.__name__ = "Integer32"
_MaintainOperationNumSplices_Object = MibTableColumn
maintainOperationNumSplices = _MaintainOperationNumSplices_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 12),
    _MaintainOperationNumSplices_Type()
)
maintainOperationNumSplices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationNumSplices.setStatus("current")


class _MaintainOperationMaxLaserPower_Type(Integer32):
    """Custom type maintainOperationMaxLaserPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1500),
    )


_MaintainOperationMaxLaserPower_Type.__name__ = "Integer32"
_MaintainOperationMaxLaserPower_Object = MibTableColumn
maintainOperationMaxLaserPower = _MaintainOperationMaxLaserPower_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 13),
    _MaintainOperationMaxLaserPower_Type()
)
maintainOperationMaxLaserPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationMaxLaserPower.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationMaxLaserPower.setUnits("0.01 dBm")


class _MaintainOperationOtdrLinkLength_Type(Integer32):
    """Custom type maintainOperationOtdrLinkLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300000),
    )


_MaintainOperationOtdrLinkLength_Type.__name__ = "Integer32"
_MaintainOperationOtdrLinkLength_Object = MibTableColumn
maintainOperationOtdrLinkLength = _MaintainOperationOtdrLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 14),
    _MaintainOperationOtdrLinkLength_Type()
)
maintainOperationOtdrLinkLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrLinkLength.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationOtdrLinkLength.setUnits("m")


class _MaintainOperationOtdrMeasTime_Type(Integer32):
    """Custom type maintainOperationOtdrMeasTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_MaintainOperationOtdrMeasTime_Type.__name__ = "Integer32"
_MaintainOperationOtdrMeasTime_Object = MibTableColumn
maintainOperationOtdrMeasTime = _MaintainOperationOtdrMeasTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 15),
    _MaintainOperationOtdrMeasTime_Type()
)
maintainOperationOtdrMeasTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationOtdrMeasTime.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationOtdrMeasTime.setUnits("s")


class _MaintainOperationDwdmMode_Type(Integer32):
    """Custom type maintainOperationDwdmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MaintainOperationDwdmMode_Type.__name__ = "Integer32"
_MaintainOperationDwdmMode_Object = MibTableColumn
maintainOperationDwdmMode = _MaintainOperationDwdmMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 16),
    _MaintainOperationDwdmMode_Type()
)
maintainOperationDwdmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationDwdmMode.setStatus("current")


class _MaintainOperationLossCalculationPoint_Type(Integer32):
    """Custom type maintainOperationLossCalculationPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 150000),
        ValueRangeConstraint(0, 0),
    )


_MaintainOperationLossCalculationPoint_Type.__name__ = "Integer32"
_MaintainOperationLossCalculationPoint_Object = MibTableColumn
maintainOperationLossCalculationPoint = _MaintainOperationLossCalculationPoint_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 17),
    _MaintainOperationLossCalculationPoint_Type()
)
maintainOperationLossCalculationPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationLossCalculationPoint.setStatus("current")
if mibBuilder.loadTexts:
    maintainOperationLossCalculationPoint.setUnits("m")


class _MaintainOperationFastMode_Type(Integer32):
    """Custom type maintainOperationFastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MaintainOperationFastMode_Type.__name__ = "Integer32"
_MaintainOperationFastMode_Object = MibTableColumn
maintainOperationFastMode = _MaintainOperationFastMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 18),
    _MaintainOperationFastMode_Type()
)
maintainOperationFastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationFastMode.setStatus("current")


class _MaintainOperationMonitoringMode_Type(Integer32):
    """Custom type maintainOperationMonitoringMode based on Integer32"""
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
        *(("lossCalculation", 1),
          ("trafficCheck", 2),
          ("standard", 3),
          ("highDynamic", 4),
          ("highResolution", 5),
          ("fiberIdentFrequency270", 6),
          ("fiberIdentFrequency330", 7),
          ("fiberIdentFrequency1000", 8),
          ("fiberIdentFrequency2000", 9),
          ("cabinetSensorShort", 10),
          ("cabinetSensorLong", 11),
          ("dpaFast", 12),
          ("dpaBalanced", 13),
          ("dpaHighSensitivity", 14))
    )


_MaintainOperationMonitoringMode_Type.__name__ = "Integer32"
_MaintainOperationMonitoringMode_Object = MibTableColumn
maintainOperationMonitoringMode = _MaintainOperationMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 19),
    _MaintainOperationMonitoringMode_Type()
)
maintainOperationMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationMonitoringMode.setStatus("current")


class _MaintainOperationExpectedLoss_Type(Integer32):
    """Custom type maintainOperationExpectedLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 350),
        ValueRangeConstraint(0, 0),
    )


_MaintainOperationExpectedLoss_Type.__name__ = "Integer32"
_MaintainOperationExpectedLoss_Object = MibTableColumn
maintainOperationExpectedLoss = _MaintainOperationExpectedLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 1, 1, 20),
    _MaintainOperationExpectedLoss_Type()
)
maintainOperationExpectedLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintainOperationExpectedLoss.setStatus("current")
_ScheduleFaTable_Object = MibTable
scheduleFaTable = _ScheduleFaTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2)
)
if mibBuilder.loadTexts:
    scheduleFaTable.setStatus("current")
_ScheduleFaEntry_Object = MibTableRow
scheduleFaEntry = _ScheduleFaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1)
)
scheduleFaEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    scheduleFaEntry.setStatus("current")
_ScheduleFaFirstRun_Type = DateAndTime
_ScheduleFaFirstRun_Object = MibTableColumn
scheduleFaFirstRun = _ScheduleFaFirstRun_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 1),
    _ScheduleFaFirstRun_Type()
)
scheduleFaFirstRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleFaFirstRun.setStatus("current")


class _ScheduleFaInterval_Type(Integer32):
    """Custom type scheduleFaInterval based on Integer32"""
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
        *(("disabled", 0),
          ("twoHours", 1),
          ("threeHours", 2),
          ("fourHours", 3),
          ("sixHours", 4),
          ("eightHours", 5),
          ("twelveHours", 6),
          ("oneDay", 7),
          ("twoDays", 8),
          ("sevenDays", 9))
    )


_ScheduleFaInterval_Type.__name__ = "Integer32"
_ScheduleFaInterval_Object = MibTableColumn
scheduleFaInterval = _ScheduleFaInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 2),
    _ScheduleFaInterval_Type()
)
scheduleFaInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleFaInterval.setStatus("current")


class _ScheduleFaRequiredState_Type(Integer32):
    """Custom type scheduleFaRequiredState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("inServiceOrManagement", 2))
    )


_ScheduleFaRequiredState_Type.__name__ = "Integer32"
_ScheduleFaRequiredState_Object = MibTableColumn
scheduleFaRequiredState = _ScheduleFaRequiredState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 3),
    _ScheduleFaRequiredState_Type()
)
scheduleFaRequiredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleFaRequiredState.setStatus("current")
_ScheduleFaNextRun_Type = DateAndTime
_ScheduleFaNextRun_Object = MibTableColumn
scheduleFaNextRun = _ScheduleFaNextRun_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 4),
    _ScheduleFaNextRun_Type()
)
scheduleFaNextRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduleFaNextRun.setStatus("current")
_ScheduleFaLastRun_Type = DateAndTime
_ScheduleFaLastRun_Object = MibTableColumn
scheduleFaLastRun = _ScheduleFaLastRun_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 5),
    _ScheduleFaLastRun_Type()
)
scheduleFaLastRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduleFaLastRun.setStatus("current")


class _ScheduleFaStatus_Type(Integer32):
    """Custom type scheduleFaStatus based on Integer32"""
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
        *(("disabled", 0),
          ("idle", 1),
          ("queued", 2),
          ("running", 3),
          ("finished", 4),
          ("error", 5))
    )


_ScheduleFaStatus_Type.__name__ = "Integer32"
_ScheduleFaStatus_Object = MibTableColumn
scheduleFaStatus = _ScheduleFaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 6, 2, 1, 6),
    _ScheduleFaStatus_Type()
)
scheduleFaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduleFaStatus.setStatus("current")
_OtdrTraceMgmt_ObjectIdentity = ObjectIdentity
otdrTraceMgmt = _OtdrTraceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7)
)
_OtdrTraceMgmtTable_Object = MibTable
otdrTraceMgmtTable = _OtdrTraceMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1)
)
if mibBuilder.loadTexts:
    otdrTraceMgmtTable.setStatus("current")
_OtdrTraceMgmtEntry_Object = MibTableRow
otdrTraceMgmtEntry = _OtdrTraceMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1)
)
otdrTraceMgmtEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "portId"),
)
if mibBuilder.loadTexts:
    otdrTraceMgmtEntry.setStatus("current")


class _OtdrTraceMgmtRequest_Type(Integer32):
    """Custom type otdrTraceMgmtRequest based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("exportOmTrace", 2),
          ("exportFaTrace", 3),
          ("exportFpTrace", 4),
          ("exportAutoFaTrace", 5),
          ("exportOmTraceFiltered", 6),
          ("exportFaTraceFiltered", 7),
          ("exportFpTraceFiltered", 8),
          ("exportAutoFaTraceFiltered", 9),
          ("exportOmSor", 10),
          ("exportFaSor", 11),
          ("exportFpSor", 12),
          ("exportAutoFaSor", 13),
          ("exportOmSorFiltered", 14),
          ("exportFaSorFiltered", 15),
          ("exportFpSorFiltered", 16),
          ("exportAutoFaSorFiltered", 17),
          ("exportFaSorFilteredLow", 18),
          ("exportFaSorFilteredHigh", 19),
          ("exportFpSorFilteredLow", 20),
          ("exportFpSorFilteredHigh", 21),
          ("exportAutoFaSorFilteredLow", 22),
          ("exportAutoFaSorFilteredHigh", 23))
    )


_OtdrTraceMgmtRequest_Type.__name__ = "Integer32"
_OtdrTraceMgmtRequest_Object = MibTableColumn
otdrTraceMgmtRequest = _OtdrTraceMgmtRequest_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 1),
    _OtdrTraceMgmtRequest_Type()
)
otdrTraceMgmtRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtRequest.setStatus("current")


class _OtdrTraceMgmtState_Type(Integer32):
    """Custom type otdrTraceMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("exportingAutoFaTrace", 4),
          ("exportingOmTrace", 5),
          ("exportingFaTrace", 6),
          ("exportingFpTrace", 7),
          ("failure", 8))
    )


_OtdrTraceMgmtState_Type.__name__ = "Integer32"
_OtdrTraceMgmtState_Object = MibTableColumn
otdrTraceMgmtState = _OtdrTraceMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 2),
    _OtdrTraceMgmtState_Type()
)
otdrTraceMgmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtState.setStatus("current")


class _OtdrTraceMgmtLastError_Type(Integer32):
    """Custom type otdrTraceMgmtLastError based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("transferLoginFailed", 2),
          ("transferFileNotFound", 3),
          ("transferFileNoAccess", 4),
          ("transferServerUnreachable", 5),
          ("transferFailed", 6),
          ("missingOtdrTrace", 7),
          ("wrongOtdrTraceIndex", 8),
          ("internalError", 9),
          ("noSpaceLeft", 10))
    )


_OtdrTraceMgmtLastError_Type.__name__ = "Integer32"
_OtdrTraceMgmtLastError_Object = MibTableColumn
otdrTraceMgmtLastError = _OtdrTraceMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 3),
    _OtdrTraceMgmtLastError_Type()
)
otdrTraceMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtLastError.setStatus("current")
_OtdrTraceMgmtServerAddress_Type = IpAddress
_OtdrTraceMgmtServerAddress_Object = MibTableColumn
otdrTraceMgmtServerAddress = _OtdrTraceMgmtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 4),
    _OtdrTraceMgmtServerAddress_Type()
)
otdrTraceMgmtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerAddress.setStatus("current")
_OtdrTraceMgmtServerLogin_Type = SnmpAdminString
_OtdrTraceMgmtServerLogin_Object = MibTableColumn
otdrTraceMgmtServerLogin = _OtdrTraceMgmtServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 5),
    _OtdrTraceMgmtServerLogin_Type()
)
otdrTraceMgmtServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerLogin.setStatus("current")
_OtdrTraceMgmtServerPasswd_Type = SnmpAdminString
_OtdrTraceMgmtServerPasswd_Object = MibTableColumn
otdrTraceMgmtServerPasswd = _OtdrTraceMgmtServerPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 6),
    _OtdrTraceMgmtServerPasswd_Type()
)
otdrTraceMgmtServerPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerPasswd.setStatus("current")
_OtdrTraceMgmtServerDirectory_Type = SnmpAdminString
_OtdrTraceMgmtServerDirectory_Object = MibTableColumn
otdrTraceMgmtServerDirectory = _OtdrTraceMgmtServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 7),
    _OtdrTraceMgmtServerDirectory_Type()
)
otdrTraceMgmtServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtServerDirectory.setStatus("current")
_OtdrTraceMgmtFileName_Type = SnmpAdminString
_OtdrTraceMgmtFileName_Object = MibTableColumn
otdrTraceMgmtFileName = _OtdrTraceMgmtFileName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 8),
    _OtdrTraceMgmtFileName_Type()
)
otdrTraceMgmtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtFileName.setStatus("current")


class _OtdrTraceMgmtTransferProtocol_Type(Integer32):
    """Custom type otdrTraceMgmtTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 2))
    )


_OtdrTraceMgmtTransferProtocol_Type.__name__ = "Integer32"
_OtdrTraceMgmtTransferProtocol_Object = MibTableColumn
otdrTraceMgmtTransferProtocol = _OtdrTraceMgmtTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 9),
    _OtdrTraceMgmtTransferProtocol_Type()
)
otdrTraceMgmtTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtTransferProtocol.setStatus("current")


class _OtdrTraceMgmtFtpPort_Type(Integer32):
    """Custom type otdrTraceMgmtFtpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OtdrTraceMgmtFtpPort_Type.__name__ = "Integer32"
_OtdrTraceMgmtFtpPort_Object = MibTableColumn
otdrTraceMgmtFtpPort = _OtdrTraceMgmtFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 10),
    _OtdrTraceMgmtFtpPort_Type()
)
otdrTraceMgmtFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtFtpPort.setStatus("current")


class _OtdrTraceMgmtActionProgress_Type(Integer32):
    """Custom type otdrTraceMgmtActionProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_OtdrTraceMgmtActionProgress_Type.__name__ = "Integer32"
_OtdrTraceMgmtActionProgress_Object = MibTableColumn
otdrTraceMgmtActionProgress = _OtdrTraceMgmtActionProgress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 11),
    _OtdrTraceMgmtActionProgress_Type()
)
otdrTraceMgmtActionProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTraceMgmtActionProgress.setStatus("current")
if mibBuilder.loadTexts:
    otdrTraceMgmtActionProgress.setUnits("%")


class _OtdrTraceMgmtAutoFaReference_Type(Integer32):
    """Custom type otdrTraceMgmtAutoFaReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OtdrTraceMgmtAutoFaReference_Type.__name__ = "Integer32"
_OtdrTraceMgmtAutoFaReference_Object = MibTableColumn
otdrTraceMgmtAutoFaReference = _OtdrTraceMgmtAutoFaReference_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 12),
    _OtdrTraceMgmtAutoFaReference_Type()
)
otdrTraceMgmtAutoFaReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtAutoFaReference.setStatus("current")
_OtdrTraceMgmtIpv6Address_Type = SnmpAdminString
_OtdrTraceMgmtIpv6Address_Object = MibTableColumn
otdrTraceMgmtIpv6Address = _OtdrTraceMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 13),
    _OtdrTraceMgmtIpv6Address_Type()
)
otdrTraceMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtIpv6Address.setStatus("current")


class _OtdrTraceMgmtScpPort_Type(Integer32):
    """Custom type otdrTraceMgmtScpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OtdrTraceMgmtScpPort_Type.__name__ = "Integer32"
_OtdrTraceMgmtScpPort_Object = MibTableColumn
otdrTraceMgmtScpPort = _OtdrTraceMgmtScpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 7, 1, 1, 14),
    _OtdrTraceMgmtScpPort_Type()
)
otdrTraceMgmtScpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdrTraceMgmtScpPort.setStatus("current")
_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8)
)
_InventoryTable_Object = MibTable
inventoryTable = _InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1)
)
if mibBuilder.loadTexts:
    inventoryTable.setStatus("current")
_InventoryEntry_Object = MibTableRow
inventoryEntry = _InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1)
)
inventoryEntry.setIndexNames(
    (0, "ADVA-FSP3000ALM-MIB", "inventoryShelfNo"),
    (0, "ADVA-FSP3000ALM-MIB", "inventorySlotNo"),
    (0, "ADVA-FSP3000ALM-MIB", "inventoryPortNo"),
    (0, "ADVA-FSP3000ALM-MIB", "inventoryExtNo"),
    (0, "ADVA-FSP3000ALM-MIB", "inventoryClassName"),
)
if mibBuilder.loadTexts:
    inventoryEntry.setStatus("current")


class _InventoryShelfNo_Type(Integer32):
    """Custom type inventoryShelfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InventoryShelfNo_Type.__name__ = "Integer32"
_InventoryShelfNo_Object = MibTableColumn
inventoryShelfNo = _InventoryShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 1),
    _InventoryShelfNo_Type()
)
inventoryShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventoryShelfNo.setStatus("current")


class _InventorySlotNo_Type(Integer32):
    """Custom type inventorySlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_InventorySlotNo_Type.__name__ = "Integer32"
_InventorySlotNo_Object = MibTableColumn
inventorySlotNo = _InventorySlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 2),
    _InventorySlotNo_Type()
)
inventorySlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventorySlotNo.setStatus("current")


class _InventoryPortNo_Type(Integer32):
    """Custom type inventoryPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_InventoryPortNo_Type.__name__ = "Integer32"
_InventoryPortNo_Object = MibTableColumn
inventoryPortNo = _InventoryPortNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 3),
    _InventoryPortNo_Type()
)
inventoryPortNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventoryPortNo.setStatus("current")


class _InventoryExtNo_Type(Integer32):
    """Custom type inventoryExtNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_InventoryExtNo_Type.__name__ = "Integer32"
_InventoryExtNo_Object = MibTableColumn
inventoryExtNo = _InventoryExtNo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 4),
    _InventoryExtNo_Type()
)
inventoryExtNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventoryExtNo.setStatus("current")


class _InventoryClassName_Type(Integer32):
    """Custom type inventoryClassName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
    )


_InventoryClassName_Type.__name__ = "Integer32"
_InventoryClassName_Object = MibTableColumn
inventoryClassName = _InventoryClassName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 5),
    _InventoryClassName_Type()
)
inventoryClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inventoryClassName.setStatus("current")
_InventoryAidString_Type = IdentityTranslation
_InventoryAidString_Object = MibTableColumn
inventoryAidString = _InventoryAidString_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 6),
    _InventoryAidString_Type()
)
inventoryAidString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryAidString.setStatus("current")
_InventoryUnitName_Type = SnmpAdminString
_InventoryUnitName_Object = MibTableColumn
inventoryUnitName = _InventoryUnitName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 7),
    _InventoryUnitName_Type()
)
inventoryUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryUnitName.setStatus("current")
_InventoryFirmwarePackageRev_Type = SnmpAdminString
_InventoryFirmwarePackageRev_Object = MibTableColumn
inventoryFirmwarePackageRev = _InventoryFirmwarePackageRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 8),
    _InventoryFirmwarePackageRev_Type()
)
inventoryFirmwarePackageRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFirmwarePackageRev.setStatus("current")
_InventoryHardwareRev_Type = SnmpAdminString
_InventoryHardwareRev_Object = MibTableColumn
inventoryHardwareRev = _InventoryHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 9),
    _InventoryHardwareRev_Type()
)
inventoryHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryHardwareRev.setStatus("current")
_InventoryFpgaRev_Type = SnmpAdminString
_InventoryFpgaRev_Object = MibTableColumn
inventoryFpgaRev = _InventoryFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 10),
    _InventoryFpgaRev_Type()
)
inventoryFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryFpgaRev.setStatus("current")
_InventorySerialNumber_Type = SnmpAdminString
_InventorySerialNumber_Object = MibTableColumn
inventorySerialNumber = _InventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 11),
    _InventorySerialNumber_Type()
)
inventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventorySerialNumber.setStatus("current")
_InventoryPartNumber_Type = SnmpAdminString
_InventoryPartNumber_Object = MibTableColumn
inventoryPartNumber = _InventoryPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 12),
    _InventoryPartNumber_Type()
)
inventoryPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryPartNumber.setStatus("current")
_InventoryCleiCode_Type = SnmpAdminString
_InventoryCleiCode_Object = MibTableColumn
inventoryCleiCode = _InventoryCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 13),
    _InventoryCleiCode_Type()
)
inventoryCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryCleiCode.setStatus("current")
_InventoryOrigin_Type = SnmpAdminString
_InventoryOrigin_Object = MibTableColumn
inventoryOrigin = _InventoryOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 14),
    _InventoryOrigin_Type()
)
inventoryOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryOrigin.setStatus("current")
_InventoryShelfType_Type = SnmpAdminString
_InventoryShelfType_Object = MibTableColumn
inventoryShelfType = _InventoryShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 15),
    _InventoryShelfType_Type()
)
inventoryShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryShelfType.setStatus("current")
_InventoryUniversalSerialIdent_Type = SnmpAdminString
_InventoryUniversalSerialIdent_Object = MibTableColumn
inventoryUniversalSerialIdent = _InventoryUniversalSerialIdent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 8, 1, 1, 16),
    _InventoryUniversalSerialIdent_Type()
)
inventoryUniversalSerialIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inventoryUniversalSerialIdent.setStatus("current")

# Managed Objects groups


# Notification objects

alarmTempCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 1)
)
alarmTempCPU.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempCPU.setStatus(
        "current"
    )

alarmTempBoard1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 2)
)
alarmTempBoard1.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard1.setStatus(
        "current"
    )

alarmTempBoard2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 3)
)
alarmTempBoard2Low.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard2Low.setStatus(
        "current"
    )

alarmTempBoard2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 4)
)
alarmTempBoard2High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempBoard2High.setStatus(
        "current"
    )

alarmTempLaserLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 5)
)
alarmTempLaserLow.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempLaserLow.setStatus(
        "current"
    )

alarmTempLaserHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 6)
)
alarmTempLaserHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTempLaserHigh.setStatus(
        "current"
    )

alarmMonNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 7)
)
alarmMonNotRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmMonNotRunning.setStatus(
        "current"
    )

alarmFpRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 8)
)
alarmFpRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFpRunning.setStatus(
        "current"
    )

alarmFaRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 9)
)
alarmFaRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFaRunning.setStatus(
        "current"
    )

alarmFpMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 10)
)
alarmFpMissing.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmFpMissing.setStatus(
        "current"
    )

alarmThresCrossedFast = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 11)
)
alarmThresCrossedFast.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedFast.setStatus(
        "current"
    )

alarmThresCrossedMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 12)
)
alarmThresCrossedMedium.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedMedium.setStatus(
        "current"
    )

alarmThresCrossedSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 13)
)
alarmThresCrossedSlow.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmThresCrossedSlow.setStatus(
        "current"
    )

alarmLinkBudgetExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 14)
)
alarmLinkBudgetExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLinkBudgetExceeded.setStatus(
        "current"
    )

alarmLinkBudgetNearlyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 15)
)
alarmLinkBudgetNearlyExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLinkBudgetNearlyExceeded.setStatus(
        "current"
    )

alarmManagementState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 16)
)
alarmManagementState.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmManagementState.setStatus(
        "current"
    )

alarmDisabledState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 17)
)
alarmDisabledState.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmDisabledState.setStatus(
        "current"
    )

stateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 18)
)
stateChangedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    stateChangedTrap.setStatus(
        "current"
    )

objectChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 19)
)
objectChangedTrap.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    objectChangedTrap.setStatus(
        "current"
    )

trapsinkCreatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 20)
)
trapsinkCreatedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "trapsinkAddress"),
        ("ADVA-FSP3000ALM-MIB", "ipv6TrapsinkAddress"),
        ("ADVA-FSP3000ALM-MIB", "dnsTrapsinkHostName"))
)
if mibBuilder.loadTexts:
    trapsinkCreatedTrap.setStatus(
        "current"
    )

trapsinkDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 21)
)
trapsinkDeletedTrap.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "trapsinkAddress"),
        ("ADVA-FSP3000ALM-MIB", "ipv6TrapsinkAddress"),
        ("ADVA-FSP3000ALM-MIB", "dnsTrapsinkHostName"))
)
if mibBuilder.loadTexts:
    trapsinkDeletedTrap.setStatus(
        "current"
    )

transient15MinMeasCollected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 22)
)
if mibBuilder.loadTexts:
    transient15MinMeasCollected.setStatus(
        "current"
    )

transient1DayMeasCollected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 23)
)
if mibBuilder.loadTexts:
    transient1DayMeasCollected.setStatus(
        "current"
    )

transientFpStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 24)
)
transientFpStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpStarted.setStatus(
        "current"
    )

transientFpCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 25)
)
transientFpCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpCompleted.setStatus(
        "current"
    )

transientFpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 26)
)
transientFpFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpFailed.setStatus(
        "current"
    )

transientSwMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 27)
)
transientSwMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionStarted.setStatus(
        "current"
    )

transientSwMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 28)
)
transientSwMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionCompleted.setStatus(
        "current"
    )

transientSwMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 29)
)
transientSwMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "softwareMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientSwMgmtActionFailed.setStatus(
        "current"
    )

transientDbMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 30)
)
transientDbMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionStarted.setStatus(
        "current"
    )

transientDbMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 31)
)
transientDbMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionCompleted.setStatus(
        "current"
    )

transientDbMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 32)
)
transientDbMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "databaseMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientDbMgmtActionFailed.setStatus(
        "current"
    )

alarmNtpServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 33)
)
alarmNtpServerUnreachable.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"),
        ("ADVA-FSP3000ALM-MIB", "ntpServerName"),
        ("ADVA-FSP3000ALM-MIB", "ntpServerName2"),
        ("ADVA-FSP3000ALM-MIB", "ntpServerName3"))
)
if mibBuilder.loadTexts:
    alarmNtpServerUnreachable.setStatus(
        "current"
    )

transientFpSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 34)
)
transientFpSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFpSaved.setStatus(
        "current"
    )

transientMonStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 35)
)
transientMonStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientMonStarted.setStatus(
        "current"
    )

transientMonStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 36)
)
transientMonStopped.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientMonStopped.setStatus(
        "current"
    )

transientOtdrMeasurementStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 37)
)
transientOtdrMeasurementStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementStarted.setStatus(
        "current"
    )

transientOtdrMeasurementCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 38)
)
transientOtdrMeasurementCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementCompleted.setStatus(
        "current"
    )

transientOtdrMeasurementFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 39)
)
transientOtdrMeasurementFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementFailed.setStatus(
        "current"
    )

transientOtdrMeasurementSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 40)
)
transientOtdrMeasurementSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementSaved.setStatus(
        "current"
    )

transientFaStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 41)
)
transientFaStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaStarted.setStatus(
        "current"
    )

transientFaCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 42)
)
transientFaCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaCompleted.setStatus(
        "current"
    )

transientFaFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 43)
)
transientFaFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaFailed.setStatus(
        "current"
    )

transientFaSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 44)
)
transientFaSaved.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "measurementFaFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "measurementFaCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "measurementAutoFaFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "measurementAutoFaCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "measurementFaFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "measurementFaFaultPosLongitude"),
        ("ADVA-FSP3000ALM-MIB", "measurementAutoFaFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "measurementAutoFaFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    transientFaSaved.setStatus(
        "current"
    )

transientInternalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 45)
)
transientInternalError.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    transientInternalError.setStatus(
        "current"
    )

alarmRebootRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 46)
)
alarmRebootRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmRebootRunning.setStatus(
        "current"
    )

alarmWarmupRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 47)
)
alarmWarmupRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmWarmupRunning.setStatus(
        "current"
    )

alarmBadSysStat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 48)
)
alarmBadSysStat.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmBadSysStat.setStatus(
        "current"
    )

alarmWrongFWVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 49)
)
alarmWrongFWVersion.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmWrongFWVersion.setStatus(
        "current"
    )

alarmMonProcNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 50)
)
alarmMonProcNotRunning.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmMonProcNotRunning.setStatus(
        "current"
    )

transientFaDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 51)
)
transientFaDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFaDeleted.setStatus(
        "current"
    )

transientOtdrMeasurementDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 52)
)
transientOtdrMeasurementDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientOtdrMeasurementDeleted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 53)
)
transientOtdrTraceMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionStarted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 54)
)
transientOtdrTraceMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionCompleted.setStatus(
        "current"
    )

transientOtdrTraceMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 55)
)
transientOtdrTraceMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtFileName"),
        ("ADVA-FSP3000ALM-MIB", "otdrTraceMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientOtdrTraceMgmtActionFailed.setStatus(
        "current"
    )

alarmAlmPackageMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 56)
)
alarmAlmPackageMismatch.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmAlmPackageMismatch.setStatus(
        "current"
    )

alarmEmailNotifyThresCrossedFast = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 57)
)
alarmEmailNotifyThresCrossedFast.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyThresCrossedFast.setStatus(
        "current"
    )

alarmEmailNotifyThresCrossedMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 58)
)
alarmEmailNotifyThresCrossedMedium.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyThresCrossedMedium.setStatus(
        "current"
    )

alarmEmailNotifyThresCrossedSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 59)
)
alarmEmailNotifyThresCrossedSlow.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyThresCrossedSlow.setStatus(
        "current"
    )

alarmEmailNotifyLinkBudgetExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 60)
)
alarmEmailNotifyLinkBudgetExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyLinkBudgetExceeded.setStatus(
        "current"
    )

alarmEmailNotifyLinkBudgetNearlyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 61)
)
alarmEmailNotifyLinkBudgetNearlyExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyLinkBudgetNearlyExceeded.setStatus(
        "current"
    )

authenticationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 62)
)
authenticationNotification.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "authTrapLctIp"),
        ("ADVA-FSP3000ALM-MIB", "authTrapStatus"),
        ("ADVA-FSP3000ALM-MIB", "authTrapSessionId"),
        ("ADVA-FSP3000ALM-MIB", "authTrapProtocol"),
        ("ADVA-FSP3000ALM-MIB", "authTrapUserName"),
        ("ADVA-FSP3000ALM-MIB", "authTrapLctIpv6"))
)
if mibBuilder.loadTexts:
    authenticationNotification.setStatus(
        "current"
    )

authenticationNotificationSummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 63)
)
authenticationNotificationSummary.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "authTrapProtocol"),
        ("ADVA-FSP3000ALM-MIB", "authTrapSuccessfulAuthCount"),
        ("ADVA-FSP3000ALM-MIB", "authTrapUnsuccessfulAuthCount"),
        ("ADVA-FSP3000ALM-MIB", "authTrapLogoutCount"))
)
if mibBuilder.loadTexts:
    authenticationNotificationSummary.setStatus(
        "current"
    )

monitorPointCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 64)
)
monitorPointCreated.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"))
)
if mibBuilder.loadTexts:
    monitorPointCreated.setStatus(
        "current"
    )

monitorPointDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 65)
)
monitorPointDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"))
)
if mibBuilder.loadTexts:
    monitorPointDeleted.setStatus(
        "current"
    )

alarmLossDeviationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 66)
)
alarmLossDeviationHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLossDeviationHigh.setStatus(
        "current"
    )

alarmLossHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 67)
)
alarmLossHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmLossHigh.setStatus(
        "current"
    )

alarmRootLinkFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 68)
)
alarmRootLinkFault.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmRootLinkFault.setStatus(
        "current"
    )

transientResetMeansStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 69)
)
transientResetMeansStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientResetMeansStarted.setStatus(
        "current"
    )

transientResetMeansCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 70)
)
transientResetMeansCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientResetMeansCompleted.setStatus(
        "current"
    )

transientResetMeansFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 71)
)
transientResetMeansFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientResetMeansFailed.setStatus(
        "current"
    )

alarmTrafficOutage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 72)
)
alarmTrafficOutage.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTrafficOutage.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 73)
)
userAdded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "userManagementUsername"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 74)
)
userDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "userManagementUsername"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

customizedFpEventCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 75)
)
customizedFpEventCreated.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "customizedFpEventId"),
        ("ADVA-FSP3000ALM-MIB", "customizedFpEventCorrectedPosition"),
        ("ADVA-FSP3000ALM-MIB", "customizedFpEventRemark"))
)
if mibBuilder.loadTexts:
    customizedFpEventCreated.setStatus(
        "current"
    )

customizedFpEventDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 76)
)
customizedFpEventDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "customizedFpEventId"))
)
if mibBuilder.loadTexts:
    customizedFpEventDeleted.setStatus(
        "current"
    )

transientExportMgmtActionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 77)
)
transientExportMgmtActionStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "exportMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientExportMgmtActionStarted.setStatus(
        "current"
    )

transientExportMgmtActionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 78)
)
transientExportMgmtActionCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "exportMgmtRequest"))
)
if mibBuilder.loadTexts:
    transientExportMgmtActionCompleted.setStatus(
        "current"
    )

transientExportMgmtActionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 79)
)
transientExportMgmtActionFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "exportMgmtRequest"),
        ("ADVA-FSP3000ALM-MIB", "exportMgmtLastError"))
)
if mibBuilder.loadTexts:
    transientExportMgmtActionFailed.setStatus(
        "current"
    )

alarmSensor1High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 80)
)
alarmSensor1High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmSensor1High.setStatus(
        "current"
    )

alarmSensor2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 81)
)
alarmSensor2High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmSensor2High.setStatus(
        "current"
    )

alarmEmailNotifyRootLinkFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 82)
)
alarmEmailNotifyRootLinkFault.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLatitude"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosLongitude"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyRootLinkFault.setStatus(
        "current"
    )

transientTimeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 83)
)
transientTimeChange.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "localDateAndTime"),
        ("ADVA-FSP3000ALM-MIB", "ntpTimeChangeReason"))
)
if mibBuilder.loadTexts:
    transientTimeChange.setStatus(
        "current"
    )

alarmTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 84)
)
alarmTopologyChanged.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmTopologyChanged.setStatus(
        "current"
    )

alarmEmailNotifyLossDeviationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 85)
)
alarmEmailNotifyLossDeviationHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyLossDeviationHigh.setStatus(
        "current"
    )

alarmEmailNotifyLossHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 86)
)
alarmEmailNotifyLossHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyLossHigh.setStatus(
        "current"
    )

alarmEmailNotifySensor1High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 87)
)
alarmEmailNotifySensor1High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifySensor1High.setStatus(
        "current"
    )

alarmEmailNotifySensor2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 88)
)
alarmEmailNotifySensor2High.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifySensor2High.setStatus(
        "current"
    )

alarmEmulationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 89)
)
alarmEmulationMode.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "aidString"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmEmulationMode.setStatus(
        "current"
    )

transientFiberIdentifierStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 90)
)
transientFiberIdentifierStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFiberIdentifierStarted.setStatus(
        "current"
    )

transientFiberIdentifierCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 91)
)
transientFiberIdentifierCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFiberIdentifierCompleted.setStatus(
        "current"
    )

transientFiberIdentifierFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 92)
)
transientFiberIdentifierFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"))
)
if mibBuilder.loadTexts:
    transientFiberIdentifierFailed.setStatus(
        "current"
    )

transientPkiCertRequestStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 93)
)
transientPkiCertRequestStarted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "caId"),
        ("ADVA-FSP3000ALM-MIB", "certificateId"),
        ("ADVA-FSP3000ALM-MIB", "keyId"))
)
if mibBuilder.loadTexts:
    transientPkiCertRequestStarted.setStatus(
        "current"
    )

transientPkiCertRequestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 94)
)
transientPkiCertRequestCompleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "caId"),
        ("ADVA-FSP3000ALM-MIB", "certificateId"),
        ("ADVA-FSP3000ALM-MIB", "keyId"))
)
if mibBuilder.loadTexts:
    transientPkiCertRequestCompleted.setStatus(
        "current"
    )

transientPkiCertRequestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 95)
)
transientPkiCertRequestFailed.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "caId"),
        ("ADVA-FSP3000ALM-MIB", "certificateId"),
        ("ADVA-FSP3000ALM-MIB", "keyId"),
        ("ADVA-FSP3000ALM-MIB", "keyCertRequestStatus"))
)
if mibBuilder.loadTexts:
    transientPkiCertRequestFailed.setStatus(
        "current"
    )

alarmCertExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 96)
)
alarmCertExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "certificateId"))
)
if mibBuilder.loadTexts:
    alarmCertExceeded.setStatus(
        "current"
    )

alarmCertNearlyExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 97)
)
alarmCertNearlyExceeded.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "certificateId"))
)
if mibBuilder.loadTexts:
    alarmCertNearlyExceeded.setStatus(
        "current"
    )

transientLinkChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 98)
)
transientLinkChanged.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "linkLayoutEventId"))
)
if mibBuilder.loadTexts:
    transientLinkChanged.setStatus(
        "current"
    )

alarmAddDropLinkLossHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 99)
)
alarmAddDropLinkLossHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmAddDropLinkLossHigh.setStatus(
        "current"
    )

alarmAddDropLinkLossDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 100)
)
alarmAddDropLinkLossDev.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointPos"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmAddDropLinkLossDev.setStatus(
        "current"
    )

alarmEmailNotifyAddDropLinkLossHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 101)
)
alarmEmailNotifyAddDropLinkLossHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyAddDropLinkLossHigh.setStatus(
        "current"
    )

alarmEmailNotifyAddDropLinkLossDev = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 102)
)
alarmEmailNotifyAddDropLinkLossDev.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointAidString"),
        ("ADVA-FSP3000ALM-MIB", "monitorPointName"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyExternalId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyId"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifySeverity"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyState"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEvent"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyEventTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultType"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultPosition"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyCorrectedFaultPos"),
        ("ADVA-FSP3000ALM-MIB", "alarmEmailNotifyFaultAnalysisReference"))
)
if mibBuilder.loadTexts:
    alarmEmailNotifyAddDropLinkLossDev.setStatus(
        "current"
    )

segmentCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 103)
)
segmentCreated.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "segmentId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStartEventId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStopEventId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStartCorrection"),
        ("ADVA-FSP3000ALM-MIB", "segmentStopCorrection"),
        ("ADVA-FSP3000ALM-MIB", "segmentRemark"))
)
if mibBuilder.loadTexts:
    segmentCreated.setStatus(
        "current"
    )

segmentDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 104)
)
segmentDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "segmentId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStartEventId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStopEventId"),
        ("ADVA-FSP3000ALM-MIB", "segmentStartCorrection"),
        ("ADVA-FSP3000ALM-MIB", "segmentStopCorrection"),
        ("ADVA-FSP3000ALM-MIB", "segmentRemark"))
)
if mibBuilder.loadTexts:
    segmentDeleted.setStatus(
        "current"
    )

alarmEquipmentRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 105)
)
alarmEquipmentRemoved.setObjects(
    ("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp")
)
if mibBuilder.loadTexts:
    alarmEquipmentRemoved.setStatus(
        "current"
    )

alarmEquipmentFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 106)
)
alarmEquipmentFault.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "extShelfAidString"),
        ("ADVA-FSP3000ALM-MIB", "extShelfName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmEquipmentFault.setStatus(
        "current"
    )

alarmAttenuationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 107)
)
alarmAttenuationHigh.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    alarmAttenuationHigh.setStatus(
        "current"
    )

internalExtensionChannelCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 108)
)
internalExtensionChannelCreated.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"))
)
if mibBuilder.loadTexts:
    internalExtensionChannelCreated.setStatus(
        "current"
    )

internalExtensionChannelDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 109)
)
internalExtensionChannelDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "portAidString"),
        ("ADVA-FSP3000ALM-MIB", "portName"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"),
        ("ADVA-FSP3000ALM-MIB", "entityPortAidString"))
)
if mibBuilder.loadTexts:
    internalExtensionChannelDeleted.setStatus(
        "current"
    )

portExtenderCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 110)
)
portExtenderCreated.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "extShelfAidString"),
        ("ADVA-FSP3000ALM-MIB", "extShelfName"),
        ("ADVA-FSP3000ALM-MIB", "extShelfType"))
)
if mibBuilder.loadTexts:
    portExtenderCreated.setStatus(
        "current"
    )

portExtenderDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 14, 0, 111)
)
portExtenderDeleted.setObjects(
      *(("ADVA-FSP3000ALM-MIB", "eventLogTimeStamp"),
        ("ADVA-FSP3000ALM-MIB", "extShelfAidString"),
        ("ADVA-FSP3000ALM-MIB", "extShelfName"),
        ("ADVA-FSP3000ALM-MIB", "extShelfType"))
)
if mibBuilder.loadTexts:
    portExtenderDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVA-FSP3000ALM-MIB",
    **{"Fsp3000almAlarmListType": Fsp3000almAlarmListType,
       "advaMIB": advaMIB,
       "products": products,
       "fsp3000alm": fsp3000alm,
       "trap": trap,
       "alarmTempCPU": alarmTempCPU,
       "alarmTempBoard1": alarmTempBoard1,
       "alarmTempBoard2Low": alarmTempBoard2Low,
       "alarmTempBoard2High": alarmTempBoard2High,
       "alarmTempLaserLow": alarmTempLaserLow,
       "alarmTempLaserHigh": alarmTempLaserHigh,
       "alarmMonNotRunning": alarmMonNotRunning,
       "alarmFpRunning": alarmFpRunning,
       "alarmFaRunning": alarmFaRunning,
       "alarmFpMissing": alarmFpMissing,
       "alarmThresCrossedFast": alarmThresCrossedFast,
       "alarmThresCrossedMedium": alarmThresCrossedMedium,
       "alarmThresCrossedSlow": alarmThresCrossedSlow,
       "alarmLinkBudgetExceeded": alarmLinkBudgetExceeded,
       "alarmLinkBudgetNearlyExceeded": alarmLinkBudgetNearlyExceeded,
       "alarmManagementState": alarmManagementState,
       "alarmDisabledState": alarmDisabledState,
       "stateChangedTrap": stateChangedTrap,
       "objectChangedTrap": objectChangedTrap,
       "trapsinkCreatedTrap": trapsinkCreatedTrap,
       "trapsinkDeletedTrap": trapsinkDeletedTrap,
       "transient15MinMeasCollected": transient15MinMeasCollected,
       "transient1DayMeasCollected": transient1DayMeasCollected,
       "transientFpStarted": transientFpStarted,
       "transientFpCompleted": transientFpCompleted,
       "transientFpFailed": transientFpFailed,
       "transientSwMgmtActionStarted": transientSwMgmtActionStarted,
       "transientSwMgmtActionCompleted": transientSwMgmtActionCompleted,
       "transientSwMgmtActionFailed": transientSwMgmtActionFailed,
       "transientDbMgmtActionStarted": transientDbMgmtActionStarted,
       "transientDbMgmtActionCompleted": transientDbMgmtActionCompleted,
       "transientDbMgmtActionFailed": transientDbMgmtActionFailed,
       "alarmNtpServerUnreachable": alarmNtpServerUnreachable,
       "transientFpSaved": transientFpSaved,
       "transientMonStarted": transientMonStarted,
       "transientMonStopped": transientMonStopped,
       "transientOtdrMeasurementStarted": transientOtdrMeasurementStarted,
       "transientOtdrMeasurementCompleted": transientOtdrMeasurementCompleted,
       "transientOtdrMeasurementFailed": transientOtdrMeasurementFailed,
       "transientOtdrMeasurementSaved": transientOtdrMeasurementSaved,
       "transientFaStarted": transientFaStarted,
       "transientFaCompleted": transientFaCompleted,
       "transientFaFailed": transientFaFailed,
       "transientFaSaved": transientFaSaved,
       "transientInternalError": transientInternalError,
       "alarmRebootRunning": alarmRebootRunning,
       "alarmWarmupRunning": alarmWarmupRunning,
       "alarmBadSysStat": alarmBadSysStat,
       "alarmWrongFWVersion": alarmWrongFWVersion,
       "alarmMonProcNotRunning": alarmMonProcNotRunning,
       "transientFaDeleted": transientFaDeleted,
       "transientOtdrMeasurementDeleted": transientOtdrMeasurementDeleted,
       "transientOtdrTraceMgmtActionStarted": transientOtdrTraceMgmtActionStarted,
       "transientOtdrTraceMgmtActionCompleted": transientOtdrTraceMgmtActionCompleted,
       "transientOtdrTraceMgmtActionFailed": transientOtdrTraceMgmtActionFailed,
       "alarmAlmPackageMismatch": alarmAlmPackageMismatch,
       "alarmEmailNotifyThresCrossedFast": alarmEmailNotifyThresCrossedFast,
       "alarmEmailNotifyThresCrossedMedium": alarmEmailNotifyThresCrossedMedium,
       "alarmEmailNotifyThresCrossedSlow": alarmEmailNotifyThresCrossedSlow,
       "alarmEmailNotifyLinkBudgetExceeded": alarmEmailNotifyLinkBudgetExceeded,
       "alarmEmailNotifyLinkBudgetNearlyExceeded": alarmEmailNotifyLinkBudgetNearlyExceeded,
       "authenticationNotification": authenticationNotification,
       "authenticationNotificationSummary": authenticationNotificationSummary,
       "monitorPointCreated": monitorPointCreated,
       "monitorPointDeleted": monitorPointDeleted,
       "alarmLossDeviationHigh": alarmLossDeviationHigh,
       "alarmLossHigh": alarmLossHigh,
       "alarmRootLinkFault": alarmRootLinkFault,
       "transientResetMeansStarted": transientResetMeansStarted,
       "transientResetMeansCompleted": transientResetMeansCompleted,
       "transientResetMeansFailed": transientResetMeansFailed,
       "alarmTrafficOutage": alarmTrafficOutage,
       "userAdded": userAdded,
       "userDeleted": userDeleted,
       "customizedFpEventCreated": customizedFpEventCreated,
       "customizedFpEventDeleted": customizedFpEventDeleted,
       "transientExportMgmtActionStarted": transientExportMgmtActionStarted,
       "transientExportMgmtActionCompleted": transientExportMgmtActionCompleted,
       "transientExportMgmtActionFailed": transientExportMgmtActionFailed,
       "alarmSensor1High": alarmSensor1High,
       "alarmSensor2High": alarmSensor2High,
       "alarmEmailNotifyRootLinkFault": alarmEmailNotifyRootLinkFault,
       "transientTimeChange": transientTimeChange,
       "alarmTopologyChanged": alarmTopologyChanged,
       "alarmEmailNotifyLossDeviationHigh": alarmEmailNotifyLossDeviationHigh,
       "alarmEmailNotifyLossHigh": alarmEmailNotifyLossHigh,
       "alarmEmailNotifySensor1High": alarmEmailNotifySensor1High,
       "alarmEmailNotifySensor2High": alarmEmailNotifySensor2High,
       "alarmEmulationMode": alarmEmulationMode,
       "transientFiberIdentifierStarted": transientFiberIdentifierStarted,
       "transientFiberIdentifierCompleted": transientFiberIdentifierCompleted,
       "transientFiberIdentifierFailed": transientFiberIdentifierFailed,
       "transientPkiCertRequestStarted": transientPkiCertRequestStarted,
       "transientPkiCertRequestCompleted": transientPkiCertRequestCompleted,
       "transientPkiCertRequestFailed": transientPkiCertRequestFailed,
       "alarmCertExceeded": alarmCertExceeded,
       "alarmCertNearlyExceeded": alarmCertNearlyExceeded,
       "transientLinkChanged": transientLinkChanged,
       "alarmAddDropLinkLossHigh": alarmAddDropLinkLossHigh,
       "alarmAddDropLinkLossDev": alarmAddDropLinkLossDev,
       "alarmEmailNotifyAddDropLinkLossHigh": alarmEmailNotifyAddDropLinkLossHigh,
       "alarmEmailNotifyAddDropLinkLossDev": alarmEmailNotifyAddDropLinkLossDev,
       "segmentCreated": segmentCreated,
       "segmentDeleted": segmentDeleted,
       "alarmEquipmentRemoved": alarmEquipmentRemoved,
       "alarmEquipmentFault": alarmEquipmentFault,
       "alarmAttenuationHigh": alarmAttenuationHigh,
       "internalExtensionChannelCreated": internalExtensionChannelCreated,
       "internalExtensionChannelDeleted": internalExtensionChannelDeleted,
       "portExtenderCreated": portExtenderCreated,
       "portExtenderDeleted": portExtenderDeleted,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmSource": alarmSource,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmTimeStamp": alarmTimeStamp,
       "alarmSeverityTable": alarmSeverityTable,
       "alarmSeverityEntry": alarmSeverityEntry,
       "alarmSeverityType": alarmSeverityType,
       "alarmSeverityValue": alarmSeverityValue,
       "alarmEmailNotifyTable": alarmEmailNotifyTable,
       "alarmEmailNotifyEntry": alarmEmailNotifyEntry,
       "alarmEmailNotifyType": alarmEmailNotifyType,
       "alarmEmailNotifyExternalId": alarmEmailNotifyExternalId,
       "alarmEmailNotifyId": alarmEmailNotifyId,
       "alarmEmailNotifySeverity": alarmEmailNotifySeverity,
       "alarmEmailNotifyTimeStamp": alarmEmailNotifyTimeStamp,
       "alarmEmailNotifyFaultPosition": alarmEmailNotifyFaultPosition,
       "alarmEmailNotifyFaultType": alarmEmailNotifyFaultType,
       "alarmEmailNotifyState": alarmEmailNotifyState,
       "alarmEmailNotifyEvent": alarmEmailNotifyEvent,
       "alarmEmailNotifyEventTimeStamp": alarmEmailNotifyEventTimeStamp,
       "alarmEmailNotifyFaultAnalysisReference": alarmEmailNotifyFaultAnalysisReference,
       "alarmEmailNotifyCorrectedFaultPos": alarmEmailNotifyCorrectedFaultPos,
       "alarmEmailNotifyFaultPosLatitude": alarmEmailNotifyFaultPosLatitude,
       "alarmEmailNotifyFaultPosLongitude": alarmEmailNotifyFaultPosLongitude,
       "alarmDescriptionTable": alarmDescriptionTable,
       "alarmDescriptionEntry": alarmDescriptionEntry,
       "alarmDescriptionName": alarmDescriptionName,
       "lossAlarmsMasking": lossAlarmsMasking,
       "device": device,
       "shelf": shelf,
       "shelfUnitName": shelfUnitName,
       "firmwarePackageRev": firmwarePackageRev,
       "hardwareRev": hardwareRev,
       "fpgaRev": fpgaRev,
       "serialNumber": serialNumber,
       "partNumber": partNumber,
       "cleiCode": cleiCode,
       "vendorId": vendorId,
       "inventoryType": inventoryType,
       "universalSerialIdent": universalSerialIdent,
       "tempCPU": tempCPU,
       "thresholdMaxTempCPU": thresholdMaxTempCPU,
       "tempBoard1": tempBoard1,
       "thresholdMaxTempBoard1": thresholdMaxTempBoard1,
       "tempBoard2": tempBoard2,
       "thresholdMinTempBoard2": thresholdMinTempBoard2,
       "thresholdMaxTempBoard2": thresholdMaxTempBoard2,
       "tempLaser": tempLaser,
       "thresholdMinTempLaser": thresholdMinTempLaser,
       "thresholdMaxTempLaser": thresholdMaxTempLaser,
       "aidString": aidString,
       "shelfName": shelfName,
       "portTable": portTable,
       "portEntry": portEntry,
       "portId": portId,
       "portAdminState": portAdminState,
       "portOperState": portOperState,
       "portName": portName,
       "portAidString": portAidString,
       "portRemark": portRemark,
       "portFingerprintMode": portFingerprintMode,
       "portPriority": portPriority,
       "portGisConfigured": portGisConfigured,
       "portConnectedInternalChannel": portConnectedInternalChannel,
       "portPmData": portPmData,
       "monitoringItems": monitoringItems,
       "feederLengthTable": feederLengthTable,
       "feederLengthEntry": feederLengthEntry,
       "feederLength": feederLength,
       "monitorPointTable": monitorPointTable,
       "monitorPointEntry": monitorPointEntry,
       "mpId": mpId,
       "monitorPointPos": monitorPointPos,
       "monitorPointState": monitorPointState,
       "monitorPointName": monitorPointName,
       "monitorPointAidString": monitorPointAidString,
       "monitorPointRemark": monitorPointRemark,
       "monitorPointExternalId": monitorPointExternalId,
       "extShelfTable": extShelfTable,
       "extShelfEntry": extShelfEntry,
       "extShelfNo": extShelfNo,
       "extShelfRowStatus": extShelfRowStatus,
       "extShelfType": extShelfType,
       "extShelfAidString": extShelfAidString,
       "extShelfInternalId": extShelfInternalId,
       "extShelfNrInternalPorts": extShelfNrInternalPorts,
       "extShelfNrMonitorPorts": extShelfNrMonitorPorts,
       "extShelfName": extShelfName,
       "extShelfRemark": extShelfRemark,
       "entityPortTable": entityPortTable,
       "entityPortEntry": entityPortEntry,
       "entityPortInternalNo": entityPortInternalNo,
       "entityPortPortNo": entityPortPortNo,
       "entityPortAidString": entityPortAidString,
       "entityPortPortId": entityPortPortId,
       "measurement": measurement,
       "measurementLossTable": measurementLossTable,
       "measurementLossEntry": measurementLossEntry,
       "measurementLossIndex": measurementLossIndex,
       "measurementLossLinkLoss": measurementLossLinkLoss,
       "measurementLossLinkFaultLoc": measurementLossLinkFaultLoc,
       "measurementLossLinkFaultLocRes": measurementLossLinkFaultLocRes,
       "measurementLossDevFast": measurementLossDevFast,
       "measurementLossDevMedium": measurementLossDevMedium,
       "measurementLossDevSlow": measurementLossDevSlow,
       "measurementLossDataTimestamp": measurementLossDataTimestamp,
       "histMeasLoss15MinTable": histMeasLoss15MinTable,
       "histMeasLoss15MinEntry": histMeasLoss15MinEntry,
       "histMeasLoss15MinNumber": histMeasLoss15MinNumber,
       "histMeasLoss15MinLow": histMeasLoss15MinLow,
       "histMeasLoss15MinMean": histMeasLoss15MinMean,
       "histMeasLoss15MinHigh": histMeasLoss15MinHigh,
       "histMeasLoss15MinValidFlag": histMeasLoss15MinValidFlag,
       "histMeasLoss15MinTimeStamp": histMeasLoss15MinTimeStamp,
       "histMeasLoss15MinLength": histMeasLoss15MinLength,
       "histMeasLoss15MinLossPerKmLow": histMeasLoss15MinLossPerKmLow,
       "histMeasLoss15MinLossPerKmMean": histMeasLoss15MinLossPerKmMean,
       "histMeasLoss15MinLossPerKmHigh": histMeasLoss15MinLossPerKmHigh,
       "histMeasLoss1DayTable": histMeasLoss1DayTable,
       "histMeasLoss1DayEntry": histMeasLoss1DayEntry,
       "histMeasLoss1DayNumber": histMeasLoss1DayNumber,
       "histMeasLoss1DayLow": histMeasLoss1DayLow,
       "histMeasLoss1DayMean": histMeasLoss1DayMean,
       "histMeasLoss1DayHigh": histMeasLoss1DayHigh,
       "histMeasLoss1DayValidFlag": histMeasLoss1DayValidFlag,
       "histMeasLoss1DayTimeStamp": histMeasLoss1DayTimeStamp,
       "histMeasLoss1DayLength": histMeasLoss1DayLength,
       "histMeasLoss1DayLossPerKmLow": histMeasLoss1DayLossPerKmLow,
       "histMeasLoss1DayLossPerKmMean": histMeasLoss1DayLossPerKmMean,
       "histMeasLoss1DayLossPerKmHigh": histMeasLoss1DayLossPerKmHigh,
       "portThresTable": portThresTable,
       "portThresEntry": portThresEntry,
       "portThresDeviationFast": portThresDeviationFast,
       "portThresDeviationMedium": portThresDeviationMedium,
       "portThresDeviationSlow": portThresDeviationSlow,
       "portThresBudget": portThresBudget,
       "portThresCloseToBudget": portThresCloseToBudget,
       "portMonitorThresLossBudget": portMonitorThresLossBudget,
       "portMonitorThresDeviation": portMonitorThresDeviation,
       "portSensor1Thres": portSensor1Thres,
       "portSensor2Thres": portSensor2Thres,
       "portAutoThresAdjustment": portAutoThresAdjustment,
       "portThresBudgetMargin": portThresBudgetMargin,
       "portThresCloseToBudgetMargin": portThresCloseToBudgetMargin,
       "portThresAddDropHigh": portThresAddDropHigh,
       "portThresAddDropDeviation": portThresAddDropDeviation,
       "portPeriodLossDevTable": portPeriodLossDevTable,
       "portPeriodLossDevEntry": portPeriodLossDevEntry,
       "portPeriodLossDevFast": portPeriodLossDevFast,
       "portPeriodLossDevMedium": portPeriodLossDevMedium,
       "portPeriodLossDevSlow": portPeriodLossDevSlow,
       "measurementFpTable": measurementFpTable,
       "measurementFpEntry": measurementFpEntry,
       "measurementFpIndex": measurementFpIndex,
       "measurementFpRefractiveIndex": measurementFpRefractiveIndex,
       "measurementFpExternalOffset": measurementFpExternalOffset,
       "measurementFpCouplerLoss": measurementFpCouplerLoss,
       "measurementFpLinkLoss": measurementFpLinkLoss,
       "measurementFpLineEndPos": measurementFpLineEndPos,
       "measurementFpDataTimestamp": measurementFpDataTimestamp,
       "measurementFpNumConnectors": measurementFpNumConnectors,
       "measurementFpNumSplices": measurementFpNumSplices,
       "measurementFpMaxLaserPower": measurementFpMaxLaserPower,
       "measurementFpFastMode": measurementFpFastMode,
       "measurementFpMonitoringMode": measurementFpMonitoringMode,
       "measurementFpTrafficDetected": measurementFpTrafficDetected,
       "measurementFaTable": measurementFaTable,
       "measurementFaEntry": measurementFaEntry,
       "measurementFaIndex": measurementFaIndex,
       "measurementFaLinkLoss": measurementFaLinkLoss,
       "measurementFaFaultPos": measurementFaFaultPos,
       "measurementFaDeprecated": measurementFaDeprecated,
       "measurementFaDataTimestamp": measurementFaDataTimestamp,
       "measurementFaCorrectedFaultPos": measurementFaCorrectedFaultPos,
       "measurementFaFaultPosLatitude": measurementFaFaultPosLatitude,
       "measurementFaFaultPosLongitude": measurementFaFaultPosLongitude,
       "measurementOtdrTable": measurementOtdrTable,
       "measurementOtdrEntry": measurementOtdrEntry,
       "measurementOtdrIndex": measurementOtdrIndex,
       "measurementOtdrLength": measurementOtdrLength,
       "measurementOtdrExternalOffset": measurementOtdrExternalOffset,
       "measurementOtdrRefractiveIndex": measurementOtdrRefractiveIndex,
       "measurementOtdrPowerLevel": measurementOtdrPowerLevel,
       "measurementOtdrPulseWidth": measurementOtdrPulseWidth,
       "measurementOtdrAverageRate": measurementOtdrAverageRate,
       "measurementOtdrDataTimestamp": measurementOtdrDataTimestamp,
       "measurementOtdrMaxLaserPower": measurementOtdrMaxLaserPower,
       "measurementOtdrLinkLength": measurementOtdrLinkLength,
       "measurementOtdrMeasTime": measurementOtdrMeasTime,
       "measurementAutoFaTable": measurementAutoFaTable,
       "measurementAutoFaEntry": measurementAutoFaEntry,
       "measurementAutoFaIndex": measurementAutoFaIndex,
       "measurementAutoFaReference": measurementAutoFaReference,
       "measurementAutoFaLinkLoss": measurementAutoFaLinkLoss,
       "measurementAutoFaFaultPos": measurementAutoFaFaultPos,
       "measurementAutoFaDeprecated": measurementAutoFaDeprecated,
       "measurementAutoFaDataTimestamp": measurementAutoFaDataTimestamp,
       "measurementAutoFaCorrectedFaultPos": measurementAutoFaCorrectedFaultPos,
       "measurementAutoFaFaultPosLatitude": measurementAutoFaFaultPosLatitude,
       "measurementAutoFaFaultPosLongitude": measurementAutoFaFaultPosLongitude,
       "monitorPointLossTable": monitorPointLossTable,
       "monitorPointLossEntry": monitorPointLossEntry,
       "monitorPointLossCurrentLoss": monitorPointLossCurrentLoss,
       "monitorPointLossFpLoss": monitorPointLossFpLoss,
       "monitorPointLossDataTimestamp": monitorPointLossDataTimestamp,
       "histMonitorPointLoss15MinTable": histMonitorPointLoss15MinTable,
       "histMonitorPointLoss15MinEntry": histMonitorPointLoss15MinEntry,
       "histMonitorPointLoss15MinNumber": histMonitorPointLoss15MinNumber,
       "histMonitorPointLoss15MinLow": histMonitorPointLoss15MinLow,
       "histMonitorPointLoss15MinMean": histMonitorPointLoss15MinMean,
       "histMonitorPointLoss15MinHigh": histMonitorPointLoss15MinHigh,
       "histMonitorPointLoss15MinValid": histMonitorPointLoss15MinValid,
       "histMonitorPointLoss15MinTimeStamp": histMonitorPointLoss15MinTimeStamp,
       "histMonitorPointLoss1DayTable": histMonitorPointLoss1DayTable,
       "histMonitorPointLoss1DayEntry": histMonitorPointLoss1DayEntry,
       "histMonitorPointLoss1DayNumber": histMonitorPointLoss1DayNumber,
       "histMonitorPointLoss1DayLow": histMonitorPointLoss1DayLow,
       "histMonitorPointLoss1DayMean": histMonitorPointLoss1DayMean,
       "histMonitorPointLoss1DayHigh": histMonitorPointLoss1DayHigh,
       "histMonitorPointLoss1DayValid": histMonitorPointLoss1DayValid,
       "histMonitorPointLoss1DayTimeStamp": histMonitorPointLoss1DayTimeStamp,
       "measurementFpEventTable": measurementFpEventTable,
       "measurementFpEventEntry": measurementFpEventEntry,
       "measurementFpEventId": measurementFpEventId,
       "measurementFpEventPosition": measurementFpEventPosition,
       "measurementFpEventReflectance": measurementFpEventReflectance,
       "measurementFpEventAttenuation": measurementFpEventAttenuation,
       "measurementFpEventRemark": measurementFpEventRemark,
       "customizedFpEventTable": customizedFpEventTable,
       "customizedFpEventEntry": customizedFpEventEntry,
       "customizedFpEventId": customizedFpEventId,
       "customizedFpEventRowStatus": customizedFpEventRowStatus,
       "customizedFpEventCorrectedPosition": customizedFpEventCorrectedPosition,
       "customizedFpEventRemark": customizedFpEventRemark,
       "customizedFpEventOtdrId": customizedFpEventOtdrId,
       "customizedFpEventOtdrPosition": customizedFpEventOtdrPosition,
       "customizedFpEventLayoutId": customizedFpEventLayoutId,
       "mergedFpEventTable": mergedFpEventTable,
       "mergedFpEventEntry": mergedFpEventEntry,
       "mergedFpEventId": mergedFpEventId,
       "mergedFpEventCustomizedEventId": mergedFpEventCustomizedEventId,
       "mergedFpEventOtdrId": mergedFpEventOtdrId,
       "mergedFpEventCorrectedPosition": mergedFpEventCorrectedPosition,
       "mergedFpEventOtdrPosition": mergedFpEventOtdrPosition,
       "mergedFpEventRemark": mergedFpEventRemark,
       "linkLayoutEventTable": linkLayoutEventTable,
       "linkLayoutEventEntry": linkLayoutEventEntry,
       "linkLayoutEventId": linkLayoutEventId,
       "linkLayoutEventRowStatus": linkLayoutEventRowStatus,
       "linkLayoutEventMpId": linkLayoutEventMpId,
       "linkLayoutEventFpEventId": linkLayoutEventFpEventId,
       "linkLayoutEventCustomizedEventId": linkLayoutEventCustomizedEventId,
       "linkLayoutEventFaultPos": linkLayoutEventFaultPos,
       "linkLayoutEventCorrectedFaultPos": linkLayoutEventCorrectedFaultPos,
       "segmentTable": segmentTable,
       "segmentEntry": segmentEntry,
       "segmentId": segmentId,
       "segmentRowStatus": segmentRowStatus,
       "segmentStartEventId": segmentStartEventId,
       "segmentStopEventId": segmentStopEventId,
       "segmentStartCorrection": segmentStartCorrection,
       "segmentStopCorrection": segmentStopCorrection,
       "segmentRemark": segmentRemark,
       "segmentFpLength": segmentFpLength,
       "segmentFpLoss": segmentFpLoss,
       "segmentFpLossPerKm": segmentFpLossPerKm,
       "histSegmentTable": histSegmentTable,
       "histSegmentEntry": histSegmentEntry,
       "histSegmentNumber": histSegmentNumber,
       "histSegmentLength": histSegmentLength,
       "histSegmentLoss": histSegmentLoss,
       "histSegmentLossPerKm": histSegmentLossPerKm,
       "histSegmentUncertain": histSegmentUncertain,
       "histSegmentTimeStamp": histSegmentTimeStamp,
       "internalChannelLossTable": internalChannelLossTable,
       "internalChannelLossEntry": internalChannelLossEntry,
       "internalChannelLossValue": internalChannelLossValue,
       "internalChannelLossTimeStamp": internalChannelLossTimeStamp,
       "eventLogs": eventLogs,
       "eventsLogged": eventsLogged,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogTimeStamp": eventLogTimeStamp,
       "eventLogNotificationOID": eventLogNotificationOID,
       "eventLogIdentityTranslation": eventLogIdentityTranslation,
       "eventLogVarTable": eventLogVarTable,
       "eventLogVarEntry": eventLogVarEntry,
       "eventLogVarIndex": eventLogVarIndex,
       "eventLogVarId": eventLogVarId,
       "eventLogVarType": eventLogVarType,
       "eventLogVarInteger32Val": eventLogVarInteger32Val,
       "eventLogVarIpAddressVal": eventLogVarIpAddressVal,
       "eventLogVarOctetStringVal": eventLogVarOctetStringVal,
       "eventLogVarOidVal": eventLogVarOidVal,
       "eventLogVarCounter64Val": eventLogVarCounter64Val,
       "eventLogVarUnsigned32Val": eventLogVarUnsigned32Val,
       "trapsinkTable": trapsinkTable,
       "trapsinkEntry": trapsinkEntry,
       "trapsinkAddress": trapsinkAddress,
       "trapsinkPort": trapsinkPort,
       "trapsinkCommunity": trapsinkCommunity,
       "trapsinkRowStatus": trapsinkRowStatus,
       "trapsinkVersion": trapsinkVersion,
       "trapsinkUserName": trapsinkUserName,
       "trapsinkRemark": trapsinkRemark,
       "trapsinkLifetime": trapsinkLifetime,
       "ipv6TrapsinkTable": ipv6TrapsinkTable,
       "ipv6TrapsinkEntry": ipv6TrapsinkEntry,
       "ipv6TrapsinkId": ipv6TrapsinkId,
       "ipv6TrapsinkAddress": ipv6TrapsinkAddress,
       "ipv6TrapsinkPort": ipv6TrapsinkPort,
       "ipv6TrapsinkCommunity": ipv6TrapsinkCommunity,
       "ipv6TrapsinkRowStatus": ipv6TrapsinkRowStatus,
       "ipv6TrapsinkVersion": ipv6TrapsinkVersion,
       "ipv6TrapsinkUserName": ipv6TrapsinkUserName,
       "ipv6TrapsinkRemark": ipv6TrapsinkRemark,
       "ipv6TrapsinkLifetime": ipv6TrapsinkLifetime,
       "sysLogRecipients": sysLogRecipients,
       "sysLogRecipient1Address": sysLogRecipient1Address,
       "sysLogRecipient2Address": sysLogRecipient2Address,
       "sysLogRecipient3Address": sysLogRecipient3Address,
       "dnsTrapsinkTable": dnsTrapsinkTable,
       "dnsTrapsinkEntry": dnsTrapsinkEntry,
       "dnsTrapsinkId": dnsTrapsinkId,
       "dnsTrapsinkHostName": dnsTrapsinkHostName,
       "dnsTrapsinkPort": dnsTrapsinkPort,
       "dnsTrapsinkCommunity": dnsTrapsinkCommunity,
       "dnsTrapsinkRowStatus": dnsTrapsinkRowStatus,
       "dnsTrapsinkVersion": dnsTrapsinkVersion,
       "dnsTrapsinkUserName": dnsTrapsinkUserName,
       "dnsTrapsinkRemark": dnsTrapsinkRemark,
       "dnsTrapsinkLifetime": dnsTrapsinkLifetime,
       "sysLogFacility": sysLogFacility,
       "system": system,
       "information": information,
       "softwareVersion": softwareVersion,
       "localDateAndTime": localDateAndTime,
       "releaseNumber": releaseNumber,
       "expectedSoftwareVersion": expectedSoftwareVersion,
       "ipSettings": ipSettings,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "dns1": dns1,
       "dns2": dns2,
       "dhcp": dhcp,
       "ipv6Address": ipv6Address,
       "ipv6Dns1": ipv6Dns1,
       "ipv6Dns2": ipv6Dns2,
       "ipSettingsUsb": ipSettingsUsb,
       "ipSettingsUsbMode": ipSettingsUsbMode,
       "ipSettingsUsbMobileDialInNumber": ipSettingsUsbMobileDialInNumber,
       "ipSettingsUsbMobileAPN": ipSettingsUsbMobileAPN,
       "ipSettingsUsbMobileUserName": ipSettingsUsbMobileUserName,
       "ipSettingsUsbMobileUserPassword": ipSettingsUsbMobileUserPassword,
       "ipSettingsUsbMobileSIMPin": ipSettingsUsbMobileSIMPin,
       "ipSettingsUsbMobileIPAddress": ipSettingsUsbMobileIPAddress,
       "ipSettingsUsbMobileRoutingNetAddress": ipSettingsUsbMobileRoutingNetAddress,
       "ipSettingsUsbMobileRoutingNetMask": ipSettingsUsbMobileRoutingNetMask,
       "ipSettingsUsbLanAdapterIPAddress": ipSettingsUsbLanAdapterIPAddress,
       "ipSettingsUsbLanAdapterSubnetMask": ipSettingsUsbLanAdapterSubnetMask,
       "ipSettingsUsbLanAdapterGateway": ipSettingsUsbLanAdapterGateway,
       "ipSettingsUsbLanAdapterRoutingNetAddress": ipSettingsUsbLanAdapterRoutingNetAddress,
       "ipSettingsUsbLanAdapterRoutingNetMask": ipSettingsUsbLanAdapterRoutingNetMask,
       "ethernetPortTable": ethernetPortTable,
       "ethernetPortEntry": ethernetPortEntry,
       "ethernetPortId": ethernetPortId,
       "ethernetPortIdentifier": ethernetPortIdentifier,
       "ethernetPortMode": ethernetPortMode,
       "ethernetPortBitrate": ethernetPortBitrate,
       "ethernetPortDuplex": ethernetPortDuplex,
       "ethernetPortMtu": ethernetPortMtu,
       "softwareMgmt": softwareMgmt,
       "softwareMgmtFileTable": softwareMgmtFileTable,
       "softwareMgmtFileEntry": softwareMgmtFileEntry,
       "softwareMgmtFileIndex": softwareMgmtFileIndex,
       "softwareMgmtFileSize": softwareMgmtFileSize,
       "softwareMgmtFileCreationTime": softwareMgmtFileCreationTime,
       "softwareMgmtFileVersion": softwareMgmtFileVersion,
       "softwareMgmtFileFileName": softwareMgmtFileFileName,
       "softwareMgmtFileRowStatus": softwareMgmtFileRowStatus,
       "softwareMgmtRequest": softwareMgmtRequest,
       "softwareMgmtState": softwareMgmtState,
       "softwareMgmtLastError": softwareMgmtLastError,
       "softwareMgmtDatabaseUsage": softwareMgmtDatabaseUsage,
       "softwareMgmtDatabaseFileName": softwareMgmtDatabaseFileName,
       "softwareMgmtServerAddress": softwareMgmtServerAddress,
       "softwareMgmtServerLogin": softwareMgmtServerLogin,
       "softwareMgmtServerPasswd": softwareMgmtServerPasswd,
       "softwareMgmtServerDirectory": softwareMgmtServerDirectory,
       "softwareMgmtFileName": softwareMgmtFileName,
       "softwareMgmtTransferProtocol": softwareMgmtTransferProtocol,
       "softwareMgmtFtpPort": softwareMgmtFtpPort,
       "softwareMgmtActionProgress": softwareMgmtActionProgress,
       "softwareMgmtIpv6Address": softwareMgmtIpv6Address,
       "softwareMgmtScpPort": softwareMgmtScpPort,
       "softwareMgmtBackupPassword": softwareMgmtBackupPassword,
       "databaseMgmt": databaseMgmt,
       "databaseMgmtFileTable": databaseMgmtFileTable,
       "databaseMgmtFileEntry": databaseMgmtFileEntry,
       "databaseMgmtFileIndex": databaseMgmtFileIndex,
       "databaseMgmtFileSize": databaseMgmtFileSize,
       "databaseMgmtFileCreationTime": databaseMgmtFileCreationTime,
       "databaseMgmtFileVersion": databaseMgmtFileVersion,
       "databaseMgmtFileFileName": databaseMgmtFileFileName,
       "databaseMgmtFileRowStatus": databaseMgmtFileRowStatus,
       "databaseMgmtRequest": databaseMgmtRequest,
       "databaseMgmtState": databaseMgmtState,
       "databaseMgmtLastError": databaseMgmtLastError,
       "databaseMgmtServerAddress": databaseMgmtServerAddress,
       "databaseMgmtServerLogin": databaseMgmtServerLogin,
       "databaseMgmtServerPasswd": databaseMgmtServerPasswd,
       "databaseMgmtServerDirectory": databaseMgmtServerDirectory,
       "databaseMgmtFileName": databaseMgmtFileName,
       "databaseMgmtTransferProtocol": databaseMgmtTransferProtocol,
       "databaseMgmtFtpPort": databaseMgmtFtpPort,
       "databaseMgmtActionProgress": databaseMgmtActionProgress,
       "databaseMgmtIpv6Address": databaseMgmtIpv6Address,
       "databaseMgmtScpPort": databaseMgmtScpPort,
       "databaseMgmtBackupPassword": databaseMgmtBackupPassword,
       "ntpMgmt": ntpMgmt,
       "ntpClientConfig": ntpClientConfig,
       "ntpServerName": ntpServerName,
       "ntpServerName2": ntpServerName2,
       "ntpServerName3": ntpServerName3,
       "ntpTimeChangeReason": ntpTimeChangeReason,
       "generalSettings": generalSettings,
       "operationMode": operationMode,
       "httpsPort": httpsPort,
       "access": access,
       "sshInterface": sshInterface,
       "netconfInterface": netconfInterface,
       "sshPasswordAuthentication": sshPasswordAuthentication,
       "generalSessionTimeout": generalSessionTimeout,
       "snmpSessionTimeout": snmpSessionTimeout,
       "maxLoginFailureDelay": maxLoginFailureDelay,
       "passwordStrength": passwordStrength,
       "userInfoDeletionPeriod": userInfoDeletionPeriod,
       "defaultTrapsinkLifetime": defaultTrapsinkLifetime,
       "pki": pki,
       "caTable": caTable,
       "caEntry": caEntry,
       "caId": caId,
       "caRowStatus": caRowStatus,
       "caAlias": caAlias,
       "caScepUrl": caScepUrl,
       "caScepDomainName": caScepDomainName,
       "caScepUserName": caScepUserName,
       "caScepPassword": caScepPassword,
       "caScepCertValidation": caScepCertValidation,
       "caScepQueryMessage": caScepQueryMessage,
       "caScepCipherAlgorithm": caScepCipherAlgorithm,
       "caScepDigestAlgorithm": caScepDigestAlgorithm,
       "caScepRequestMethod": caScepRequestMethod,
       "keyTable": keyTable,
       "keyEntry": keyEntry,
       "keyId": keyId,
       "keyRowStatus": keyRowStatus,
       "keyAlias": keyAlias,
       "keyProfile": keyProfile,
       "keyAlgorithm": keyAlgorithm,
       "keyLength": keyLength,
       "keySha1": keySha1,
       "keySha256": keySha256,
       "keyCertCommonName": keyCertCommonName,
       "keyCertAlternativeNameIp": keyCertAlternativeNameIp,
       "keyCertAlternativeNameDns": keyCertAlternativeNameDns,
       "keyCertKeyUsage": keyCertKeyUsage,
       "keyCertExtKeyUsage": keyCertExtKeyUsage,
       "keyCertValidityPeriod": keyCertValidityPeriod,
       "keyCertRequestChallenge": keyCertRequestChallenge,
       "keyCertRenewMode": keyCertRenewMode,
       "keyCertRenewInterval": keyCertRenewInterval,
       "keyCertRenewRetryInterval": keyCertRenewRetryInterval,
       "keyCertRenewDate": keyCertRenewDate,
       "keyCertWarnInterval": keyCertWarnInterval,
       "keyCertRequest": keyCertRequest,
       "keyCertRequestStatus": keyCertRequestStatus,
       "keyCaEntity": keyCaEntity,
       "keyCertificates": keyCertificates,
       "certificateTable": certificateTable,
       "certificateEntry": certificateEntry,
       "certificateId": certificateId,
       "certificateType": certificateType,
       "certificateValidityStatus": certificateValidityStatus,
       "certificatePurpose": certificatePurpose,
       "certificateStatus": certificateStatus,
       "certificateIssuer": certificateIssuer,
       "certificateSerialNo": certificateSerialNo,
       "certificateSubject": certificateSubject,
       "certificateCommonName": certificateCommonName,
       "certificateValidFrom": certificateValidFrom,
       "certificateValidTo": certificateValidTo,
       "certificateSignAlgorithm": certificateSignAlgorithm,
       "certificateSha1": certificateSha1,
       "certificateSha256": certificateSha256,
       "certificateAlternativeNameIp": certificateAlternativeNameIp,
       "certificateAlternativeNameDns": certificateAlternativeNameDns,
       "certificateKeyUsage": certificateKeyUsage,
       "certificateExtKeyUsage": certificateExtKeyUsage,
       "certificateBasicConstraints": certificateBasicConstraints,
       "certificateCrlDistrPoints": certificateCrlDistrPoints,
       "certificateCaEntity": certificateCaEntity,
       "certificateKeyEntity": certificateKeyEntity,
       "emailNotifySettings": emailNotifySettings,
       "emailNotifyConfig": emailNotifyConfig,
       "smtpServerName": smtpServerName,
       "smtpServerPort": smtpServerPort,
       "smtpServerConnectionSecurity": smtpServerConnectionSecurity,
       "smtpServerAuthConfig": smtpServerAuthConfig,
       "smtpServerAccount": smtpServerAccount,
       "smtpServerPasswd": smtpServerPasswd,
       "emailRecipientTable": emailRecipientTable,
       "emailRecipientEntry": emailRecipientEntry,
       "emailRecipientId": emailRecipientId,
       "emailRecipientAddress": emailRecipientAddress,
       "emailRecipientType": emailRecipientType,
       "emailRecipientRowStatus": emailRecipientRowStatus,
       "emailRecipientFormat": emailRecipientFormat,
       "emailRecipientMinSeverity": emailRecipientMinSeverity,
       "emailRecipientAttachment": emailRecipientAttachment,
       "externalIdTable": externalIdTable,
       "externalIdEntry": externalIdEntry,
       "externalId": externalId,
       "smtpSenderAddress": smtpSenderAddress,
       "smtpExtendedHello": smtpExtendedHello,
       "advaSecurity": advaSecurity,
       "authTrapUserName": authTrapUserName,
       "authTrapLctIp": authTrapLctIp,
       "authTrapStatus": authTrapStatus,
       "authTrapSessionId": authTrapSessionId,
       "authTrapProtocol": authTrapProtocol,
       "authTrapSuccessfulAuthCount": authTrapSuccessfulAuthCount,
       "authTrapUnsuccessfulAuthCount": authTrapUnsuccessfulAuthCount,
       "authTrapLogoutCount": authTrapLogoutCount,
       "authTrapLctIpv6": authTrapLctIpv6,
       "lossGuidance": lossGuidance,
       "lossGuidanceConfig": lossGuidanceConfig,
       "minLoss": minLoss,
       "alwDev": alwDev,
       "lossKm": lossKm,
       "lossConnectors": lossConnectors,
       "lossSplices": lossSplices,
       "numConnectors": numConnectors,
       "numSplices": numSplices,
       "userManagement": userManagement,
       "userManagementTable": userManagementTable,
       "userManagementEntry": userManagementEntry,
       "userManagementRowStatus": userManagementRowStatus,
       "userManagementUsername": userManagementUsername,
       "userManagementEmailAddress": userManagementEmailAddress,
       "userManagementPrivilegeLevel": userManagementPrivilegeLevel,
       "userManagementSecurityLevel": userManagementSecurityLevel,
       "userManagementAuthPrivKey": userManagementAuthPrivKey,
       "userManagementAuthPrivKeyOld": userManagementAuthPrivKeyOld,
       "userManagementUdpSessionStatus": userManagementUdpSessionStatus,
       "userManagementSso2fa": userManagementSso2fa,
       "userManagementSnmpAuthProtocol": userManagementSnmpAuthProtocol,
       "userManagementPrivacyKeyType": userManagementPrivacyKeyType,
       "userManagementPrivacyKey": userManagementPrivacyKey,
       "exportMgmt": exportMgmt,
       "exportMgmtRequest": exportMgmtRequest,
       "exportMgmtState": exportMgmtState,
       "exportMgmtLastError": exportMgmtLastError,
       "exportMgmtServerAddress": exportMgmtServerAddress,
       "exportMgmtServerLogin": exportMgmtServerLogin,
       "exportMgmtServerPasswd": exportMgmtServerPasswd,
       "exportMgmtServerDirectory": exportMgmtServerDirectory,
       "exportMgmtFileName": exportMgmtFileName,
       "exportMgmtTransferProtocol": exportMgmtTransferProtocol,
       "exportMgmtFtpPort": exportMgmtFtpPort,
       "exportMgmtActionProgress": exportMgmtActionProgress,
       "exportMgmtIpv6Address": exportMgmtIpv6Address,
       "exportMgmtScpPort": exportMgmtScpPort,
       "bidirSettings": bidirSettings,
       "bidirSettingsTimeSlotConfig": bidirSettingsTimeSlotConfig,
       "bidirSettingsInactiveUserCmds": bidirSettingsInactiveUserCmds,
       "dwdmExtraWaitTimeSlot": dwdmExtraWaitTimeSlot,
       "remoteAuth": remoteAuth,
       "authmode": authmode,
       "loginmode": loginmode,
       "sso2fa": sso2fa,
       "remoteAuthServersTable": remoteAuthServersTable,
       "remoteAuthServersEntry": remoteAuthServersEntry,
       "remoteAuthServersId": remoteAuthServersId,
       "remoteAuthServersIpAddress": remoteAuthServersIpAddress,
       "remoteAuthServersPort": remoteAuthServersPort,
       "remoteAuthServersSecret": remoteAuthServersSecret,
       "remoteAuthServersTimeout": remoteAuthServersTimeout,
       "remoteAuthServersActive": remoteAuthServersActive,
       "prioSettings": prioSettings,
       "prioSettingsConfig": prioSettingsConfig,
       "maintain": maintain,
       "maintainTable": maintainTable,
       "maintainEntry": maintainEntry,
       "maintainOperationRequest": maintainOperationRequest,
       "maintainOperationRefractiveIndex": maintainOperationRefractiveIndex,
       "maintainOperationExternalOffset": maintainOperationExternalOffset,
       "maintainOperationCouplerLoss": maintainOperationCouplerLoss,
       "maintainOperationOtdrLength": maintainOperationOtdrLength,
       "maintainOperationOtdrPowerLevel": maintainOperationOtdrPowerLevel,
       "maintainOperationOtdrPulseWidth": maintainOperationOtdrPulseWidth,
       "maintainOperationOtdrAverageRate": maintainOperationOtdrAverageRate,
       "maintainOperationState": maintainOperationState,
       "maintainOperationLastError": maintainOperationLastError,
       "maintainOperationNumConnectors": maintainOperationNumConnectors,
       "maintainOperationNumSplices": maintainOperationNumSplices,
       "maintainOperationMaxLaserPower": maintainOperationMaxLaserPower,
       "maintainOperationOtdrLinkLength": maintainOperationOtdrLinkLength,
       "maintainOperationOtdrMeasTime": maintainOperationOtdrMeasTime,
       "maintainOperationDwdmMode": maintainOperationDwdmMode,
       "maintainOperationLossCalculationPoint": maintainOperationLossCalculationPoint,
       "maintainOperationFastMode": maintainOperationFastMode,
       "maintainOperationMonitoringMode": maintainOperationMonitoringMode,
       "maintainOperationExpectedLoss": maintainOperationExpectedLoss,
       "scheduleFaTable": scheduleFaTable,
       "scheduleFaEntry": scheduleFaEntry,
       "scheduleFaFirstRun": scheduleFaFirstRun,
       "scheduleFaInterval": scheduleFaInterval,
       "scheduleFaRequiredState": scheduleFaRequiredState,
       "scheduleFaNextRun": scheduleFaNextRun,
       "scheduleFaLastRun": scheduleFaLastRun,
       "scheduleFaStatus": scheduleFaStatus,
       "otdrTraceMgmt": otdrTraceMgmt,
       "otdrTraceMgmtTable": otdrTraceMgmtTable,
       "otdrTraceMgmtEntry": otdrTraceMgmtEntry,
       "otdrTraceMgmtRequest": otdrTraceMgmtRequest,
       "otdrTraceMgmtState": otdrTraceMgmtState,
       "otdrTraceMgmtLastError": otdrTraceMgmtLastError,
       "otdrTraceMgmtServerAddress": otdrTraceMgmtServerAddress,
       "otdrTraceMgmtServerLogin": otdrTraceMgmtServerLogin,
       "otdrTraceMgmtServerPasswd": otdrTraceMgmtServerPasswd,
       "otdrTraceMgmtServerDirectory": otdrTraceMgmtServerDirectory,
       "otdrTraceMgmtFileName": otdrTraceMgmtFileName,
       "otdrTraceMgmtTransferProtocol": otdrTraceMgmtTransferProtocol,
       "otdrTraceMgmtFtpPort": otdrTraceMgmtFtpPort,
       "otdrTraceMgmtActionProgress": otdrTraceMgmtActionProgress,
       "otdrTraceMgmtAutoFaReference": otdrTraceMgmtAutoFaReference,
       "otdrTraceMgmtIpv6Address": otdrTraceMgmtIpv6Address,
       "otdrTraceMgmtScpPort": otdrTraceMgmtScpPort,
       "inventory": inventory,
       "inventoryTable": inventoryTable,
       "inventoryEntry": inventoryEntry,
       "inventoryShelfNo": inventoryShelfNo,
       "inventorySlotNo": inventorySlotNo,
       "inventoryPortNo": inventoryPortNo,
       "inventoryExtNo": inventoryExtNo,
       "inventoryClassName": inventoryClassName,
       "inventoryAidString": inventoryAidString,
       "inventoryUnitName": inventoryUnitName,
       "inventoryFirmwarePackageRev": inventoryFirmwarePackageRev,
       "inventoryHardwareRev": inventoryHardwareRev,
       "inventoryFpgaRev": inventoryFpgaRev,
       "inventorySerialNumber": inventorySerialNumber,
       "inventoryPartNumber": inventoryPartNumber,
       "inventoryCleiCode": inventoryCleiCode,
       "inventoryOrigin": inventoryOrigin,
       "inventoryShelfType": inventoryShelfType,
       "inventoryUniversalSerialIdent": inventoryUniversalSerialIdent}
)
