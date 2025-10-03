# SNMP MIB module (ALU-MICROWAVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALU-MICROWAVE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:14:37 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex")

(TmnxPortOperStatus,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxPortOperStatus")

(TNamedItemOrEmpty,
 TmnxActionType,
 TmnxDisplayStringURL,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxDisplayStringURL",
    "TmnxPortID")


# MODULE-IDENTITY

aluMwMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    aluMwMIBModule.setRevisions(
        ("1908-01-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluMwLinkID(TextualConvention, Unsigned32):
    status = "current"


class AluMwLinkRadioActivity(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("mainRadio", 2),
          ("spareRadio", 3),
          ("bothActive", 4))
    )



class AluMwLinkRevertiveness(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("revertive", 2),
          ("nonRevertive", 3))
    )



class AluMwLinkMaintenanceOp(TextualConvention, Integer32):
    status = "current"
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
          ("lockout", 1),
          ("forced", 2),
          ("manual", 3))
    )



class AluMwRadioSwState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("dwnldRequested", 1),
          ("dwnldForced", 2),
          ("inProgress", 3),
          ("ready", 4),
          ("ok", 5),
          ("mismatch", 6),
          ("dwnldFailed", 7))
    )



class AluMwPerfMonSection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radioHop", 0),
          ("radioLink", 1))
    )



class AluMwPerfMonPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinute", 0),
          ("twentyFourHour", 1))
    )



class AluMwPerfMonBin(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 96),
    )



class AluMwPerfMonEPSState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("active", 1),
          ("notRelevant", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluMwMIBConformance_ObjectIdentity = ObjectIdentity
aluMwMIBConformance = _AluMwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7)
)
_AluMwConformance_ObjectIdentity = ObjectIdentity
aluMwConformance = _AluMwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1)
)
_AluMwCompliances_ObjectIdentity = ObjectIdentity
aluMwCompliances = _AluMwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 1)
)
_AluMwComp7705_ObjectIdentity = ObjectIdentity
aluMwComp7705 = _AluMwComp7705_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 1, 1)
)
_AluMwGroups_ObjectIdentity = ObjectIdentity
aluMwGroups = _AluMwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2)
)
_AluMwObjPrefix_ObjectIdentity = ObjectIdentity
aluMwObjPrefix = _AluMwObjPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7)
)
_AluMwObjs_ObjectIdentity = ObjectIdentity
aluMwObjs = _AluMwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1)
)
_AluMwLinkTable_Object = MibTable
aluMwLinkTable = _AluMwLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    aluMwLinkTable.setStatus("current")
_AluMwLinkEntry_Object = MibTableRow
aluMwLinkEntry = _AluMwLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1)
)
aluMwLinkEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwLinkID"),
)
if mibBuilder.loadTexts:
    aluMwLinkEntry.setStatus("current")
_AluMwLinkID_Type = AluMwLinkID
_AluMwLinkID_Object = MibTableColumn
aluMwLinkID = _AluMwLinkID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 1),
    _AluMwLinkID_Type()
)
aluMwLinkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluMwLinkID.setStatus("current")
_AluMwLinkRowStatus_Type = RowStatus
_AluMwLinkRowStatus_Object = MibTableColumn
aluMwLinkRowStatus = _AluMwLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 2),
    _AluMwLinkRowStatus_Type()
)
aluMwLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkRowStatus.setStatus("current")


class _AluMwLinkOperFlags_Type(Bits):
    """Custom type aluMwLinkOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("noRadioCfg", 0),
          ("linkAdminDown", 1),
          ("noRadiosPresent", 2),
          ("noRadiosReady", 3),
          ("incompatibleConfig", 4),
          ("radioFailure", 5),
          ("receptionFailure", 6),
          ("di", 7),
          ("txMuted", 8))
    )

_AluMwLinkOperFlags_Type.__name__ = "Bits"
_AluMwLinkOperFlags_Object = MibTableColumn
aluMwLinkOperFlags = _AluMwLinkOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 3),
    _AluMwLinkOperFlags_Type()
)
aluMwLinkOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkOperFlags.setStatus("current")


class _AluMwLinkRadioScheme_Type(Integer32):
    """Custom type aluMwLinkRadioScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("onePlusZero", 1),
          ("onePlusOneHSB", 2))
    )


_AluMwLinkRadioScheme_Type.__name__ = "Integer32"
_AluMwLinkRadioScheme_Object = MibTableColumn
aluMwLinkRadioScheme = _AluMwLinkRadioScheme_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 4),
    _AluMwLinkRadioScheme_Type()
)
aluMwLinkRadioScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkRadioScheme.setStatus("current")


class _AluMwLinkAlarmState_Type(Integer32):
    """Custom type aluMwLinkAlarmState based on Integer32"""
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
        *(("ok", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("inderminate", 5),
          ("notSupported", 6),
          ("unknown", 7))
    )


_AluMwLinkAlarmState_Type.__name__ = "Integer32"
_AluMwLinkAlarmState_Object = MibTableColumn
aluMwLinkAlarmState = _AluMwLinkAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 5),
    _AluMwLinkAlarmState_Type()
)
aluMwLinkAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmState.setStatus("current")
_AluMwLinkAlarmsCritical_Type = Integer32
_AluMwLinkAlarmsCritical_Object = MibTableColumn
aluMwLinkAlarmsCritical = _AluMwLinkAlarmsCritical_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 6),
    _AluMwLinkAlarmsCritical_Type()
)
aluMwLinkAlarmsCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsCritical.setStatus("current")
_AluMwLinkAlarmsMajor_Type = Integer32
_AluMwLinkAlarmsMajor_Object = MibTableColumn
aluMwLinkAlarmsMajor = _AluMwLinkAlarmsMajor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 7),
    _AluMwLinkAlarmsMajor_Type()
)
aluMwLinkAlarmsMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsMajor.setStatus("current")
_AluMwLinkAlarmsMinor_Type = Integer32
_AluMwLinkAlarmsMinor_Object = MibTableColumn
aluMwLinkAlarmsMinor = _AluMwLinkAlarmsMinor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 8),
    _AluMwLinkAlarmsMinor_Type()
)
aluMwLinkAlarmsMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsMinor.setStatus("current")
_AluMwLinkAlarmsWarning_Type = Integer32
_AluMwLinkAlarmsWarning_Object = MibTableColumn
aluMwLinkAlarmsWarning = _AluMwLinkAlarmsWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 9),
    _AluMwLinkAlarmsWarning_Type()
)
aluMwLinkAlarmsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsWarning.setStatus("current")
_AluMwLinkAlarmsInd_Type = Integer32
_AluMwLinkAlarmsInd_Object = MibTableColumn
aluMwLinkAlarmsInd = _AluMwLinkAlarmsInd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 10),
    _AluMwLinkAlarmsInd_Type()
)
aluMwLinkAlarmsInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsInd.setStatus("current")
_AluMwLinkAlarmsCommunication_Type = Integer32
_AluMwLinkAlarmsCommunication_Object = MibTableColumn
aluMwLinkAlarmsCommunication = _AluMwLinkAlarmsCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 11),
    _AluMwLinkAlarmsCommunication_Type()
)
aluMwLinkAlarmsCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsCommunication.setStatus("current")
_AluMwLinkAlarmsEquipment_Type = Integer32
_AluMwLinkAlarmsEquipment_Object = MibTableColumn
aluMwLinkAlarmsEquipment = _AluMwLinkAlarmsEquipment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 12),
    _AluMwLinkAlarmsEquipment_Type()
)
aluMwLinkAlarmsEquipment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAlarmsEquipment.setStatus("current")


class _AluMwLinkEPSActivity_Type(AluMwLinkRadioActivity):
    """Custom type aluMwLinkEPSActivity based on AluMwLinkRadioActivity"""
    defaultValue = 1


_AluMwLinkEPSActivity_Type.__name__ = "AluMwLinkRadioActivity"
_AluMwLinkEPSActivity_Object = MibTableColumn
aluMwLinkEPSActivity = _AluMwLinkEPSActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 13),
    _AluMwLinkEPSActivity_Type()
)
aluMwLinkEPSActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkEPSActivity.setStatus("current")


class _AluMwLinkTPSActivity_Type(AluMwLinkRadioActivity):
    """Custom type aluMwLinkTPSActivity based on AluMwLinkRadioActivity"""
    defaultValue = 1


_AluMwLinkTPSActivity_Type.__name__ = "AluMwLinkRadioActivity"
_AluMwLinkTPSActivity_Object = MibTableColumn
aluMwLinkTPSActivity = _AluMwLinkTPSActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 14),
    _AluMwLinkTPSActivity_Type()
)
aluMwLinkTPSActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkTPSActivity.setStatus("current")


class _AluMwLinkRPSActivity_Type(AluMwLinkRadioActivity):
    """Custom type aluMwLinkRPSActivity based on AluMwLinkRadioActivity"""
    defaultValue = 1


_AluMwLinkRPSActivity_Type.__name__ = "AluMwLinkRadioActivity"
_AluMwLinkRPSActivity_Object = MibTableColumn
aluMwLinkRPSActivity = _AluMwLinkRPSActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 15),
    _AluMwLinkRPSActivity_Type()
)
aluMwLinkRPSActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkRPSActivity.setStatus("current")


class _AluMwLinkEPSRevertiveness_Type(AluMwLinkRevertiveness):
    """Custom type aluMwLinkEPSRevertiveness based on AluMwLinkRevertiveness"""
    defaultValue = 1


_AluMwLinkEPSRevertiveness_Type.__name__ = "AluMwLinkRevertiveness"
_AluMwLinkEPSRevertiveness_Object = MibTableColumn
aluMwLinkEPSRevertiveness = _AluMwLinkEPSRevertiveness_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 16),
    _AluMwLinkEPSRevertiveness_Type()
)
aluMwLinkEPSRevertiveness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkEPSRevertiveness.setStatus("current")


class _AluMwLinkTPSRevertiveness_Type(AluMwLinkRevertiveness):
    """Custom type aluMwLinkTPSRevertiveness based on AluMwLinkRevertiveness"""
    defaultValue = 1


_AluMwLinkTPSRevertiveness_Type.__name__ = "AluMwLinkRevertiveness"
_AluMwLinkTPSRevertiveness_Object = MibTableColumn
aluMwLinkTPSRevertiveness = _AluMwLinkTPSRevertiveness_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 17),
    _AluMwLinkTPSRevertiveness_Type()
)
aluMwLinkTPSRevertiveness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkTPSRevertiveness.setStatus("current")


class _AluMwLinkRPSRevertiveness_Type(AluMwLinkRevertiveness):
    """Custom type aluMwLinkRPSRevertiveness based on AluMwLinkRevertiveness"""
    defaultValue = 1


_AluMwLinkRPSRevertiveness_Type.__name__ = "AluMwLinkRevertiveness"
_AluMwLinkRPSRevertiveness_Object = MibTableColumn
aluMwLinkRPSRevertiveness = _AluMwLinkRPSRevertiveness_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 18),
    _AluMwLinkRPSRevertiveness_Type()
)
aluMwLinkRPSRevertiveness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkRPSRevertiveness.setStatus("current")


class _AluMwLinkEPSMainMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkEPSMainMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkEPSMainMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkEPSMainMaintOp_Object = MibTableColumn
aluMwLinkEPSMainMaintOp = _AluMwLinkEPSMainMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 19),
    _AluMwLinkEPSMainMaintOp_Type()
)
aluMwLinkEPSMainMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkEPSMainMaintOp.setStatus("current")


class _AluMwLinkEPSSpareMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkEPSSpareMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkEPSSpareMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkEPSSpareMaintOp_Object = MibTableColumn
aluMwLinkEPSSpareMaintOp = _AluMwLinkEPSSpareMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 20),
    _AluMwLinkEPSSpareMaintOp_Type()
)
aluMwLinkEPSSpareMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkEPSSpareMaintOp.setStatus("current")


class _AluMwLinkTPSMainMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkTPSMainMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkTPSMainMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkTPSMainMaintOp_Object = MibTableColumn
aluMwLinkTPSMainMaintOp = _AluMwLinkTPSMainMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 21),
    _AluMwLinkTPSMainMaintOp_Type()
)
aluMwLinkTPSMainMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkTPSMainMaintOp.setStatus("current")


class _AluMwLinkTPSSpareMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkTPSSpareMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkTPSSpareMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkTPSSpareMaintOp_Object = MibTableColumn
aluMwLinkTPSSpareMaintOp = _AluMwLinkTPSSpareMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 22),
    _AluMwLinkTPSSpareMaintOp_Type()
)
aluMwLinkTPSSpareMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkTPSSpareMaintOp.setStatus("current")


class _AluMwLinkRPSMainMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkRPSMainMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkRPSMainMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkRPSMainMaintOp_Object = MibTableColumn
aluMwLinkRPSMainMaintOp = _AluMwLinkRPSMainMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 23),
    _AluMwLinkRPSMainMaintOp_Type()
)
aluMwLinkRPSMainMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkRPSMainMaintOp.setStatus("current")


class _AluMwLinkRPSSpareMaintOp_Type(AluMwLinkMaintenanceOp):
    """Custom type aluMwLinkRPSSpareMaintOp based on AluMwLinkMaintenanceOp"""
    defaultValue = 0


_AluMwLinkRPSSpareMaintOp_Type.__name__ = "AluMwLinkMaintenanceOp"
_AluMwLinkRPSSpareMaintOp_Object = MibTableColumn
aluMwLinkRPSSpareMaintOp = _AluMwLinkRPSSpareMaintOp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 24),
    _AluMwLinkRPSSpareMaintOp_Type()
)
aluMwLinkRPSSpareMaintOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkRPSSpareMaintOp.setStatus("current")
_AluMwLinkPeerID_Type = AluMwLinkID
_AluMwLinkPeerID_Object = MibTableColumn
aluMwLinkPeerID = _AluMwLinkPeerID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 25),
    _AluMwLinkPeerID_Type()
)
aluMwLinkPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkPeerID.setStatus("current")
_AluMwLinkPeerNEIpAddress_Type = IpAddress
_AluMwLinkPeerNEIpAddress_Object = MibTableColumn
aluMwLinkPeerNEIpAddress = _AluMwLinkPeerNEIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 26),
    _AluMwLinkPeerNEIpAddress_Type()
)
aluMwLinkPeerNEIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkPeerNEIpAddress.setStatus("current")


class _AluMwLinkClearStatistics_Type(TmnxActionType):
    """Custom type aluMwLinkClearStatistics based on TmnxActionType"""
    defaultValue = 2


_AluMwLinkClearStatistics_Type.__name__ = "TmnxActionType"
_AluMwLinkClearStatistics_Object = MibTableColumn
aluMwLinkClearStatistics = _AluMwLinkClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 27),
    _AluMwLinkClearStatistics_Type()
)
aluMwLinkClearStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkClearStatistics.setStatus("current")


class _AluMwLinkPeerDiscovery_Type(TruthValue):
    """Custom type aluMwLinkPeerDiscovery based on TruthValue"""
    defaultValue = 1


_AluMwLinkPeerDiscovery_Type.__name__ = "TruthValue"
_AluMwLinkPeerDiscovery_Object = MibTableColumn
aluMwLinkPeerDiscovery = _AluMwLinkPeerDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 1, 1, 28),
    _AluMwLinkPeerDiscovery_Type()
)
aluMwLinkPeerDiscovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwLinkPeerDiscovery.setStatus("current")
_AluMwRadioTable_Object = MibTable
aluMwRadioTable = _AluMwRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    aluMwRadioTable.setStatus("current")
_AluMwRadioEntry_Object = MibTableRow
aluMwRadioEntry = _AluMwRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1)
)
aluMwRadioEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
)
if mibBuilder.loadTexts:
    aluMwRadioEntry.setStatus("current")
_AluMwRadioPortID_Type = TmnxPortID
_AluMwRadioPortID_Object = MibTableColumn
aluMwRadioPortID = _AluMwRadioPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 1),
    _AluMwRadioPortID_Type()
)
aluMwRadioPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluMwRadioPortID.setStatus("current")
_AluMwRadioRowStatus_Type = RowStatus
_AluMwRadioRowStatus_Object = MibTableColumn
aluMwRadioRowStatus = _AluMwRadioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 2),
    _AluMwRadioRowStatus_Type()
)
aluMwRadioRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioRowStatus.setStatus("current")


class _AluMwRadioMode_Type(Integer32):
    """Custom type aluMwRadioMode based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 0),
          ("onePlusZero", 1),
          ("main", 2),
          ("spare", 3))
    )


_AluMwRadioMode_Type.__name__ = "Integer32"
_AluMwRadioMode_Object = MibTableColumn
aluMwRadioMode = _AluMwRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 3),
    _AluMwRadioMode_Type()
)
aluMwRadioMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioMode.setStatus("current")
_AluMwRadioMwLinkID_Type = AluMwLinkID
_AluMwRadioMwLinkID_Object = MibTableColumn
aluMwRadioMwLinkID = _AluMwRadioMwLinkID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 4),
    _AluMwRadioMwLinkID_Type()
)
aluMwRadioMwLinkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioMwLinkID.setStatus("current")
_AluMwRadioOperStatus_Type = TmnxPortOperStatus
_AluMwRadioOperStatus_Object = MibTableColumn
aluMwRadioOperStatus = _AluMwRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 5),
    _AluMwRadioOperStatus_Type()
)
aluMwRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioOperStatus.setStatus("current")


class _AluMwRadioOperFlags_Type(Bits):
    """Custom type aluMwRadioOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("portNotPresent", 0),
          ("portOperDown", 1),
          ("radioNotPresent", 2),
          ("radioCommError", 3),
          ("radioInit", 4),
          ("softwareDownload", 5),
          ("txMuted", 6),
          ("radioNotReady", 7),
          ("radioEqFailure", 8),
          ("incompatibleShifter", 9),
          ("incompatibleFreq", 10),
          ("incompatiblePower", 11),
          ("incompatibleModParms", 12),
          ("di", 13),
          ("radioLinkDown", 14),
          ("rslThresholdFail", 15),
          ("lof", 16),
          ("protectionFail", 17),
          ("proxyActive", 18),
          ("noDbFile", 19),
          ("dbSyncInProgress", 20),
          ("noDbConfig", 21),
          ("tpsTxMuted", 22),
          ("noSoftware", 23),
          ("softwareMismatch", 24),
          ("issu", 25),
          ("highBer", 26))
    )

_AluMwRadioOperFlags_Type.__name__ = "Bits"
_AluMwRadioOperFlags_Object = MibTableColumn
aluMwRadioOperFlags = _AluMwRadioOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 6),
    _AluMwRadioOperFlags_Type()
)
aluMwRadioOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioOperFlags.setStatus("current")


class _AluMwRadioStandalone_Type(TruthValue):
    """Custom type aluMwRadioStandalone based on TruthValue"""
    defaultValue = 2


_AluMwRadioStandalone_Type.__name__ = "TruthValue"
_AluMwRadioStandalone_Object = MibTableColumn
aluMwRadioStandalone = _AluMwRadioStandalone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 7),
    _AluMwRadioStandalone_Type()
)
aluMwRadioStandalone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioStandalone.setStatus("current")
_AluMwRadioName_Type = TNamedItemOrEmpty
_AluMwRadioName_Object = MibTableColumn
aluMwRadioName = _AluMwRadioName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 8),
    _AluMwRadioName_Type()
)
aluMwRadioName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioName.setStatus("current")
_AluMwRadioDatabaseFilename_Type = TNamedItemOrEmpty
_AluMwRadioDatabaseFilename_Object = MibTableColumn
aluMwRadioDatabaseFilename = _AluMwRadioDatabaseFilename_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 9),
    _AluMwRadioDatabaseFilename_Type()
)
aluMwRadioDatabaseFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioDatabaseFilename.setStatus("current")
_AluMwRadioType_Type = Integer32
_AluMwRadioType_Object = MibTableColumn
aluMwRadioType = _AluMwRadioType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 10),
    _AluMwRadioType_Type()
)
aluMwRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioType.setStatus("current")
_AluMwRadioFrequency_Type = Integer32
_AluMwRadioFrequency_Object = MibTableColumn
aluMwRadioFrequency = _AluMwRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 11),
    _AluMwRadioFrequency_Type()
)
aluMwRadioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aluMwRadioFrequency.setUnits("MHz")


class _AluMwRadioAlarmState_Type(Integer32):
    """Custom type aluMwRadioAlarmState based on Integer32"""
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
        *(("ok", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("inderminate", 5),
          ("notSupported", 6),
          ("unknown", 7))
    )


_AluMwRadioAlarmState_Type.__name__ = "Integer32"
_AluMwRadioAlarmState_Object = MibTableColumn
aluMwRadioAlarmState = _AluMwRadioAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 12),
    _AluMwRadioAlarmState_Type()
)
aluMwRadioAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmState.setStatus("current")
_AluMwRadioAlarmsCritical_Type = Integer32
_AluMwRadioAlarmsCritical_Object = MibTableColumn
aluMwRadioAlarmsCritical = _AluMwRadioAlarmsCritical_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 13),
    _AluMwRadioAlarmsCritical_Type()
)
aluMwRadioAlarmsCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsCritical.setStatus("current")
_AluMwRadioAlarmsMajor_Type = Integer32
_AluMwRadioAlarmsMajor_Object = MibTableColumn
aluMwRadioAlarmsMajor = _AluMwRadioAlarmsMajor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 14),
    _AluMwRadioAlarmsMajor_Type()
)
aluMwRadioAlarmsMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsMajor.setStatus("current")
_AluMwRadioAlarmsMinor_Type = Integer32
_AluMwRadioAlarmsMinor_Object = MibTableColumn
aluMwRadioAlarmsMinor = _AluMwRadioAlarmsMinor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 15),
    _AluMwRadioAlarmsMinor_Type()
)
aluMwRadioAlarmsMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsMinor.setStatus("current")
_AluMwRadioAlarmsWarning_Type = Integer32
_AluMwRadioAlarmsWarning_Object = MibTableColumn
aluMwRadioAlarmsWarning = _AluMwRadioAlarmsWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 16),
    _AluMwRadioAlarmsWarning_Type()
)
aluMwRadioAlarmsWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsWarning.setStatus("current")
_AluMwRadioAlarmsInd_Type = Integer32
_AluMwRadioAlarmsInd_Object = MibTableColumn
aluMwRadioAlarmsInd = _AluMwRadioAlarmsInd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 17),
    _AluMwRadioAlarmsInd_Type()
)
aluMwRadioAlarmsInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsInd.setStatus("current")
_AluMwRadioAlarmsCommunication_Type = Integer32
_AluMwRadioAlarmsCommunication_Object = MibTableColumn
aluMwRadioAlarmsCommunication = _AluMwRadioAlarmsCommunication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 18),
    _AluMwRadioAlarmsCommunication_Type()
)
aluMwRadioAlarmsCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsCommunication.setStatus("current")
_AluMwRadioAlarmsEquipment_Type = Integer32
_AluMwRadioAlarmsEquipment_Object = MibTableColumn
aluMwRadioAlarmsEquipment = _AluMwRadioAlarmsEquipment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 19),
    _AluMwRadioAlarmsEquipment_Type()
)
aluMwRadioAlarmsEquipment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmsEquipment.setStatus("current")


class _AluMwRadioTxMuted_Type(Integer32):
    """Custom type aluMwRadioTxMuted based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 0),
          ("none", 1),
          ("manual", 2),
          ("auto", 3))
    )


_AluMwRadioTxMuted_Type.__name__ = "Integer32"
_AluMwRadioTxMuted_Object = MibTableColumn
aluMwRadioTxMuted = _AluMwRadioTxMuted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 20),
    _AluMwRadioTxMuted_Type()
)
aluMwRadioTxMuted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioTxMuted.setStatus("current")


class _AluMwRadioReboot_Type(TmnxActionType):
    """Custom type aluMwRadioReboot based on TmnxActionType"""
    defaultValue = 2


_AluMwRadioReboot_Type.__name__ = "TmnxActionType"
_AluMwRadioReboot_Object = MibTableColumn
aluMwRadioReboot = _AluMwRadioReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 21),
    _AluMwRadioReboot_Type()
)
aluMwRadioReboot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioReboot.setStatus("current")
_AluMwRadioLastStateChange_Type = TimeStamp
_AluMwRadioLastStateChange_Object = MibTableColumn
aluMwRadioLastStateChange = _AluMwRadioLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 22),
    _AluMwRadioLastStateChange_Type()
)
aluMwRadioLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioLastStateChange.setStatus("current")
_AluMwRadioCommEstablished_Type = TimeStamp
_AluMwRadioCommEstablished_Object = MibTableColumn
aluMwRadioCommEstablished = _AluMwRadioCommEstablished_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 23),
    _AluMwRadioCommEstablished_Type()
)
aluMwRadioCommEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioCommEstablished.setStatus("current")
_AluMwRadioCommLost_Type = TimeStamp
_AluMwRadioCommLost_Object = MibTableColumn
aluMwRadioCommLost = _AluMwRadioCommLost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 24),
    _AluMwRadioCommLost_Type()
)
aluMwRadioCommLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioCommLost.setStatus("current")
_AluMwRadioSwState_Type = AluMwRadioSwState
_AluMwRadioSwState_Object = MibTableColumn
aluMwRadioSwState = _AluMwRadioSwState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 25),
    _AluMwRadioSwState_Type()
)
aluMwRadioSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioSwState.setStatus("current")
_AluMwRadioSwDnldProgress_Type = Integer32
_AluMwRadioSwDnldProgress_Object = MibTableColumn
aluMwRadioSwDnldProgress = _AluMwRadioSwDnldProgress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 26),
    _AluMwRadioSwDnldProgress_Type()
)
aluMwRadioSwDnldProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioSwDnldProgress.setStatus("current")
_AluMwRadioRslHistoryUrl_Type = TmnxDisplayStringURL
_AluMwRadioRslHistoryUrl_Object = MibTableColumn
aluMwRadioRslHistoryUrl = _AluMwRadioRslHistoryUrl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 27),
    _AluMwRadioRslHistoryUrl_Type()
)
aluMwRadioRslHistoryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioRslHistoryUrl.setStatus("current")


class _AluMwRadioRslHistoryClear_Type(TmnxActionType):
    """Custom type aluMwRadioRslHistoryClear based on TmnxActionType"""
    defaultValue = 2


_AluMwRadioRslHistoryClear_Type.__name__ = "TmnxActionType"
_AluMwRadioRslHistoryClear_Object = MibTableColumn
aluMwRadioRslHistoryClear = _AluMwRadioRslHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 28),
    _AluMwRadioRslHistoryClear_Type()
)
aluMwRadioRslHistoryClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioRslHistoryClear.setStatus("current")


class _AluMwRadioFfdSuppressFlags_Type(Bits):
    """Custom type aluMwRadioFfdSuppressFlags based on Bits"""
    namedValues = NamedValues(
        *(("allfaults", 0),
          ("highBer", 1),
          ("di", 2),
          ("rslThreshold", 3))
    )

_AluMwRadioFfdSuppressFlags_Type.__name__ = "Bits"
_AluMwRadioFfdSuppressFlags_Object = MibTableColumn
aluMwRadioFfdSuppressFlags = _AluMwRadioFfdSuppressFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 29),
    _AluMwRadioFfdSuppressFlags_Type()
)
aluMwRadioFfdSuppressFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioFfdSuppressFlags.setStatus("current")


class _AluMwRadioPMG826Enable_Type(TruthValue):
    """Custom type aluMwRadioPMG826Enable based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMG826Enable_Type.__name__ = "TruthValue"
_AluMwRadioPMG826Enable_Object = MibTableColumn
aluMwRadioPMG826Enable = _AluMwRadioPMG826Enable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 30),
    _AluMwRadioPMG826Enable_Type()
)
aluMwRadioPMG826Enable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMG826Enable.setStatus("current")


class _AluMwRadioPMG826OperStatus_Type(TruthValue):
    """Custom type aluMwRadioPMG826OperStatus based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMG826OperStatus_Type.__name__ = "TruthValue"
_AluMwRadioPMG826OperStatus_Object = MibTableColumn
aluMwRadioPMG826OperStatus = _AluMwRadioPMG826OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 31),
    _AluMwRadioPMG826OperStatus_Type()
)
aluMwRadioPMG826OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioPMG826OperStatus.setStatus("current")


class _AluMwRadioPMG826Clear_Type(TmnxActionType):
    """Custom type aluMwRadioPMG826Clear based on TmnxActionType"""
    defaultValue = 2


_AluMwRadioPMG826Clear_Type.__name__ = "TmnxActionType"
_AluMwRadioPMG826Clear_Object = MibTableColumn
aluMwRadioPMG826Clear = _AluMwRadioPMG826Clear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 32),
    _AluMwRadioPMG826Clear_Type()
)
aluMwRadioPMG826Clear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMG826Clear.setStatus("current")


class _AluMwRadioPMACMEnable_Type(TruthValue):
    """Custom type aluMwRadioPMACMEnable based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMACMEnable_Type.__name__ = "TruthValue"
_AluMwRadioPMACMEnable_Object = MibTableColumn
aluMwRadioPMACMEnable = _AluMwRadioPMACMEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 33),
    _AluMwRadioPMACMEnable_Type()
)
aluMwRadioPMACMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMACMEnable.setStatus("current")


class _AluMwRadioPMACMOperStatus_Type(TruthValue):
    """Custom type aluMwRadioPMACMOperStatus based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMACMOperStatus_Type.__name__ = "TruthValue"
_AluMwRadioPMACMOperStatus_Object = MibTableColumn
aluMwRadioPMACMOperStatus = _AluMwRadioPMACMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 34),
    _AluMwRadioPMACMOperStatus_Type()
)
aluMwRadioPMACMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioPMACMOperStatus.setStatus("current")


class _AluMwRadioPMACMClear_Type(TmnxActionType):
    """Custom type aluMwRadioPMACMClear based on TmnxActionType"""
    defaultValue = 2


_AluMwRadioPMACMClear_Type.__name__ = "TmnxActionType"
_AluMwRadioPMACMClear_Object = MibTableColumn
aluMwRadioPMACMClear = _AluMwRadioPMACMClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 35),
    _AluMwRadioPMACMClear_Type()
)
aluMwRadioPMACMClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMACMClear.setStatus("current")


class _AluMwRadioPMPowerEnable_Type(TruthValue):
    """Custom type aluMwRadioPMPowerEnable based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMPowerEnable_Type.__name__ = "TruthValue"
_AluMwRadioPMPowerEnable_Object = MibTableColumn
aluMwRadioPMPowerEnable = _AluMwRadioPMPowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 36),
    _AluMwRadioPMPowerEnable_Type()
)
aluMwRadioPMPowerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMPowerEnable.setStatus("current")


class _AluMwRadioPMPowerOperStatus_Type(TruthValue):
    """Custom type aluMwRadioPMPowerOperStatus based on TruthValue"""
    defaultValue = 2


_AluMwRadioPMPowerOperStatus_Type.__name__ = "TruthValue"
_AluMwRadioPMPowerOperStatus_Object = MibTableColumn
aluMwRadioPMPowerOperStatus = _AluMwRadioPMPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 37),
    _AluMwRadioPMPowerOperStatus_Type()
)
aluMwRadioPMPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioPMPowerOperStatus.setStatus("current")


class _AluMwRadioPMPowerClear_Type(TmnxActionType):
    """Custom type aluMwRadioPMPowerClear based on TmnxActionType"""
    defaultValue = 2


_AluMwRadioPMPowerClear_Type.__name__ = "TmnxActionType"
_AluMwRadioPMPowerClear_Object = MibTableColumn
aluMwRadioPMPowerClear = _AluMwRadioPMPowerClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 2, 1, 38),
    _AluMwRadioPMPowerClear_Type()
)
aluMwRadioPMPowerClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluMwRadioPMPowerClear.setStatus("current")
_AluMwRadioPowerMeasuresTable_Object = MibTable
aluMwRadioPowerMeasuresTable = _AluMwRadioPowerMeasuresTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    aluMwRadioPowerMeasuresTable.setStatus("current")
_AluMwRadioPowerMeasuresEntry_Object = MibTableRow
aluMwRadioPowerMeasuresEntry = _AluMwRadioPowerMeasuresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1)
)
aluMwRadioPowerMeasuresEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
)
if mibBuilder.loadTexts:
    aluMwRadioPowerMeasuresEntry.setStatus("current")


class _AluMwRadioLocalTxPower_Type(Integer32):
    """Custom type aluMwRadioLocalTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwRadioLocalTxPower_Type.__name__ = "Integer32"
_AluMwRadioLocalTxPower_Object = MibTableColumn
aluMwRadioLocalTxPower = _AluMwRadioLocalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 1),
    _AluMwRadioLocalTxPower_Type()
)
aluMwRadioLocalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioLocalTxPower.setStatus("current")


class _AluMwRadioLocalRxMainPower_Type(Integer32):
    """Custom type aluMwRadioLocalRxMainPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_AluMwRadioLocalRxMainPower_Type.__name__ = "Integer32"
_AluMwRadioLocalRxMainPower_Object = MibTableColumn
aluMwRadioLocalRxMainPower = _AluMwRadioLocalRxMainPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 2),
    _AluMwRadioLocalRxMainPower_Type()
)
aluMwRadioLocalRxMainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioLocalRxMainPower.setStatus("current")


class _AluMwRadioRemoteTxPower_Type(Integer32):
    """Custom type aluMwRadioRemoteTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwRadioRemoteTxPower_Type.__name__ = "Integer32"
_AluMwRadioRemoteTxPower_Object = MibTableColumn
aluMwRadioRemoteTxPower = _AluMwRadioRemoteTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 3),
    _AluMwRadioRemoteTxPower_Type()
)
aluMwRadioRemoteTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioRemoteTxPower.setStatus("current")


class _AluMwRadioRemoteRxMainPower_Type(Integer32):
    """Custom type aluMwRadioRemoteRxMainPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_AluMwRadioRemoteRxMainPower_Type.__name__ = "Integer32"
_AluMwRadioRemoteRxMainPower_Object = MibTableColumn
aluMwRadioRemoteRxMainPower = _AluMwRadioRemoteRxMainPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 4),
    _AluMwRadioRemoteRxMainPower_Type()
)
aluMwRadioRemoteRxMainPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioRemoteRxMainPower.setStatus("current")


class _AluMwRadioLocalDiversityPower_Type(Integer32):
    """Custom type aluMwRadioLocalDiversityPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwRadioLocalDiversityPower_Type.__name__ = "Integer32"
_AluMwRadioLocalDiversityPower_Object = MibTableColumn
aluMwRadioLocalDiversityPower = _AluMwRadioLocalDiversityPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 5),
    _AluMwRadioLocalDiversityPower_Type()
)
aluMwRadioLocalDiversityPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioLocalDiversityPower.setStatus("current")


class _AluMwRadioRemoteDiversityPower_Type(Integer32):
    """Custom type aluMwRadioRemoteDiversityPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_AluMwRadioRemoteDiversityPower_Type.__name__ = "Integer32"
_AluMwRadioRemoteDiversityPower_Object = MibTableColumn
aluMwRadioRemoteDiversityPower = _AluMwRadioRemoteDiversityPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 3, 1, 6),
    _AluMwRadioRemoteDiversityPower_Type()
)
aluMwRadioRemoteDiversityPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioRemoteDiversityPower.setStatus("current")
_AluMwRadioAlarmsTable_Object = MibTable
aluMwRadioAlarmsTable = _AluMwRadioAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    aluMwRadioAlarmsTable.setStatus("current")
_AluMwRadioAlarmsEntry_Object = MibTableRow
aluMwRadioAlarmsEntry = _AluMwRadioAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1)
)
aluMwRadioAlarmsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioAlarmID"),
)
if mibBuilder.loadTexts:
    aluMwRadioAlarmsEntry.setStatus("current")
_AluMwRadioAlarmID_Type = Integer32
_AluMwRadioAlarmID_Object = MibTableColumn
aluMwRadioAlarmID = _AluMwRadioAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 1),
    _AluMwRadioAlarmID_Type()
)
aluMwRadioAlarmID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluMwRadioAlarmID.setStatus("current")
_AluMwRadioAlarmTime_Type = DateAndTime
_AluMwRadioAlarmTime_Object = MibTableColumn
aluMwRadioAlarmTime = _AluMwRadioAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 2),
    _AluMwRadioAlarmTime_Type()
)
aluMwRadioAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmTime.setStatus("current")
_AluMwRadioAlarmName_Type = DisplayString
_AluMwRadioAlarmName_Object = MibTableColumn
aluMwRadioAlarmName = _AluMwRadioAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 3),
    _AluMwRadioAlarmName_Type()
)
aluMwRadioAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmName.setStatus("current")


class _AluMwRadioAlarmSeverity_Type(Integer32):
    """Custom type aluMwRadioAlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("indeterminate", 5),
          ("cleared", 6))
    )


_AluMwRadioAlarmSeverity_Type.__name__ = "Integer32"
_AluMwRadioAlarmSeverity_Object = MibTableColumn
aluMwRadioAlarmSeverity = _AluMwRadioAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 4),
    _AluMwRadioAlarmSeverity_Type()
)
aluMwRadioAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmSeverity.setStatus("current")
_AluMwRadioAlarmSpecProblem_Type = DisplayString
_AluMwRadioAlarmSpecProblem_Object = MibTableColumn
aluMwRadioAlarmSpecProblem = _AluMwRadioAlarmSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 5),
    _AluMwRadioAlarmSpecProblem_Type()
)
aluMwRadioAlarmSpecProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmSpecProblem.setStatus("current")


class _AluMwRadioAlarmType_Type(Integer32):
    """Custom type aluMwRadioAlarmType based on Integer32"""
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
        *(("communication", 1),
          ("qos", 2),
          ("processing", 3),
          ("equipment", 4),
          ("environment", 5))
    )


_AluMwRadioAlarmType_Type.__name__ = "Integer32"
_AluMwRadioAlarmType_Object = MibTableColumn
aluMwRadioAlarmType = _AluMwRadioAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 6),
    _AluMwRadioAlarmType_Type()
)
aluMwRadioAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmType.setStatus("current")
_AluMwRadioAlarmObject_Type = DisplayString
_AluMwRadioAlarmObject_Object = MibTableColumn
aluMwRadioAlarmObject = _AluMwRadioAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 7),
    _AluMwRadioAlarmObject_Type()
)
aluMwRadioAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmObject.setStatus("current")
_AluMwRadioAlarmSubObject_Type = DisplayString
_AluMwRadioAlarmSubObject_Object = MibTableColumn
aluMwRadioAlarmSubObject = _AluMwRadioAlarmSubObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 4, 1, 8),
    _AluMwRadioAlarmSubObject_Type()
)
aluMwRadioAlarmSubObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioAlarmSubObject.setStatus("current")
_AluMwLinkStatisticsTable_Object = MibTable
aluMwLinkStatisticsTable = _AluMwLinkStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    aluMwLinkStatisticsTable.setStatus("current")
_AluMwLinkStatisticsEntry_Object = MibTableRow
aluMwLinkStatisticsEntry = _AluMwLinkStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1)
)
aluMwLinkStatisticsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwLinkID"),
)
if mibBuilder.loadTexts:
    aluMwLinkStatisticsEntry.setStatus("current")
_AluMwLinkAggrFramesTx_Type = Counter64
_AluMwLinkAggrFramesTx_Object = MibTableColumn
aluMwLinkAggrFramesTx = _AluMwLinkAggrFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 1),
    _AluMwLinkAggrFramesTx_Type()
)
aluMwLinkAggrFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAggrFramesTx.setStatus("current")
_AluMwLinkAggrOctetsTx_Type = Counter64
_AluMwLinkAggrOctetsTx_Object = MibTableColumn
aluMwLinkAggrOctetsTx = _AluMwLinkAggrOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 2),
    _AluMwLinkAggrOctetsTx_Type()
)
aluMwLinkAggrOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAggrOctetsTx.setStatus("current")
_AluMwLinkAggrDiscardedTx_Type = Counter64
_AluMwLinkAggrDiscardedTx_Object = MibTableColumn
aluMwLinkAggrDiscardedTx = _AluMwLinkAggrDiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 3),
    _AluMwLinkAggrDiscardedTx_Type()
)
aluMwLinkAggrDiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkAggrDiscardedTx.setStatus("current")
_AluMwLinkQueue1FramesTx_Type = Counter64
_AluMwLinkQueue1FramesTx_Object = MibTableColumn
aluMwLinkQueue1FramesTx = _AluMwLinkQueue1FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 4),
    _AluMwLinkQueue1FramesTx_Type()
)
aluMwLinkQueue1FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue1FramesTx.setStatus("current")
_AluMwLinkQueue1OctetsTx_Type = Counter64
_AluMwLinkQueue1OctetsTx_Object = MibTableColumn
aluMwLinkQueue1OctetsTx = _AluMwLinkQueue1OctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 5),
    _AluMwLinkQueue1OctetsTx_Type()
)
aluMwLinkQueue1OctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue1OctetsTx.setStatus("current")
_AluMwLinkQueue1DiscardedTx_Type = Counter64
_AluMwLinkQueue1DiscardedTx_Object = MibTableColumn
aluMwLinkQueue1DiscardedTx = _AluMwLinkQueue1DiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 6),
    _AluMwLinkQueue1DiscardedTx_Type()
)
aluMwLinkQueue1DiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue1DiscardedTx.setStatus("current")
_AluMwLinkQueue2FramesTx_Type = Counter64
_AluMwLinkQueue2FramesTx_Object = MibTableColumn
aluMwLinkQueue2FramesTx = _AluMwLinkQueue2FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 7),
    _AluMwLinkQueue2FramesTx_Type()
)
aluMwLinkQueue2FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue2FramesTx.setStatus("current")
_AluMwLinkQueue2OctetsTx_Type = Counter64
_AluMwLinkQueue2OctetsTx_Object = MibTableColumn
aluMwLinkQueue2OctetsTx = _AluMwLinkQueue2OctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 8),
    _AluMwLinkQueue2OctetsTx_Type()
)
aluMwLinkQueue2OctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue2OctetsTx.setStatus("current")
_AluMwLinkQueue2DiscardedTx_Type = Counter64
_AluMwLinkQueue2DiscardedTx_Object = MibTableColumn
aluMwLinkQueue2DiscardedTx = _AluMwLinkQueue2DiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 9),
    _AluMwLinkQueue2DiscardedTx_Type()
)
aluMwLinkQueue2DiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue2DiscardedTx.setStatus("current")
_AluMwLinkQueue3FramesTx_Type = Counter64
_AluMwLinkQueue3FramesTx_Object = MibTableColumn
aluMwLinkQueue3FramesTx = _AluMwLinkQueue3FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 10),
    _AluMwLinkQueue3FramesTx_Type()
)
aluMwLinkQueue3FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue3FramesTx.setStatus("current")
_AluMwLinkQueue3OctetsTx_Type = Counter64
_AluMwLinkQueue3OctetsTx_Object = MibTableColumn
aluMwLinkQueue3OctetsTx = _AluMwLinkQueue3OctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 11),
    _AluMwLinkQueue3OctetsTx_Type()
)
aluMwLinkQueue3OctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue3OctetsTx.setStatus("current")
_AluMwLinkQueue3DiscardedTx_Type = Counter64
_AluMwLinkQueue3DiscardedTx_Object = MibTableColumn
aluMwLinkQueue3DiscardedTx = _AluMwLinkQueue3DiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 12),
    _AluMwLinkQueue3DiscardedTx_Type()
)
aluMwLinkQueue3DiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue3DiscardedTx.setStatus("current")
_AluMwLinkQueue4FramesTx_Type = Counter64
_AluMwLinkQueue4FramesTx_Object = MibTableColumn
aluMwLinkQueue4FramesTx = _AluMwLinkQueue4FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 13),
    _AluMwLinkQueue4FramesTx_Type()
)
aluMwLinkQueue4FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue4FramesTx.setStatus("current")
_AluMwLinkQueue4OctetsTx_Type = Counter64
_AluMwLinkQueue4OctetsTx_Object = MibTableColumn
aluMwLinkQueue4OctetsTx = _AluMwLinkQueue4OctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 14),
    _AluMwLinkQueue4OctetsTx_Type()
)
aluMwLinkQueue4OctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue4OctetsTx.setStatus("current")
_AluMwLinkQueue4DiscardedTx_Type = Counter64
_AluMwLinkQueue4DiscardedTx_Object = MibTableColumn
aluMwLinkQueue4DiscardedTx = _AluMwLinkQueue4DiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 15),
    _AluMwLinkQueue4DiscardedTx_Type()
)
aluMwLinkQueue4DiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue4DiscardedTx.setStatus("current")
_AluMwLinkQueue5FramesTx_Type = Counter64
_AluMwLinkQueue5FramesTx_Object = MibTableColumn
aluMwLinkQueue5FramesTx = _AluMwLinkQueue5FramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 16),
    _AluMwLinkQueue5FramesTx_Type()
)
aluMwLinkQueue5FramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue5FramesTx.setStatus("current")
_AluMwLinkQueue5OctetsTx_Type = Counter64
_AluMwLinkQueue5OctetsTx_Object = MibTableColumn
aluMwLinkQueue5OctetsTx = _AluMwLinkQueue5OctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 17),
    _AluMwLinkQueue5OctetsTx_Type()
)
aluMwLinkQueue5OctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue5OctetsTx.setStatus("current")
_AluMwLinkQueue5DiscardedTx_Type = Counter64
_AluMwLinkQueue5DiscardedTx_Object = MibTableColumn
aluMwLinkQueue5DiscardedTx = _AluMwLinkQueue5DiscardedTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 5, 1, 18),
    _AluMwLinkQueue5DiscardedTx_Type()
)
aluMwLinkQueue5DiscardedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkQueue5DiscardedTx.setStatus("current")
_AluMwRadioInfoTable_Object = MibTable
aluMwRadioInfoTable = _AluMwRadioInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    aluMwRadioInfoTable.setStatus("current")
_AluMwRadioInfoEntry_Object = MibTableRow
aluMwRadioInfoEntry = _AluMwRadioInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1)
)
aluMwRadioInfoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
)
if mibBuilder.loadTexts:
    aluMwRadioInfoEntry.setStatus("current")
_AluMwRadioInfoValid_Type = TruthValue
_AluMwRadioInfoValid_Object = MibTableColumn
aluMwRadioInfoValid = _AluMwRadioInfoValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 1),
    _AluMwRadioInfoValid_Type()
)
aluMwRadioInfoValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioInfoValid.setStatus("current")


class _AluMwRadioCompanyId_Type(SnmpAdminString):
    """Custom type aluMwRadioCompanyId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AluMwRadioCompanyId_Type.__name__ = "SnmpAdminString"
_AluMwRadioCompanyId_Object = MibTableColumn
aluMwRadioCompanyId = _AluMwRadioCompanyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 2),
    _AluMwRadioCompanyId_Type()
)
aluMwRadioCompanyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioCompanyId.setStatus("current")


class _AluMwRadioMnemonic_Type(SnmpAdminString):
    """Custom type aluMwRadioMnemonic based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AluMwRadioMnemonic_Type.__name__ = "SnmpAdminString"
_AluMwRadioMnemonic_Object = MibTableColumn
aluMwRadioMnemonic = _AluMwRadioMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 3),
    _AluMwRadioMnemonic_Type()
)
aluMwRadioMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioMnemonic.setStatus("current")


class _AluMwRadioCLEI_Type(SnmpAdminString):
    """Custom type aluMwRadioCLEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AluMwRadioCLEI_Type.__name__ = "SnmpAdminString"
_AluMwRadioCLEI_Object = MibTableColumn
aluMwRadioCLEI = _AluMwRadioCLEI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 4),
    _AluMwRadioCLEI_Type()
)
aluMwRadioCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioCLEI.setStatus("current")


class _AluMwRadioHwPartNumber_Type(SnmpAdminString):
    """Custom type aluMwRadioHwPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AluMwRadioHwPartNumber_Type.__name__ = "SnmpAdminString"
_AluMwRadioHwPartNumber_Object = MibTableColumn
aluMwRadioHwPartNumber = _AluMwRadioHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 5),
    _AluMwRadioHwPartNumber_Type()
)
aluMwRadioHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioHwPartNumber.setStatus("current")


class _AluMwRadioSwPartNumber_Type(SnmpAdminString):
    """Custom type aluMwRadioSwPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AluMwRadioSwPartNumber_Type.__name__ = "SnmpAdminString"
_AluMwRadioSwPartNumber_Object = MibTableColumn
aluMwRadioSwPartNumber = _AluMwRadioSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 6),
    _AluMwRadioSwPartNumber_Type()
)
aluMwRadioSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioSwPartNumber.setStatus("current")


class _AluMwRadioFactoryId_Type(SnmpAdminString):
    """Custom type aluMwRadioFactoryId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AluMwRadioFactoryId_Type.__name__ = "SnmpAdminString"
_AluMwRadioFactoryId_Object = MibTableColumn
aluMwRadioFactoryId = _AluMwRadioFactoryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 7),
    _AluMwRadioFactoryId_Type()
)
aluMwRadioFactoryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioFactoryId.setStatus("current")


class _AluMwRadioSerialNumber_Type(SnmpAdminString):
    """Custom type aluMwRadioSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AluMwRadioSerialNumber_Type.__name__ = "SnmpAdminString"
_AluMwRadioSerialNumber_Object = MibTableColumn
aluMwRadioSerialNumber = _AluMwRadioSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 8),
    _AluMwRadioSerialNumber_Type()
)
aluMwRadioSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioSerialNumber.setStatus("current")


class _AluMwRadioMfgDateId_Type(SnmpAdminString):
    """Custom type aluMwRadioMfgDateId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_AluMwRadioMfgDateId_Type.__name__ = "SnmpAdminString"
_AluMwRadioMfgDateId_Object = MibTableColumn
aluMwRadioMfgDateId = _AluMwRadioMfgDateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 9),
    _AluMwRadioMfgDateId_Type()
)
aluMwRadioMfgDateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioMfgDateId.setStatus("current")


class _AluMwRadioMfgDate_Type(SnmpAdminString):
    """Custom type aluMwRadioMfgDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AluMwRadioMfgDate_Type.__name__ = "SnmpAdminString"
_AluMwRadioMfgDate_Object = MibTableColumn
aluMwRadioMfgDate = _AluMwRadioMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 10),
    _AluMwRadioMfgDate_Type()
)
aluMwRadioMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioMfgDate.setStatus("current")


class _AluMwRadioCustomerField_Type(SnmpAdminString):
    """Custom type aluMwRadioCustomerField based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_AluMwRadioCustomerField_Type.__name__ = "SnmpAdminString"
_AluMwRadioCustomerField_Object = MibTableColumn
aluMwRadioCustomerField = _AluMwRadioCustomerField_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 11),
    _AluMwRadioCustomerField_Type()
)
aluMwRadioCustomerField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioCustomerField.setStatus("current")
_AluMwRadioTemperature_Type = Integer32
_AluMwRadioTemperature_Object = MibTableColumn
aluMwRadioTemperature = _AluMwRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 6, 1, 12),
    _AluMwRadioTemperature_Type()
)
aluMwRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwRadioTemperature.setStatus("current")
_AluMwTable_Object = MibTable
aluMwTable = _AluMwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 7)
)
if mibBuilder.loadTexts:
    aluMwTable.setStatus("current")
_AluMwEntry_Object = MibTableRow
aluMwEntry = _AluMwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 7, 1)
)
aluMwEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    aluMwEntry.setStatus("current")
_AluMwSwPackageValid_Type = TruthValue
_AluMwSwPackageValid_Object = MibTableColumn
aluMwSwPackageValid = _AluMwSwPackageValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 7, 1, 1),
    _AluMwSwPackageValid_Type()
)
aluMwSwPackageValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwSwPackageValid.setStatus("current")


class _AluMwSwDownloadTool_Type(Integer32):
    """Custom type aluMwSwDownloadTool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("startDownload", 1),
          ("startForcedDownload", 2))
    )


_AluMwSwDownloadTool_Type.__name__ = "Integer32"
_AluMwSwDownloadTool_Object = MibTableColumn
aluMwSwDownloadTool = _AluMwSwDownloadTool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 7, 1, 2),
    _AluMwSwDownloadTool_Type()
)
aluMwSwDownloadTool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluMwSwDownloadTool.setStatus("current")


class _AluMwSwDownloadState_Type(Integer32):
    """Custom type aluMwSwDownloadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("noSoftwarePackage", 1),
          ("ready", 2),
          ("downloadInProgress", 3),
          ("downloadFailed", 5))
    )


_AluMwSwDownloadState_Type.__name__ = "Integer32"
_AluMwSwDownloadState_Object = MibTableColumn
aluMwSwDownloadState = _AluMwSwDownloadState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 7, 1, 3),
    _AluMwSwDownloadState_Type()
)
aluMwSwDownloadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwSwDownloadState.setStatus("current")
_AluMwLinkTdaStatusTable_Object = MibTable
aluMwLinkTdaStatusTable = _AluMwLinkTdaStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 8)
)
if mibBuilder.loadTexts:
    aluMwLinkTdaStatusTable.setStatus("current")
_AluMwLinkTdaStatusEntry_Object = MibTableRow
aluMwLinkTdaStatusEntry = _AluMwLinkTdaStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 8, 1)
)
aluMwLinkTdaStatusEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwLinkID"),
)
if mibBuilder.loadTexts:
    aluMwLinkTdaStatusEntry.setStatus("current")


class _AluMwLinkTdaCmdState_Type(Integer32):
    """Custom type aluMwLinkTdaCmdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("error", 2))
    )


_AluMwLinkTdaCmdState_Type.__name__ = "Integer32"
_AluMwLinkTdaCmdState_Object = MibTableColumn
aluMwLinkTdaCmdState = _AluMwLinkTdaCmdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 8, 1, 1),
    _AluMwLinkTdaCmdState_Type()
)
aluMwLinkTdaCmdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkTdaCmdState.setStatus("current")


class _AluMwLinkTdaManualCmdStatus_Type(Integer32):
    """Custom type aluMwLinkTdaManualCmdStatus based on Integer32"""
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
        *(("notForced", 0),
          ("main", 1),
          ("diversity", 2),
          ("error", 3))
    )


_AluMwLinkTdaManualCmdStatus_Type.__name__ = "Integer32"
_AluMwLinkTdaManualCmdStatus_Object = MibTableColumn
aluMwLinkTdaManualCmdStatus = _AluMwLinkTdaManualCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 8, 1, 2),
    _AluMwLinkTdaManualCmdStatus_Type()
)
aluMwLinkTdaManualCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkTdaManualCmdStatus.setStatus("current")


class _AluMwLinkTdaSwitchPosition_Type(Integer32):
    """Custom type aluMwLinkTdaSwitchPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("diversity", 1),
          ("error", 2))
    )


_AluMwLinkTdaSwitchPosition_Type.__name__ = "Integer32"
_AluMwLinkTdaSwitchPosition_Object = MibTableColumn
aluMwLinkTdaSwitchPosition = _AluMwLinkTdaSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 8, 1, 3),
    _AluMwLinkTdaSwitchPosition_Type()
)
aluMwLinkTdaSwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwLinkTdaSwitchPosition.setStatus("current")
_AluMwRadioPMG826Table_Object = MibTable
aluMwRadioPMG826Table = _AluMwRadioPMG826Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9)
)
if mibBuilder.loadTexts:
    aluMwRadioPMG826Table.setStatus("current")
_AluMwRadioPMG826Entry_Object = MibTableRow
aluMwRadioPMG826Entry = _AluMwRadioPMG826Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1)
)
aluMwRadioPMG826Entry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMG826Section"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMG826Period"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMG826Bin"),
)
if mibBuilder.loadTexts:
    aluMwRadioPMG826Entry.setStatus("current")
_AluMwPMG826Section_Type = AluMwPerfMonSection
_AluMwPMG826Section_Object = MibTableColumn
aluMwPMG826Section = _AluMwPMG826Section_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 1),
    _AluMwPMG826Section_Type()
)
aluMwPMG826Section.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Section.setStatus("current")
_AluMwPMG826Period_Type = AluMwPerfMonPeriod
_AluMwPMG826Period_Object = MibTableColumn
aluMwPMG826Period = _AluMwPMG826Period_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 2),
    _AluMwPMG826Period_Type()
)
aluMwPMG826Period.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Period.setStatus("current")
_AluMwPMG826Bin_Type = AluMwPerfMonBin
_AluMwPMG826Bin_Object = MibTableColumn
aluMwPMG826Bin = _AluMwPMG826Bin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 3),
    _AluMwPMG826Bin_Type()
)
aluMwPMG826Bin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Bin.setStatus("current")
_AluMwPMG826Date_Type = Integer32
_AluMwPMG826Date_Object = MibTableColumn
aluMwPMG826Date = _AluMwPMG826Date_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 4),
    _AluMwPMG826Date_Type()
)
aluMwPMG826Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Date.setStatus("current")
_AluMwPMG826Duration_Type = Integer32
_AluMwPMG826Duration_Object = MibTableColumn
aluMwPMG826Duration = _AluMwPMG826Duration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 5),
    _AluMwPMG826Duration_Type()
)
aluMwPMG826Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Duration.setStatus("current")
_AluMwPMG826EPSState_Type = AluMwPerfMonEPSState
_AluMwPMG826EPSState_Object = MibTableColumn
aluMwPMG826EPSState = _AluMwPMG826EPSState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 6),
    _AluMwPMG826EPSState_Type()
)
aluMwPMG826EPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826EPSState.setStatus("current")
_AluMwPMG826Suspect_Type = TruthValue
_AluMwPMG826Suspect_Object = MibTableColumn
aluMwPMG826Suspect = _AluMwPMG826Suspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 7),
    _AluMwPMG826Suspect_Type()
)
aluMwPMG826Suspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826Suspect.setStatus("current")
_AluMwPMG826ES_Type = Unsigned32
_AluMwPMG826ES_Object = MibTableColumn
aluMwPMG826ES = _AluMwPMG826ES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 8),
    _AluMwPMG826ES_Type()
)
aluMwPMG826ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826ES.setStatus("current")
_AluMwPMG826SES_Type = Unsigned32
_AluMwPMG826SES_Object = MibTableColumn
aluMwPMG826SES = _AluMwPMG826SES_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 9),
    _AluMwPMG826SES_Type()
)
aluMwPMG826SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826SES.setStatus("current")
_AluMwPMG826BBE_Type = Unsigned32
_AluMwPMG826BBE_Object = MibTableColumn
aluMwPMG826BBE = _AluMwPMG826BBE_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 10),
    _AluMwPMG826BBE_Type()
)
aluMwPMG826BBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826BBE.setStatus("current")
_AluMwPMG826UAS_Type = Unsigned32
_AluMwPMG826UAS_Object = MibTableColumn
aluMwPMG826UAS = _AluMwPMG826UAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 9, 1, 11),
    _AluMwPMG826UAS_Type()
)
aluMwPMG826UAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMG826UAS.setStatus("current")
_AluMwRadioPMACMTable_Object = MibTable
aluMwRadioPMACMTable = _AluMwRadioPMACMTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10)
)
if mibBuilder.loadTexts:
    aluMwRadioPMACMTable.setStatus("current")
_AluMwRadioPMACMEntry_Object = MibTableRow
aluMwRadioPMACMEntry = _AluMwRadioPMACMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1)
)
aluMwRadioPMACMEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMACMPeriod"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMACMBin"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMACMModulation"),
)
if mibBuilder.loadTexts:
    aluMwRadioPMACMEntry.setStatus("current")
_AluMwPMACMPeriod_Type = AluMwPerfMonPeriod
_AluMwPMACMPeriod_Object = MibTableColumn
aluMwPMACMPeriod = _AluMwPMACMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 1),
    _AluMwPMACMPeriod_Type()
)
aluMwPMACMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMPeriod.setStatus("current")
_AluMwPMACMBin_Type = AluMwPerfMonBin
_AluMwPMACMBin_Object = MibTableColumn
aluMwPMACMBin = _AluMwPMACMBin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 2),
    _AluMwPMACMBin_Type()
)
aluMwPMACMBin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMBin.setStatus("current")
_AluMwPMACMModulation_Type = Integer32
_AluMwPMACMModulation_Object = MibTableColumn
aluMwPMACMModulation = _AluMwPMACMModulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 3),
    _AluMwPMACMModulation_Type()
)
aluMwPMACMModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMModulation.setStatus("current")
_AluMwPMACMDate_Type = Integer32
_AluMwPMACMDate_Object = MibTableColumn
aluMwPMACMDate = _AluMwPMACMDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 4),
    _AluMwPMACMDate_Type()
)
aluMwPMACMDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMDate.setStatus("current")
_AluMwPMACMDuration_Type = Integer32
_AluMwPMACMDuration_Object = MibTableColumn
aluMwPMACMDuration = _AluMwPMACMDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 5),
    _AluMwPMACMDuration_Type()
)
aluMwPMACMDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMDuration.setStatus("current")
_AluMwPMACMSuspect_Type = TruthValue
_AluMwPMACMSuspect_Object = MibTableColumn
aluMwPMACMSuspect = _AluMwPMACMSuspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 6),
    _AluMwPMACMSuspect_Type()
)
aluMwPMACMSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMSuspect.setStatus("current")
_AluMwPMACMTimeSpent_Type = Unsigned32
_AluMwPMACMTimeSpent_Object = MibTableColumn
aluMwPMACMTimeSpent = _AluMwPMACMTimeSpent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 10, 1, 7),
    _AluMwPMACMTimeSpent_Type()
)
aluMwPMACMTimeSpent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMACMTimeSpent.setStatus("current")
_AluMwRadioPMPowerTable_Object = MibTable
aluMwRadioPMPowerTable = _AluMwRadioPMPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11)
)
if mibBuilder.loadTexts:
    aluMwRadioPMPowerTable.setStatus("current")
_AluMwRadioPMPowerEntry_Object = MibTableRow
aluMwRadioPMPowerEntry = _AluMwRadioPMPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1)
)
aluMwRadioPMPowerEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALU-MICROWAVE-MIB", "aluMwRadioPortID"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMPowerDirection"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMPowerSection"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMPowerPeriod"),
    (0, "ALU-MICROWAVE-MIB", "aluMwPMPowerBin"),
)
if mibBuilder.loadTexts:
    aluMwRadioPMPowerEntry.setStatus("current")


class _AluMwPMPowerDirection_Type(Integer32):
    """Custom type aluMwPMPowerDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1))
    )


_AluMwPMPowerDirection_Type.__name__ = "Integer32"
_AluMwPMPowerDirection_Object = MibTableColumn
aluMwPMPowerDirection = _AluMwPMPowerDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 1),
    _AluMwPMPowerDirection_Type()
)
aluMwPMPowerDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerDirection.setStatus("current")
_AluMwPMPowerSection_Type = AluMwPerfMonSection
_AluMwPMPowerSection_Object = MibTableColumn
aluMwPMPowerSection = _AluMwPMPowerSection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 2),
    _AluMwPMPowerSection_Type()
)
aluMwPMPowerSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerSection.setStatus("current")
_AluMwPMPowerPeriod_Type = AluMwPerfMonPeriod
_AluMwPMPowerPeriod_Object = MibTableColumn
aluMwPMPowerPeriod = _AluMwPMPowerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 3),
    _AluMwPMPowerPeriod_Type()
)
aluMwPMPowerPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerPeriod.setStatus("current")
_AluMwPMPowerBin_Type = AluMwPerfMonBin
_AluMwPMPowerBin_Object = MibTableColumn
aluMwPMPowerBin = _AluMwPMPowerBin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 4),
    _AluMwPMPowerBin_Type()
)
aluMwPMPowerBin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerBin.setStatus("current")
_AluMwPMPowerDate_Type = Integer32
_AluMwPMPowerDate_Object = MibTableColumn
aluMwPMPowerDate = _AluMwPMPowerDate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 5),
    _AluMwPMPowerDate_Type()
)
aluMwPMPowerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerDate.setStatus("current")
_AluMwPMPowerDuration_Type = Integer32
_AluMwPMPowerDuration_Object = MibTableColumn
aluMwPMPowerDuration = _AluMwPMPowerDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 6),
    _AluMwPMPowerDuration_Type()
)
aluMwPMPowerDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerDuration.setStatus("current")
_AluMwPMPowerEPSState_Type = AluMwPerfMonEPSState
_AluMwPMPowerEPSState_Object = MibTableColumn
aluMwPMPowerEPSState = _AluMwPMPowerEPSState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 7),
    _AluMwPMPowerEPSState_Type()
)
aluMwPMPowerEPSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerEPSState.setStatus("current")
_AluMwPMPowerSuspect_Type = TruthValue
_AluMwPMPowerSuspect_Object = MibTableColumn
aluMwPMPowerSuspect = _AluMwPMPowerSuspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 8),
    _AluMwPMPowerSuspect_Type()
)
aluMwPMPowerSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerSuspect.setStatus("current")


class _AluMwPMPowerMinPowerLevel_Type(Integer32):
    """Custom type aluMwPMPowerMinPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwPMPowerMinPowerLevel_Type.__name__ = "Integer32"
_AluMwPMPowerMinPowerLevel_Object = MibTableColumn
aluMwPMPowerMinPowerLevel = _AluMwPMPowerMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 9),
    _AluMwPMPowerMinPowerLevel_Type()
)
aluMwPMPowerMinPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerMinPowerLevel.setStatus("current")


class _AluMwPMPowerMaxPowerLevel_Type(Integer32):
    """Custom type aluMwPMPowerMaxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwPMPowerMaxPowerLevel_Type.__name__ = "Integer32"
_AluMwPMPowerMaxPowerLevel_Object = MibTableColumn
aluMwPMPowerMaxPowerLevel = _AluMwPMPowerMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 10),
    _AluMwPMPowerMaxPowerLevel_Type()
)
aluMwPMPowerMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerMaxPowerLevel.setStatus("current")


class _AluMwPMPowerMeanPowerLevel_Type(Integer32):
    """Custom type aluMwPMPowerMeanPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_AluMwPMPowerMeanPowerLevel_Type.__name__ = "Integer32"
_AluMwPMPowerMeanPowerLevel_Object = MibTableColumn
aluMwPMPowerMeanPowerLevel = _AluMwPMPowerMeanPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 1, 11, 1, 11),
    _AluMwPMPowerMeanPowerLevel_Type()
)
aluMwPMPowerMeanPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMwPMPowerMeanPowerLevel.setStatus("current")
_AluMwNotifyObjs_ObjectIdentity = ObjectIdentity
aluMwNotifyObjs = _AluMwNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2)
)
_AluMwNotifyRadioPortID_Type = TmnxPortID
_AluMwNotifyRadioPortID_Object = MibScalar
aluMwNotifyRadioPortID = _AluMwNotifyRadioPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 1),
    _AluMwNotifyRadioPortID_Type()
)
aluMwNotifyRadioPortID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyRadioPortID.setStatus("current")
_AluMwNotifyAlarmTime_Type = DateAndTime
_AluMwNotifyAlarmTime_Object = MibScalar
aluMwNotifyAlarmTime = _AluMwNotifyAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 2),
    _AluMwNotifyAlarmTime_Type()
)
aluMwNotifyAlarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmTime.setStatus("current")
_AluMwNotifyAlarmId_Type = Integer32
_AluMwNotifyAlarmId_Object = MibScalar
aluMwNotifyAlarmId = _AluMwNotifyAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 3),
    _AluMwNotifyAlarmId_Type()
)
aluMwNotifyAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmId.setStatus("current")
_AluMwNotifyAlarmName_Type = DisplayString
_AluMwNotifyAlarmName_Object = MibScalar
aluMwNotifyAlarmName = _AluMwNotifyAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 4),
    _AluMwNotifyAlarmName_Type()
)
aluMwNotifyAlarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmName.setStatus("current")
_AluMwNotifyAlarmSpecProblem_Type = DisplayString
_AluMwNotifyAlarmSpecProblem_Object = MibScalar
aluMwNotifyAlarmSpecProblem = _AluMwNotifyAlarmSpecProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 5),
    _AluMwNotifyAlarmSpecProblem_Type()
)
aluMwNotifyAlarmSpecProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmSpecProblem.setStatus("current")


class _AluMwNotifyAlarmType_Type(Integer32):
    """Custom type aluMwNotifyAlarmType based on Integer32"""
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
        *(("communication", 1),
          ("qos", 2),
          ("processing", 3),
          ("equipment", 4),
          ("environment", 5))
    )


_AluMwNotifyAlarmType_Type.__name__ = "Integer32"
_AluMwNotifyAlarmType_Object = MibScalar
aluMwNotifyAlarmType = _AluMwNotifyAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 6),
    _AluMwNotifyAlarmType_Type()
)
aluMwNotifyAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmType.setStatus("current")
_AluMwNotifyAlarmObject_Type = DisplayString
_AluMwNotifyAlarmObject_Object = MibScalar
aluMwNotifyAlarmObject = _AluMwNotifyAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 7),
    _AluMwNotifyAlarmObject_Type()
)
aluMwNotifyAlarmObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmObject.setStatus("current")
_AluMwNotifyAlarmSubObject_Type = DisplayString
_AluMwNotifyAlarmSubObject_Object = MibScalar
aluMwNotifyAlarmSubObject = _AluMwNotifyAlarmSubObject_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 8),
    _AluMwNotifyAlarmSubObject_Type()
)
aluMwNotifyAlarmSubObject.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyAlarmSubObject.setStatus("current")


class _AluMwNotifyTxMute_Type(Integer32):
    """Custom type aluMwNotifyTxMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMute", 1),
          ("mute", 2))
    )


_AluMwNotifyTxMute_Type.__name__ = "Integer32"
_AluMwNotifyTxMute_Object = MibScalar
aluMwNotifyTxMute = _AluMwNotifyTxMute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 9),
    _AluMwNotifyTxMute_Type()
)
aluMwNotifyTxMute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyTxMute.setStatus("current")
_AluMwNotifyLinkPortID_Type = TmnxPortID
_AluMwNotifyLinkPortID_Object = MibScalar
aluMwNotifyLinkPortID = _AluMwNotifyLinkPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 10),
    _AluMwNotifyLinkPortID_Type()
)
aluMwNotifyLinkPortID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyLinkPortID.setStatus("current")


class _AluMwNotifyLinkActivity_Type(Integer32):
    """Custom type aluMwNotifyLinkActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("spare", 2),
          ("both", 3))
    )


_AluMwNotifyLinkActivity_Type.__name__ = "Integer32"
_AluMwNotifyLinkActivity_Object = MibScalar
aluMwNotifyLinkActivity = _AluMwNotifyLinkActivity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 11),
    _AluMwNotifyLinkActivity_Type()
)
aluMwNotifyLinkActivity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyLinkActivity.setStatus("current")


class _AluMwNotifyLinkProtectionType_Type(Integer32):
    """Custom type aluMwNotifyLinkProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eps", 1),
          ("tps", 2),
          ("rps", 3))
    )


_AluMwNotifyLinkProtectionType_Type.__name__ = "Integer32"
_AluMwNotifyLinkProtectionType_Object = MibScalar
aluMwNotifyLinkProtectionType = _AluMwNotifyLinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 12),
    _AluMwNotifyLinkProtectionType_Type()
)
aluMwNotifyLinkProtectionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyLinkProtectionType.setStatus("current")
_AluMwNotifyRadioSwState_Type = AluMwRadioSwState
_AluMwNotifyRadioSwState_Object = MibScalar
aluMwNotifyRadioSwState = _AluMwNotifyRadioSwState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 7, 2, 13),
    _AluMwNotifyRadioSwState_Type()
)
aluMwNotifyRadioSwState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aluMwNotifyRadioSwState.setStatus("current")
_AluMwNotifyPrefix_ObjectIdentity = ObjectIdentity
aluMwNotifyPrefix = _AluMwNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10)
)
_AluMwNotification_ObjectIdentity = ObjectIdentity
aluMwNotification = _AluMwNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0)
)

# Managed Objects groups

aluMwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2, 1)
)
aluMwGroup.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwRadioRowStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMode"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMwLinkID"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioOperStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioOperFlags"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRowStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkOperFlags"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRadioScheme"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkEPSActivity"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRPSActivity"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTPSActivity"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkEPSRevertiveness"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTPSRevertiveness"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRPSRevertiveness"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkEPSMainMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkEPSSpareMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTPSMainMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTPSSpareMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRPSMainMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRPSSpareMaintOp"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkPeerID"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkPeerNEIpAddress"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkClearStatistics"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioStandalone"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioName"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioDatabaseFilename"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioType"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioFrequency"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCompanyId"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMnemonic"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCLEI"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioHwPartNumber"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSwPartNumber"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioFactoryId"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSerialNumber"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMfgDateId"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMfgDate"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCustomerField"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmState"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsCritical"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsMajor"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsMinor"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsWarning"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsInd"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsCommunication"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmsEquipment"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioTxMuted"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioReboot"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioLastStateChange"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioInfoValid"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioTemperature"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCommEstablished"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioLocalTxPower"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioLocalRxMainPower"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRemoteTxPower"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRemoteRxMainPower"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAggrFramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAggrOctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAggrDiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue1FramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue1OctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue1DiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue2FramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue2OctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue2DiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue3FramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue3OctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue3DiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue4FramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue4OctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue4DiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue5FramesTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue5OctetsTx"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkQueue5DiscardedTx"),
        ("ALU-MICROWAVE-MIB", "aluMwSwPackageValid"),
        ("ALU-MICROWAVE-MIB", "aluMwSwDownloadTool"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSwState"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSwDnldProgress"),
        ("ALU-MICROWAVE-MIB", "aluMwSwDownloadState"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRslHistoryUrl"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRslHistoryClear"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTdaCmdState"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTdaManualCmdStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTdaSwitchPosition"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioLocalDiversityPower"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRemoteDiversityPower"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioFfdSuppressFlags"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMG826Enable"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMG826OperStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMG826Clear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMACMEnable"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMACMOperStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMACMClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMPowerEnable"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMPowerOperStatus"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMPowerClear"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Section"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Period"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Bin"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Date"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Duration"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826EPSState"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826Suspect"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826ES"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826SES"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826BBE"),
        ("ALU-MICROWAVE-MIB", "aluMwPMG826UAS"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMPeriod"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMBin"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMModulation"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMDate"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMDuration"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMSuspect"),
        ("ALU-MICROWAVE-MIB", "aluMwPMACMTimeSpent"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerDirection"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerSection"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerPeriod"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerBin"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerDate"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerDuration"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerEPSState"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerSuspect"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerMinPowerLevel"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerMaxPowerLevel"),
        ("ALU-MICROWAVE-MIB", "aluMwPMPowerMeanPowerLevel"))
)
if mibBuilder.loadTexts:
    aluMwGroup.setStatus("current")

aluMwNotificationObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2, 3)
)
aluMwNotificationObjsGroup.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyTxMute"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkActivity"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkProtectionType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioSwState"))
)
if mibBuilder.loadTexts:
    aluMwNotificationObjsGroup.setStatus("current")

aluMwPeerDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2, 4)
)
aluMwPeerDiscoveryGroup.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwLinkPeerDiscovery")
)
if mibBuilder.loadTexts:
    aluMwPeerDiscoveryGroup.setStatus("current")

aluMwAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2, 5)
)
aluMwAlarmGroup.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwLinkAlarmState"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsCommunication"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsCritical"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsEquipment"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsInd"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsMajor"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsMinor"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkAlarmsWarning"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmSeverity"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmSubObject"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCommLost"))
)
if mibBuilder.loadTexts:
    aluMwAlarmGroup.setStatus("current")


# Notification objects

aluMwRadioLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 1)
)
aluMwRadioLinkUp.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioLinkUp.setStatus(
        "current"
    )

aluMwRadioLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 2)
)
aluMwRadioLinkDown.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioLinkDown.setStatus(
        "current"
    )

aluMwRadioPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 3)
)
aluMwRadioPresent.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPresent.setStatus(
        "current"
    )

aluMwRadioNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 4)
)
aluMwRadioNotPresent.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioNotPresent.setStatus(
        "current"
    )

aluMwRadioSwPackageMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 5)
)
if mibBuilder.loadTexts:
    aluMwRadioSwPackageMissing.setStatus(
        "current"
    )

aluMwRadioDatabaseUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 6)
)
aluMwRadioDatabaseUpdated.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioDatabaseUpdated.setStatus(
        "current"
    )

aluMwRadioCriticalAlarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 7)
)
aluMwRadioCriticalAlarmRaise.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioCriticalAlarmRaise.setStatus(
        "current"
    )

aluMwRadioCriticalAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 8)
)
aluMwRadioCriticalAlarmClear.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioCriticalAlarmClear.setStatus(
        "current"
    )

aluMwRadioMajorAlarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 9)
)
aluMwRadioMajorAlarmRaise.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioMajorAlarmRaise.setStatus(
        "current"
    )

aluMwRadioMajorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 10)
)
aluMwRadioMajorAlarmClear.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioMajorAlarmClear.setStatus(
        "current"
    )

aluMwRadioMinorAlarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 11)
)
aluMwRadioMinorAlarmRaise.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioMinorAlarmRaise.setStatus(
        "current"
    )

aluMwRadioMinorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 12)
)
aluMwRadioMinorAlarmClear.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioMinorAlarmClear.setStatus(
        "current"
    )

aluMwRadioWarningAlarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 13)
)
aluMwRadioWarningAlarmRaise.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioWarningAlarmRaise.setStatus(
        "current"
    )

aluMwRadioWarningAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 14)
)
aluMwRadioWarningAlarmClear.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioWarningAlarmClear.setStatus(
        "current"
    )

aluMwRadioIndetermAlarmRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 15)
)
aluMwRadioIndetermAlarmRaise.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioIndetermAlarmRaise.setStatus(
        "current"
    )

aluMwRadioIndetermAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 16)
)
aluMwRadioIndetermAlarmClear.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmId"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmTime"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmName"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSpecProblem"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmType"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmObject"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyAlarmSubObject"))
)
if mibBuilder.loadTexts:
    aluMwRadioIndetermAlarmClear.setStatus(
        "current"
    )

aluMwRadioTxChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 17)
)
aluMwRadioTxChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyTxMute"))
)
if mibBuilder.loadTexts:
    aluMwRadioTxChange.setStatus(
        "current"
    )

aluMwLinkEPSActivityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 18)
)
aluMwLinkEPSActivityChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkActivity"))
)
if mibBuilder.loadTexts:
    aluMwLinkEPSActivityChange.setStatus(
        "current"
    )

aluMwLinkTPSActivityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 19)
)
aluMwLinkTPSActivityChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkActivity"))
)
if mibBuilder.loadTexts:
    aluMwLinkTPSActivityChange.setStatus(
        "current"
    )

aluMwLinkRPSActivityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 20)
)
aluMwLinkRPSActivityChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkActivity"))
)
if mibBuilder.loadTexts:
    aluMwLinkRPSActivityChange.setStatus(
        "current"
    )

aluMwLinkMaintenanceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 21)
)
aluMwLinkMaintenanceChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkProtectionType"))
)
if mibBuilder.loadTexts:
    aluMwLinkMaintenanceChange.setStatus(
        "current"
    )

aluMwLinkPeerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 22)
)
aluMwLinkPeerChange.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyLinkPortID")
)
if mibBuilder.loadTexts:
    aluMwLinkPeerChange.setStatus(
        "current"
    )

aluMwRadioSwStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 23)
)
aluMwRadioSwStateChange.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID"),
        ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioSwState"))
)
if mibBuilder.loadTexts:
    aluMwRadioSwStateChange.setStatus(
        "current"
    )

aluMwRadioRslHistoryUploadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 24)
)
aluMwRadioRslHistoryUploadFail.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioRslHistoryUploadFail.setStatus(
        "current"
    )

aluMwMptSwReconcileFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 25)
)
if mibBuilder.loadTexts:
    aluMwMptSwReconcileFail.setStatus(
        "current"
    )

aluMwRadioRslHistoryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 26)
)
if mibBuilder.loadTexts:
    aluMwRadioRslHistoryCleared.setStatus(
        "current"
    )

aluMwRadioPMG826OperUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 27)
)
aluMwRadioPMG826OperUp.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMG826OperUp.setStatus(
        "current"
    )

aluMwRadioPMG826OperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 28)
)
aluMwRadioPMG826OperDown.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMG826OperDown.setStatus(
        "current"
    )

aluMwRadioPMACMOperUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 29)
)
aluMwRadioPMACMOperUp.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMACMOperUp.setStatus(
        "current"
    )

aluMwRadioPMACMOperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 30)
)
aluMwRadioPMACMOperDown.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMACMOperDown.setStatus(
        "current"
    )

aluMwRadioPMPowerOperUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 31)
)
aluMwRadioPMPowerOperUp.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMPowerOperUp.setStatus(
        "current"
    )

aluMwRadioPMPowerOperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 10, 0, 32)
)
aluMwRadioPMPowerOperDown.setObjects(
    ("ALU-MICROWAVE-MIB", "aluMwNotifyRadioPortID")
)
if mibBuilder.loadTexts:
    aluMwRadioPMPowerOperDown.setStatus(
        "current"
    )


# Notifications groups

aluMwNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 2, 2)
)
aluMwNotificationGroup.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwRadioLinkUp"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioLinkDown"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPresent"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioNotPresent"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSwPackageMissing"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioDatabaseUpdated"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCriticalAlarmRaise"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioCriticalAlarmClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMajorAlarmRaise"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMajorAlarmClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMinorAlarmRaise"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioMinorAlarmClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioWarningAlarmRaise"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioWarningAlarmClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioIndetermAlarmRaise"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioIndetermAlarmClear"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioTxChange"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkEPSActivityChange"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkTPSActivityChange"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkRPSActivityChange"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkMaintenanceChange"),
        ("ALU-MICROWAVE-MIB", "aluMwLinkPeerChange"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioSwStateChange"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRslHistoryUploadFail"),
        ("ALU-MICROWAVE-MIB", "aluMwMptSwReconcileFail"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioRslHistoryCleared"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMG826OperUp"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMG826OperDown"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMACMOperUp"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMACMOperDown"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMPowerOperUp"),
        ("ALU-MICROWAVE-MIB", "aluMwRadioPMPowerOperDown"))
)
if mibBuilder.loadTexts:
    aluMwNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluMwComp7705V1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 7, 1, 1, 1, 1)
)
aluMwComp7705V1v0.setObjects(
      *(("ALU-MICROWAVE-MIB", "aluMwGroup"),
        ("ALU-MICROWAVE-MIB", "aluMwNotificationGroup"),
        ("ALU-MICROWAVE-MIB", "aluMwPeerDiscoveryGroup"),
        ("ALU-MICROWAVE-MIB", "aluMwAlarmGroup"))
)
if mibBuilder.loadTexts:
    aluMwComp7705V1v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-MICROWAVE-MIB",
    **{"AluMwLinkID": AluMwLinkID,
       "AluMwLinkRadioActivity": AluMwLinkRadioActivity,
       "AluMwLinkRevertiveness": AluMwLinkRevertiveness,
       "AluMwLinkMaintenanceOp": AluMwLinkMaintenanceOp,
       "AluMwRadioSwState": AluMwRadioSwState,
       "AluMwPerfMonSection": AluMwPerfMonSection,
       "AluMwPerfMonPeriod": AluMwPerfMonPeriod,
       "AluMwPerfMonBin": AluMwPerfMonBin,
       "AluMwPerfMonEPSState": AluMwPerfMonEPSState,
       "aluMwMIBModule": aluMwMIBModule,
       "aluMwMIBConformance": aluMwMIBConformance,
       "aluMwConformance": aluMwConformance,
       "aluMwCompliances": aluMwCompliances,
       "aluMwComp7705": aluMwComp7705,
       "aluMwComp7705V1v0": aluMwComp7705V1v0,
       "aluMwGroups": aluMwGroups,
       "aluMwGroup": aluMwGroup,
       "aluMwNotificationGroup": aluMwNotificationGroup,
       "aluMwNotificationObjsGroup": aluMwNotificationObjsGroup,
       "aluMwPeerDiscoveryGroup": aluMwPeerDiscoveryGroup,
       "aluMwAlarmGroup": aluMwAlarmGroup,
       "aluMwObjPrefix": aluMwObjPrefix,
       "aluMwObjs": aluMwObjs,
       "aluMwLinkTable": aluMwLinkTable,
       "aluMwLinkEntry": aluMwLinkEntry,
       "aluMwLinkID": aluMwLinkID,
       "aluMwLinkRowStatus": aluMwLinkRowStatus,
       "aluMwLinkOperFlags": aluMwLinkOperFlags,
       "aluMwLinkRadioScheme": aluMwLinkRadioScheme,
       "aluMwLinkAlarmState": aluMwLinkAlarmState,
       "aluMwLinkAlarmsCritical": aluMwLinkAlarmsCritical,
       "aluMwLinkAlarmsMajor": aluMwLinkAlarmsMajor,
       "aluMwLinkAlarmsMinor": aluMwLinkAlarmsMinor,
       "aluMwLinkAlarmsWarning": aluMwLinkAlarmsWarning,
       "aluMwLinkAlarmsInd": aluMwLinkAlarmsInd,
       "aluMwLinkAlarmsCommunication": aluMwLinkAlarmsCommunication,
       "aluMwLinkAlarmsEquipment": aluMwLinkAlarmsEquipment,
       "aluMwLinkEPSActivity": aluMwLinkEPSActivity,
       "aluMwLinkTPSActivity": aluMwLinkTPSActivity,
       "aluMwLinkRPSActivity": aluMwLinkRPSActivity,
       "aluMwLinkEPSRevertiveness": aluMwLinkEPSRevertiveness,
       "aluMwLinkTPSRevertiveness": aluMwLinkTPSRevertiveness,
       "aluMwLinkRPSRevertiveness": aluMwLinkRPSRevertiveness,
       "aluMwLinkEPSMainMaintOp": aluMwLinkEPSMainMaintOp,
       "aluMwLinkEPSSpareMaintOp": aluMwLinkEPSSpareMaintOp,
       "aluMwLinkTPSMainMaintOp": aluMwLinkTPSMainMaintOp,
       "aluMwLinkTPSSpareMaintOp": aluMwLinkTPSSpareMaintOp,
       "aluMwLinkRPSMainMaintOp": aluMwLinkRPSMainMaintOp,
       "aluMwLinkRPSSpareMaintOp": aluMwLinkRPSSpareMaintOp,
       "aluMwLinkPeerID": aluMwLinkPeerID,
       "aluMwLinkPeerNEIpAddress": aluMwLinkPeerNEIpAddress,
       "aluMwLinkClearStatistics": aluMwLinkClearStatistics,
       "aluMwLinkPeerDiscovery": aluMwLinkPeerDiscovery,
       "aluMwRadioTable": aluMwRadioTable,
       "aluMwRadioEntry": aluMwRadioEntry,
       "aluMwRadioPortID": aluMwRadioPortID,
       "aluMwRadioRowStatus": aluMwRadioRowStatus,
       "aluMwRadioMode": aluMwRadioMode,
       "aluMwRadioMwLinkID": aluMwRadioMwLinkID,
       "aluMwRadioOperStatus": aluMwRadioOperStatus,
       "aluMwRadioOperFlags": aluMwRadioOperFlags,
       "aluMwRadioStandalone": aluMwRadioStandalone,
       "aluMwRadioName": aluMwRadioName,
       "aluMwRadioDatabaseFilename": aluMwRadioDatabaseFilename,
       "aluMwRadioType": aluMwRadioType,
       "aluMwRadioFrequency": aluMwRadioFrequency,
       "aluMwRadioAlarmState": aluMwRadioAlarmState,
       "aluMwRadioAlarmsCritical": aluMwRadioAlarmsCritical,
       "aluMwRadioAlarmsMajor": aluMwRadioAlarmsMajor,
       "aluMwRadioAlarmsMinor": aluMwRadioAlarmsMinor,
       "aluMwRadioAlarmsWarning": aluMwRadioAlarmsWarning,
       "aluMwRadioAlarmsInd": aluMwRadioAlarmsInd,
       "aluMwRadioAlarmsCommunication": aluMwRadioAlarmsCommunication,
       "aluMwRadioAlarmsEquipment": aluMwRadioAlarmsEquipment,
       "aluMwRadioTxMuted": aluMwRadioTxMuted,
       "aluMwRadioReboot": aluMwRadioReboot,
       "aluMwRadioLastStateChange": aluMwRadioLastStateChange,
       "aluMwRadioCommEstablished": aluMwRadioCommEstablished,
       "aluMwRadioCommLost": aluMwRadioCommLost,
       "aluMwRadioSwState": aluMwRadioSwState,
       "aluMwRadioSwDnldProgress": aluMwRadioSwDnldProgress,
       "aluMwRadioRslHistoryUrl": aluMwRadioRslHistoryUrl,
       "aluMwRadioRslHistoryClear": aluMwRadioRslHistoryClear,
       "aluMwRadioFfdSuppressFlags": aluMwRadioFfdSuppressFlags,
       "aluMwRadioPMG826Enable": aluMwRadioPMG826Enable,
       "aluMwRadioPMG826OperStatus": aluMwRadioPMG826OperStatus,
       "aluMwRadioPMG826Clear": aluMwRadioPMG826Clear,
       "aluMwRadioPMACMEnable": aluMwRadioPMACMEnable,
       "aluMwRadioPMACMOperStatus": aluMwRadioPMACMOperStatus,
       "aluMwRadioPMACMClear": aluMwRadioPMACMClear,
       "aluMwRadioPMPowerEnable": aluMwRadioPMPowerEnable,
       "aluMwRadioPMPowerOperStatus": aluMwRadioPMPowerOperStatus,
       "aluMwRadioPMPowerClear": aluMwRadioPMPowerClear,
       "aluMwRadioPowerMeasuresTable": aluMwRadioPowerMeasuresTable,
       "aluMwRadioPowerMeasuresEntry": aluMwRadioPowerMeasuresEntry,
       "aluMwRadioLocalTxPower": aluMwRadioLocalTxPower,
       "aluMwRadioLocalRxMainPower": aluMwRadioLocalRxMainPower,
       "aluMwRadioRemoteTxPower": aluMwRadioRemoteTxPower,
       "aluMwRadioRemoteRxMainPower": aluMwRadioRemoteRxMainPower,
       "aluMwRadioLocalDiversityPower": aluMwRadioLocalDiversityPower,
       "aluMwRadioRemoteDiversityPower": aluMwRadioRemoteDiversityPower,
       "aluMwRadioAlarmsTable": aluMwRadioAlarmsTable,
       "aluMwRadioAlarmsEntry": aluMwRadioAlarmsEntry,
       "aluMwRadioAlarmID": aluMwRadioAlarmID,
       "aluMwRadioAlarmTime": aluMwRadioAlarmTime,
       "aluMwRadioAlarmName": aluMwRadioAlarmName,
       "aluMwRadioAlarmSeverity": aluMwRadioAlarmSeverity,
       "aluMwRadioAlarmSpecProblem": aluMwRadioAlarmSpecProblem,
       "aluMwRadioAlarmType": aluMwRadioAlarmType,
       "aluMwRadioAlarmObject": aluMwRadioAlarmObject,
       "aluMwRadioAlarmSubObject": aluMwRadioAlarmSubObject,
       "aluMwLinkStatisticsTable": aluMwLinkStatisticsTable,
       "aluMwLinkStatisticsEntry": aluMwLinkStatisticsEntry,
       "aluMwLinkAggrFramesTx": aluMwLinkAggrFramesTx,
       "aluMwLinkAggrOctetsTx": aluMwLinkAggrOctetsTx,
       "aluMwLinkAggrDiscardedTx": aluMwLinkAggrDiscardedTx,
       "aluMwLinkQueue1FramesTx": aluMwLinkQueue1FramesTx,
       "aluMwLinkQueue1OctetsTx": aluMwLinkQueue1OctetsTx,
       "aluMwLinkQueue1DiscardedTx": aluMwLinkQueue1DiscardedTx,
       "aluMwLinkQueue2FramesTx": aluMwLinkQueue2FramesTx,
       "aluMwLinkQueue2OctetsTx": aluMwLinkQueue2OctetsTx,
       "aluMwLinkQueue2DiscardedTx": aluMwLinkQueue2DiscardedTx,
       "aluMwLinkQueue3FramesTx": aluMwLinkQueue3FramesTx,
       "aluMwLinkQueue3OctetsTx": aluMwLinkQueue3OctetsTx,
       "aluMwLinkQueue3DiscardedTx": aluMwLinkQueue3DiscardedTx,
       "aluMwLinkQueue4FramesTx": aluMwLinkQueue4FramesTx,
       "aluMwLinkQueue4OctetsTx": aluMwLinkQueue4OctetsTx,
       "aluMwLinkQueue4DiscardedTx": aluMwLinkQueue4DiscardedTx,
       "aluMwLinkQueue5FramesTx": aluMwLinkQueue5FramesTx,
       "aluMwLinkQueue5OctetsTx": aluMwLinkQueue5OctetsTx,
       "aluMwLinkQueue5DiscardedTx": aluMwLinkQueue5DiscardedTx,
       "aluMwRadioInfoTable": aluMwRadioInfoTable,
       "aluMwRadioInfoEntry": aluMwRadioInfoEntry,
       "aluMwRadioInfoValid": aluMwRadioInfoValid,
       "aluMwRadioCompanyId": aluMwRadioCompanyId,
       "aluMwRadioMnemonic": aluMwRadioMnemonic,
       "aluMwRadioCLEI": aluMwRadioCLEI,
       "aluMwRadioHwPartNumber": aluMwRadioHwPartNumber,
       "aluMwRadioSwPartNumber": aluMwRadioSwPartNumber,
       "aluMwRadioFactoryId": aluMwRadioFactoryId,
       "aluMwRadioSerialNumber": aluMwRadioSerialNumber,
       "aluMwRadioMfgDateId": aluMwRadioMfgDateId,
       "aluMwRadioMfgDate": aluMwRadioMfgDate,
       "aluMwRadioCustomerField": aluMwRadioCustomerField,
       "aluMwRadioTemperature": aluMwRadioTemperature,
       "aluMwTable": aluMwTable,
       "aluMwEntry": aluMwEntry,
       "aluMwSwPackageValid": aluMwSwPackageValid,
       "aluMwSwDownloadTool": aluMwSwDownloadTool,
       "aluMwSwDownloadState": aluMwSwDownloadState,
       "aluMwLinkTdaStatusTable": aluMwLinkTdaStatusTable,
       "aluMwLinkTdaStatusEntry": aluMwLinkTdaStatusEntry,
       "aluMwLinkTdaCmdState": aluMwLinkTdaCmdState,
       "aluMwLinkTdaManualCmdStatus": aluMwLinkTdaManualCmdStatus,
       "aluMwLinkTdaSwitchPosition": aluMwLinkTdaSwitchPosition,
       "aluMwRadioPMG826Table": aluMwRadioPMG826Table,
       "aluMwRadioPMG826Entry": aluMwRadioPMG826Entry,
       "aluMwPMG826Section": aluMwPMG826Section,
       "aluMwPMG826Period": aluMwPMG826Period,
       "aluMwPMG826Bin": aluMwPMG826Bin,
       "aluMwPMG826Date": aluMwPMG826Date,
       "aluMwPMG826Duration": aluMwPMG826Duration,
       "aluMwPMG826EPSState": aluMwPMG826EPSState,
       "aluMwPMG826Suspect": aluMwPMG826Suspect,
       "aluMwPMG826ES": aluMwPMG826ES,
       "aluMwPMG826SES": aluMwPMG826SES,
       "aluMwPMG826BBE": aluMwPMG826BBE,
       "aluMwPMG826UAS": aluMwPMG826UAS,
       "aluMwRadioPMACMTable": aluMwRadioPMACMTable,
       "aluMwRadioPMACMEntry": aluMwRadioPMACMEntry,
       "aluMwPMACMPeriod": aluMwPMACMPeriod,
       "aluMwPMACMBin": aluMwPMACMBin,
       "aluMwPMACMModulation": aluMwPMACMModulation,
       "aluMwPMACMDate": aluMwPMACMDate,
       "aluMwPMACMDuration": aluMwPMACMDuration,
       "aluMwPMACMSuspect": aluMwPMACMSuspect,
       "aluMwPMACMTimeSpent": aluMwPMACMTimeSpent,
       "aluMwRadioPMPowerTable": aluMwRadioPMPowerTable,
       "aluMwRadioPMPowerEntry": aluMwRadioPMPowerEntry,
       "aluMwPMPowerDirection": aluMwPMPowerDirection,
       "aluMwPMPowerSection": aluMwPMPowerSection,
       "aluMwPMPowerPeriod": aluMwPMPowerPeriod,
       "aluMwPMPowerBin": aluMwPMPowerBin,
       "aluMwPMPowerDate": aluMwPMPowerDate,
       "aluMwPMPowerDuration": aluMwPMPowerDuration,
       "aluMwPMPowerEPSState": aluMwPMPowerEPSState,
       "aluMwPMPowerSuspect": aluMwPMPowerSuspect,
       "aluMwPMPowerMinPowerLevel": aluMwPMPowerMinPowerLevel,
       "aluMwPMPowerMaxPowerLevel": aluMwPMPowerMaxPowerLevel,
       "aluMwPMPowerMeanPowerLevel": aluMwPMPowerMeanPowerLevel,
       "aluMwNotifyObjs": aluMwNotifyObjs,
       "aluMwNotifyRadioPortID": aluMwNotifyRadioPortID,
       "aluMwNotifyAlarmTime": aluMwNotifyAlarmTime,
       "aluMwNotifyAlarmId": aluMwNotifyAlarmId,
       "aluMwNotifyAlarmName": aluMwNotifyAlarmName,
       "aluMwNotifyAlarmSpecProblem": aluMwNotifyAlarmSpecProblem,
       "aluMwNotifyAlarmType": aluMwNotifyAlarmType,
       "aluMwNotifyAlarmObject": aluMwNotifyAlarmObject,
       "aluMwNotifyAlarmSubObject": aluMwNotifyAlarmSubObject,
       "aluMwNotifyTxMute": aluMwNotifyTxMute,
       "aluMwNotifyLinkPortID": aluMwNotifyLinkPortID,
       "aluMwNotifyLinkActivity": aluMwNotifyLinkActivity,
       "aluMwNotifyLinkProtectionType": aluMwNotifyLinkProtectionType,
       "aluMwNotifyRadioSwState": aluMwNotifyRadioSwState,
       "aluMwNotifyPrefix": aluMwNotifyPrefix,
       "aluMwNotification": aluMwNotification,
       "aluMwRadioLinkUp": aluMwRadioLinkUp,
       "aluMwRadioLinkDown": aluMwRadioLinkDown,
       "aluMwRadioPresent": aluMwRadioPresent,
       "aluMwRadioNotPresent": aluMwRadioNotPresent,
       "aluMwRadioSwPackageMissing": aluMwRadioSwPackageMissing,
       "aluMwRadioDatabaseUpdated": aluMwRadioDatabaseUpdated,
       "aluMwRadioCriticalAlarmRaise": aluMwRadioCriticalAlarmRaise,
       "aluMwRadioCriticalAlarmClear": aluMwRadioCriticalAlarmClear,
       "aluMwRadioMajorAlarmRaise": aluMwRadioMajorAlarmRaise,
       "aluMwRadioMajorAlarmClear": aluMwRadioMajorAlarmClear,
       "aluMwRadioMinorAlarmRaise": aluMwRadioMinorAlarmRaise,
       "aluMwRadioMinorAlarmClear": aluMwRadioMinorAlarmClear,
       "aluMwRadioWarningAlarmRaise": aluMwRadioWarningAlarmRaise,
       "aluMwRadioWarningAlarmClear": aluMwRadioWarningAlarmClear,
       "aluMwRadioIndetermAlarmRaise": aluMwRadioIndetermAlarmRaise,
       "aluMwRadioIndetermAlarmClear": aluMwRadioIndetermAlarmClear,
       "aluMwRadioTxChange": aluMwRadioTxChange,
       "aluMwLinkEPSActivityChange": aluMwLinkEPSActivityChange,
       "aluMwLinkTPSActivityChange": aluMwLinkTPSActivityChange,
       "aluMwLinkRPSActivityChange": aluMwLinkRPSActivityChange,
       "aluMwLinkMaintenanceChange": aluMwLinkMaintenanceChange,
       "aluMwLinkPeerChange": aluMwLinkPeerChange,
       "aluMwRadioSwStateChange": aluMwRadioSwStateChange,
       "aluMwRadioRslHistoryUploadFail": aluMwRadioRslHistoryUploadFail,
       "aluMwMptSwReconcileFail": aluMwMptSwReconcileFail,
       "aluMwRadioRslHistoryCleared": aluMwRadioRslHistoryCleared,
       "aluMwRadioPMG826OperUp": aluMwRadioPMG826OperUp,
       "aluMwRadioPMG826OperDown": aluMwRadioPMG826OperDown,
       "aluMwRadioPMACMOperUp": aluMwRadioPMACMOperUp,
       "aluMwRadioPMACMOperDown": aluMwRadioPMACMOperDown,
       "aluMwRadioPMPowerOperUp": aluMwRadioPMPowerOperUp,
       "aluMwRadioPMPowerOperDown": aluMwRadioPMPowerOperDown}
)
