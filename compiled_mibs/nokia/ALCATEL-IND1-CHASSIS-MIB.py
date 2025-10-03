# SNMP MIB module (ALCATEL-IND1-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:09 2025
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

(chassisTraps,
 hardentIND1Chassis,
 hardentIND1Physical) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "chassisTraps",
    "hardentIND1Chassis",
    "hardentIND1Physical")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1ChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIB.setRevisions(
        ("2009-06-09 00:00",
         "2009-06-26 00:00",
         "2007-06-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChasEntPhysLed(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("off", 1),
          ("greenOn", 2),
          ("greenBlink", 3),
          ("amberOn", 4),
          ("amberBlink", 5))
    )



class ChasEntPhysPowerType(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("ac", 1),
          ("dc", 2))
    )



class ChassisTrapsStrLevel(TextualConvention, Integer32):
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
        *(("strNotFatal", 1),
          ("strApplicationFatal", 2),
          ("strFatal", 3))
    )



class ChassisTrapsStrAppID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsStrSnapID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsStrfileLineNb(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class ChassisTrapsStrErrorNb(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ChassisTrapsStrdataInfo(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )



class ChassisTrapsObjectType(TextualConvention, Integer32):
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
        *(("chassis", 1),
          ("ni", 2),
          ("powerSuply", 3),
          ("fan", 4),
          ("cmm", 5),
          ("fabric", 6),
          ("gbic", 7))
    )



class ChassisTrapsObjectNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ChassisTrapsAlertNumber(TextualConvention, Integer32):
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
              57)
        )
    )
    namedValues = NamedValues(
        *(("runningWorking", 1),
          ("runningCertified", 2),
          ("certifyStarted", 3),
          ("certifyFlashSyncStarted", 4),
          ("certifyCompleted", 5),
          ("certifyFailed", 6),
          ("synchroStarted", 7),
          ("synchroCompleted", 8),
          ("synchroFailed", 9),
          ("restoreStarted", 10),
          ("restoreCompleted", 11),
          ("restoreFailed", 12),
          ("takeoverStarted", 13),
          ("takeoverDeferred", 14),
          ("takeoverCompleted", 15),
          ("macAllocFailed", 16),
          ("macRangeFailed", 17),
          ("fanFailed", 18),
          ("fanOk", 19),
          ("fansOk", 20),
          ("tempOverThreshold", 21),
          ("tempUnderThreshold", 22),
          ("tempOverDangerThreshold", 23),
          ("powerMissing", 24),
          ("psNotOperational", 25),
          ("psOperational", 26),
          ("psAllOperational", 27),
          ("redundancyNotSupported", 28),
          ("redundancyDisabledCertifyNeeded", 29),
          ("cmmStartingAsPrimary", 30),
          ("cmmStartingAsSecondary", 31),
          ("cmmStartupCompleted", 32),
          ("cmmAPlugged", 33),
          ("cmmBPlugged", 34),
          ("cmmAUnPlugged", 35),
          ("cmmBUnPlugged", 36),
          ("lowNvramBattery", 37),
          ("notEnoughFabricsOperational", 38),
          ("simplexNoSynchro", 39),
          ("secAutoActivate", 40),
          ("secAutoCertifyStarted", 41),
          ("secAutoCertifyCompleted", 42),
          ("secInactiveReset", 43),
          ("activateScheduled", 44),
          ("activateStarted", 45),
          ("getAfileCompleted", 46),
          ("getAfileFailed", 47),
          ("sysUpdateStart", 48),
          ("sysUpdateInProgress", 49),
          ("sysUpdateError", 50),
          ("sysUpdateEnd", 51),
          ("reloadInProgress", 52),
          ("c20UpgradeOk", 53),
          ("c20UpgradeFailed", 54),
          ("c20RestoreOk", 55),
          ("c20RestoreFailed", 56),
          ("c20NiFailed", 57))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ChassisPhysMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBObjects = _AlcatelIND1ChassisPhysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBObjects.setStatus("current")
_ChasEntPhysicalTable_Object = MibTable
chasEntPhysicalTable = _ChasEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chasEntPhysicalTable.setStatus("current")
_ChasEntPhysicalEntry_Object = MibTableRow
chasEntPhysicalEntry = _ChasEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1)
)
chasEntPhysicalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasEntPhysicalEntry.setStatus("current")


class _ChasEntPhysAdminStatus_Type(Integer32):
    """Custom type chasEntPhysAdminStatus based on Integer32"""
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
        *(("unknown", 1),
          ("powerOff", 2),
          ("powerOn", 3),
          ("reset", 4),
          ("takeover", 5),
          ("resetAll", 6),
          ("standby", 7),
          ("resetWithFabric", 8),
          ("takeoverWithFabrc", 9))
    )


_ChasEntPhysAdminStatus_Type.__name__ = "Integer32"
_ChasEntPhysAdminStatus_Object = MibTableColumn
chasEntPhysAdminStatus = _ChasEntPhysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 1),
    _ChasEntPhysAdminStatus_Type()
)
chasEntPhysAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasEntPhysAdminStatus.setStatus("current")


class _ChasEntPhysOperStatus_Type(Integer32):
    """Custom type chasEntPhysOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("secondary", 5),
          ("notPresent", 6),
          ("unpowered", 7),
          ("master", 8))
    )


_ChasEntPhysOperStatus_Type.__name__ = "Integer32"
_ChasEntPhysOperStatus_Object = MibTableColumn
chasEntPhysOperStatus = _ChasEntPhysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 2),
    _ChasEntPhysOperStatus_Type()
)
chasEntPhysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysOperStatus.setStatus("current")


class _ChasEntPhysLedStatus_Type(Bits):
    """Custom type chasEntPhysLedStatus based on Bits"""
    namedValues = NamedValues(
        *(("ok1GreenLSBit", 0),
          ("ok1GreenMSBit", 1),
          ("ok1AmberLSBit", 2),
          ("ok1AmberMSBit", 3),
          ("ok2GreenLSBit", 4),
          ("ok2GreenMSBit", 5),
          ("ok2AmberLSBit", 6),
          ("ok2AmberMSBit", 7),
          ("controlGreenLSBit", 8),
          ("controlGreenMSBit", 9),
          ("controlAmberLSBIt", 10),
          ("controlAmberMSBIt", 11),
          ("fabricGreenLSBit", 12),
          ("fabricGreenMSBit", 13),
          ("fabricAmberLSBit", 14),
          ("fabricAmberMSBit", 15),
          ("tempGreenLSBit", 16),
          ("tempGreenMSBit", 17),
          ("tempAmberLSBit", 18),
          ("tempAmberMSBit", 19),
          ("fanGreenLSBit", 20),
          ("fanGreenMSBit", 21),
          ("fanAmberLSBit", 22),
          ("fanAmberMSBit", 23),
          ("powerSupGreenLSBit", 24),
          ("powerSupGreenMSBit", 25),
          ("powerSupAmberLSBit", 26),
          ("powerSupAmberMSBit", 27),
          ("backupPowerSupGreenLSBit", 28),
          ("backupPowerSupGreenMSBit", 29),
          ("backupPowerSupAmberLSBit", 30),
          ("backupPowerSupAmberMSBit", 31))
    )

_ChasEntPhysLedStatus_Type.__name__ = "Bits"
_ChasEntPhysLedStatus_Object = MibTableColumn
chasEntPhysLedStatus = _ChasEntPhysLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 3),
    _ChasEntPhysLedStatus_Type()
)
chasEntPhysLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatus.setStatus("deprecated")


class _ChasEntPhysPower_Type(Integer32):
    """Custom type chasEntPhysPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysPower_Type.__name__ = "Integer32"
_ChasEntPhysPower_Object = MibTableColumn
chasEntPhysPower = _ChasEntPhysPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 4),
    _ChasEntPhysPower_Type()
)
chasEntPhysPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPower.setStatus("current")
_ChasEntPhysModuleType_Type = SnmpAdminString
_ChasEntPhysModuleType_Object = MibTableColumn
chasEntPhysModuleType = _ChasEntPhysModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 5),
    _ChasEntPhysModuleType_Type()
)
chasEntPhysModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysModuleType.setStatus("current")


class _ChasEntPhysMfgDate_Type(SnmpAdminString):
    """Custom type chasEntPhysMfgDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ChasEntPhysMfgDate_Type.__name__ = "SnmpAdminString"
_ChasEntPhysMfgDate_Object = MibTableColumn
chasEntPhysMfgDate = _ChasEntPhysMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 6),
    _ChasEntPhysMfgDate_Type()
)
chasEntPhysMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysMfgDate.setStatus("current")


class _ChasEntPhysPartNumber_Type(SnmpAdminString):
    """Custom type chasEntPhysPartNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasEntPhysPartNumber_Type.__name__ = "SnmpAdminString"
_ChasEntPhysPartNumber_Object = MibTableColumn
chasEntPhysPartNumber = _ChasEntPhysPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 7),
    _ChasEntPhysPartNumber_Type()
)
chasEntPhysPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPartNumber.setStatus("current")
_ChasEntPhysLedStatusOk1_Type = ChasEntPhysLed
_ChasEntPhysLedStatusOk1_Object = MibTableColumn
chasEntPhysLedStatusOk1 = _ChasEntPhysLedStatusOk1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 8),
    _ChasEntPhysLedStatusOk1_Type()
)
chasEntPhysLedStatusOk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusOk1.setStatus("current")
_ChasEntPhysLedStatusOk2_Type = ChasEntPhysLed
_ChasEntPhysLedStatusOk2_Object = MibTableColumn
chasEntPhysLedStatusOk2 = _ChasEntPhysLedStatusOk2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 9),
    _ChasEntPhysLedStatusOk2_Type()
)
chasEntPhysLedStatusOk2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusOk2.setStatus("current")
_ChasEntPhysLedStatusPrimaryCMM_Type = ChasEntPhysLed
_ChasEntPhysLedStatusPrimaryCMM_Object = MibTableColumn
chasEntPhysLedStatusPrimaryCMM = _ChasEntPhysLedStatusPrimaryCMM_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 10),
    _ChasEntPhysLedStatusPrimaryCMM_Type()
)
chasEntPhysLedStatusPrimaryCMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusPrimaryCMM.setStatus("current")
_ChasEntPhysLedStatusSecondaryCMM_Type = ChasEntPhysLed
_ChasEntPhysLedStatusSecondaryCMM_Object = MibTableColumn
chasEntPhysLedStatusSecondaryCMM = _ChasEntPhysLedStatusSecondaryCMM_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 11),
    _ChasEntPhysLedStatusSecondaryCMM_Type()
)
chasEntPhysLedStatusSecondaryCMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusSecondaryCMM.setStatus("current")
_ChasEntPhysLedStatusTemperature_Type = ChasEntPhysLed
_ChasEntPhysLedStatusTemperature_Object = MibTableColumn
chasEntPhysLedStatusTemperature = _ChasEntPhysLedStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 12),
    _ChasEntPhysLedStatusTemperature_Type()
)
chasEntPhysLedStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusTemperature.setStatus("current")
_ChasEntPhysLedStatusFan_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFan_Object = MibTableColumn
chasEntPhysLedStatusFan = _ChasEntPhysLedStatusFan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 13),
    _ChasEntPhysLedStatusFan_Type()
)
chasEntPhysLedStatusFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFan.setStatus("current")
_ChasEntPhysLedStatusFan1_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFan1_Object = MibTableColumn
chasEntPhysLedStatusFan1 = _ChasEntPhysLedStatusFan1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 14),
    _ChasEntPhysLedStatusFan1_Type()
)
chasEntPhysLedStatusFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFan1.setStatus("current")
_ChasEntPhysLedStatusFan2_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFan2_Object = MibTableColumn
chasEntPhysLedStatusFan2 = _ChasEntPhysLedStatusFan2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 15),
    _ChasEntPhysLedStatusFan2_Type()
)
chasEntPhysLedStatusFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFan2.setStatus("current")
_ChasEntPhysLedStatusFan3_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFan3_Object = MibTableColumn
chasEntPhysLedStatusFan3 = _ChasEntPhysLedStatusFan3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 16),
    _ChasEntPhysLedStatusFan3_Type()
)
chasEntPhysLedStatusFan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFan3.setStatus("current")
_ChasEntPhysLedStatusBackupPS_Type = ChasEntPhysLed
_ChasEntPhysLedStatusBackupPS_Object = MibTableColumn
chasEntPhysLedStatusBackupPS = _ChasEntPhysLedStatusBackupPS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 17),
    _ChasEntPhysLedStatusBackupPS_Type()
)
chasEntPhysLedStatusBackupPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusBackupPS.setStatus("current")
_ChasEntPhysLedStatusInternalPS_Type = ChasEntPhysLed
_ChasEntPhysLedStatusInternalPS_Object = MibTableColumn
chasEntPhysLedStatusInternalPS = _ChasEntPhysLedStatusInternalPS_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 18),
    _ChasEntPhysLedStatusInternalPS_Type()
)
chasEntPhysLedStatusInternalPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusInternalPS.setStatus("current")
_ChasEntPhysLedStatusControl_Type = ChasEntPhysLed
_ChasEntPhysLedStatusControl_Object = MibTableColumn
chasEntPhysLedStatusControl = _ChasEntPhysLedStatusControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 19),
    _ChasEntPhysLedStatusControl_Type()
)
chasEntPhysLedStatusControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusControl.setStatus("current")
_ChasEntPhysLedStatusFabric_Type = ChasEntPhysLed
_ChasEntPhysLedStatusFabric_Object = MibTableColumn
chasEntPhysLedStatusFabric = _ChasEntPhysLedStatusFabric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 20),
    _ChasEntPhysLedStatusFabric_Type()
)
chasEntPhysLedStatusFabric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusFabric.setStatus("current")
_ChasEntPhysLedStatusPSU_Type = ChasEntPhysLed
_ChasEntPhysLedStatusPSU_Object = MibTableColumn
chasEntPhysLedStatusPSU = _ChasEntPhysLedStatusPSU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 21),
    _ChasEntPhysLedStatusPSU_Type()
)
chasEntPhysLedStatusPSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysLedStatusPSU.setStatus("current")


class _ChasEntPhysAsicRev_Type(SnmpAdminString):
    """Custom type chasEntPhysAsicRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysAsicRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysAsicRev_Object = MibTableColumn
chasEntPhysAsicRev = _ChasEntPhysAsicRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 22),
    _ChasEntPhysAsicRev_Type()
)
chasEntPhysAsicRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysAsicRev.setStatus("current")


class _ChasEntPhysCpldRev_Type(SnmpAdminString):
    """Custom type chasEntPhysCpldRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysCpldRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysCpldRev_Object = MibTableColumn
chasEntPhysCpldRev = _ChasEntPhysCpldRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 23),
    _ChasEntPhysCpldRev_Type()
)
chasEntPhysCpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysCpldRev.setStatus("current")


class _ChasEntPhysDefaultMinibootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysDefaultMinibootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysDefaultMinibootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysDefaultMinibootRev_Object = MibTableColumn
chasEntPhysDefaultMinibootRev = _ChasEntPhysDefaultMinibootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 24),
    _ChasEntPhysDefaultMinibootRev_Type()
)
chasEntPhysDefaultMinibootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysDefaultMinibootRev.setStatus("current")


class _ChasEntPhysBackUpMinibootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysBackUpMinibootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysBackUpMinibootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysBackUpMinibootRev_Object = MibTableColumn
chasEntPhysBackUpMinibootRev = _ChasEntPhysBackUpMinibootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 25),
    _ChasEntPhysBackUpMinibootRev_Type()
)
chasEntPhysBackUpMinibootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysBackUpMinibootRev.setStatus("current")


class _ChasEntPhysBootromRev_Type(SnmpAdminString):
    """Custom type chasEntPhysBootromRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysBootromRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysBootromRev_Object = MibTableColumn
chasEntPhysBootromRev = _ChasEntPhysBootromRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 26),
    _ChasEntPhysBootromRev_Type()
)
chasEntPhysBootromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysBootromRev.setStatus("current")


class _ChasEntPhysNiNum_Type(Integer32):
    """Custom type chasEntPhysNiNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysNiNum_Type.__name__ = "Integer32"
_ChasEntPhysNiNum_Object = MibTableColumn
chasEntPhysNiNum = _ChasEntPhysNiNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 27),
    _ChasEntPhysNiNum_Type()
)
chasEntPhysNiNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysNiNum.setStatus("current")


class _ChasEntPhysGbicNum_Type(Integer32):
    """Custom type chasEntPhysGbicNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysGbicNum_Type.__name__ = "Integer32"
_ChasEntPhysGbicNum_Object = MibTableColumn
chasEntPhysGbicNum = _ChasEntPhysGbicNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 28),
    _ChasEntPhysGbicNum_Type()
)
chasEntPhysGbicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysGbicNum.setStatus("current")


class _ChasEntPhysWaveLen_Type(Integer32):
    """Custom type chasEntPhysWaveLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysWaveLen_Type.__name__ = "Integer32"
_ChasEntPhysWaveLen_Object = MibTableColumn
chasEntPhysWaveLen = _ChasEntPhysWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 29),
    _ChasEntPhysWaveLen_Type()
)
chasEntPhysWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysWaveLen.setStatus("current")


class _ChasEntPhysUbootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysUbootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysUbootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysUbootRev_Object = MibTableColumn
chasEntPhysUbootRev = _ChasEntPhysUbootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 30),
    _ChasEntPhysUbootRev_Type()
)
chasEntPhysUbootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysUbootRev.setStatus("current")


class _ChasEntPhysUbootMinibootRev_Type(SnmpAdminString):
    """Custom type chasEntPhysUbootMinibootRev based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChasEntPhysUbootMinibootRev_Type.__name__ = "SnmpAdminString"
_ChasEntPhysUbootMinibootRev_Object = MibTableColumn
chasEntPhysUbootMinibootRev = _ChasEntPhysUbootMinibootRev_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 31),
    _ChasEntPhysUbootMinibootRev_Type()
)
chasEntPhysUbootMinibootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysUbootMinibootRev.setStatus("current")
_ChasEntPhysMacAddress_Type = MacAddress
_ChasEntPhysMacAddress_Object = MibTableColumn
chasEntPhysMacAddress = _ChasEntPhysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 32),
    _ChasEntPhysMacAddress_Type()
)
chasEntPhysMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysMacAddress.setStatus("current")


class _ChasEntPhysPoeSwVersion_Type(SnmpAdminString):
    """Custom type chasEntPhysPoeSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasEntPhysPoeSwVersion_Type.__name__ = "SnmpAdminString"
_ChasEntPhysPoeSwVersion_Object = MibTableColumn
chasEntPhysPoeSwVersion = _ChasEntPhysPoeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 33),
    _ChasEntPhysPoeSwVersion_Type()
)
chasEntPhysPoeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPoeSwVersion.setStatus("current")


class _ChasEntPhysC20LFailCont_Type(Integer32):
    """Custom type chasEntPhysC20LFailCont based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasEntPhysC20LFailCont_Type.__name__ = "Integer32"
_ChasEntPhysC20LFailCont_Object = MibTableColumn
chasEntPhysC20LFailCont = _ChasEntPhysC20LFailCont_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 34),
    _ChasEntPhysC20LFailCont_Type()
)
chasEntPhysC20LFailCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysC20LFailCont.setStatus("current")


class _ChasEntPhysCpuModel_Type(SnmpAdminString):
    """Custom type chasEntPhysCpuModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ChasEntPhysCpuModel_Type.__name__ = "SnmpAdminString"
_ChasEntPhysCpuModel_Object = MibTableColumn
chasEntPhysCpuModel = _ChasEntPhysCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 35),
    _ChasEntPhysCpuModel_Type()
)
chasEntPhysCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysCpuModel.setStatus("current")
_ChasEntPhysPowerType_Type = ChasEntPhysPowerType
_ChasEntPhysPowerType_Object = MibTableColumn
chasEntPhysPowerType = _ChasEntPhysPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 36),
    _ChasEntPhysPowerType_Type()
)
chasEntPhysPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPowerType.setStatus("current")
_ChasEntPhysPowerControlChecksum_Type = SnmpAdminString
_ChasEntPhysPowerControlChecksum_Object = MibTableColumn
chasEntPhysPowerControlChecksum = _ChasEntPhysPowerControlChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 1, 1, 1, 37),
    _ChasEntPhysPowerControlChecksum_Type()
)
chasEntPhysPowerControlChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasEntPhysPowerControlChecksum.setStatus("current")
_AlcatelIND1ChassisPhysMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBConformance = _AlcatelIND1ChassisPhysMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBConformance.setStatus("current")
_AlcatelIND1ChassisPhysMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBGroups = _AlcatelIND1ChassisPhysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBGroups.setStatus("current")
_AlcatelIND1ChassisPhysMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisPhysMIBCompliances = _AlcatelIND1ChassisPhysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBCompliances.setStatus("current")
_AlcatelIND1ChassisMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBObjects = _AlcatelIND1ChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBObjects.setStatus("current")
_ChasControlModuleTable_Object = MibTable
chasControlModuleTable = _ChasControlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    chasControlModuleTable.setStatus("current")
_ChasControlModuleEntry_Object = MibTableRow
chasControlModuleEntry = _ChasControlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1)
)
chasControlModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasControlModuleEntry.setStatus("current")


class _ChasControlRunningVersion_Type(Integer32):
    """Custom type chasControlRunningVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("working", 2),
          ("certified", 3))
    )


_ChasControlRunningVersion_Type.__name__ = "Integer32"
_ChasControlRunningVersion_Object = MibTableColumn
chasControlRunningVersion = _ChasControlRunningVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 1),
    _ChasControlRunningVersion_Type()
)
chasControlRunningVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlRunningVersion.setStatus("current")


class _ChasControlActivateTimeout_Type(Integer32):
    """Custom type chasControlActivateTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ChasControlActivateTimeout_Type.__name__ = "Integer32"
_ChasControlActivateTimeout_Object = MibTableColumn
chasControlActivateTimeout = _ChasControlActivateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 2),
    _ChasControlActivateTimeout_Type()
)
chasControlActivateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlActivateTimeout.setStatus("current")


class _ChasControlVersionMngt_Type(Integer32):
    """Custom type chasControlVersionMngt based on Integer32"""
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
        *(("notSignificant", 1),
          ("certifySynchro", 2),
          ("certifyNoSynchro", 3),
          ("flashSynchro", 4),
          ("restore", 5),
          ("activate", 6),
          ("issu", 7))
    )


_ChasControlVersionMngt_Type.__name__ = "Integer32"
_ChasControlVersionMngt_Object = MibTableColumn
chasControlVersionMngt = _ChasControlVersionMngt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 3),
    _ChasControlVersionMngt_Type()
)
chasControlVersionMngt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlVersionMngt.setStatus("current")


class _ChasControlDelayedActivateTimer_Type(Unsigned32):
    """Custom type chasControlDelayedActivateTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31622400),
    )


_ChasControlDelayedActivateTimer_Type.__name__ = "Unsigned32"
_ChasControlDelayedActivateTimer_Object = MibTableColumn
chasControlDelayedActivateTimer = _ChasControlDelayedActivateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 4),
    _ChasControlDelayedActivateTimer_Type()
)
chasControlDelayedActivateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDelayedActivateTimer.setStatus("current")


class _ChasControlCertifyStatus_Type(Integer32):
    """Custom type chasControlCertifyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("needCertify", 2),
          ("certified", 3))
    )


_ChasControlCertifyStatus_Type.__name__ = "Integer32"
_ChasControlCertifyStatus_Object = MibTableColumn
chasControlCertifyStatus = _ChasControlCertifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 5),
    _ChasControlCertifyStatus_Type()
)
chasControlCertifyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlCertifyStatus.setStatus("current")


class _ChasControlSynchronizationStatus_Type(Integer32):
    """Custom type chasControlSynchronizationStatus based on Integer32"""
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
        *(("unknown", 1),
          ("monoControlModule", 2),
          ("notSynchronized", 3),
          ("synchronized", 4))
    )


_ChasControlSynchronizationStatus_Type.__name__ = "Integer32"
_ChasControlSynchronizationStatus_Object = MibTableColumn
chasControlSynchronizationStatus = _ChasControlSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 6),
    _ChasControlSynchronizationStatus_Type()
)
chasControlSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlSynchronizationStatus.setStatus("current")


class _ChasControlAcrossCmmWorkingSynchroStatus_Type(Integer32):
    """Custom type chasControlAcrossCmmWorkingSynchroStatus based on Integer32"""
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
        *(("unknown", 1),
          ("monoCMM", 2),
          ("no", 3),
          ("yes", 4))
    )


_ChasControlAcrossCmmWorkingSynchroStatus_Type.__name__ = "Integer32"
_ChasControlAcrossCmmWorkingSynchroStatus_Object = MibTableColumn
chasControlAcrossCmmWorkingSynchroStatus = _ChasControlAcrossCmmWorkingSynchroStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 7),
    _ChasControlAcrossCmmWorkingSynchroStatus_Type()
)
chasControlAcrossCmmWorkingSynchroStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlAcrossCmmWorkingSynchroStatus.setStatus("current")


class _ChasControlAcrossCmmCertifiedSynchroStatus_Type(Integer32):
    """Custom type chasControlAcrossCmmCertifiedSynchroStatus based on Integer32"""
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
        *(("unknown", 1),
          ("monoCMM", 2),
          ("no", 3),
          ("yes", 4))
    )


_ChasControlAcrossCmmCertifiedSynchroStatus_Type.__name__ = "Integer32"
_ChasControlAcrossCmmCertifiedSynchroStatus_Object = MibTableColumn
chasControlAcrossCmmCertifiedSynchroStatus = _ChasControlAcrossCmmCertifiedSynchroStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 1, 1, 8),
    _ChasControlAcrossCmmCertifiedSynchroStatus_Type()
)
chasControlAcrossCmmCertifiedSynchroStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlAcrossCmmCertifiedSynchroStatus.setStatus("current")
_ChasControlRedundantTable_Object = MibTable
chasControlRedundantTable = _ChasControlRedundantTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    chasControlRedundantTable.setStatus("current")
_ChasControlRedundantEntry_Object = MibTableRow
chasControlRedundantEntry = _ChasControlRedundantEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 2, 1)
)
chasControlRedundantEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasControlRedundantEntry.setStatus("current")
_ChasControlNumberOfTakeover_Type = Counter32
_ChasControlNumberOfTakeover_Object = MibTableColumn
chasControlNumberOfTakeover = _ChasControlNumberOfTakeover_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 2, 1, 1),
    _ChasControlNumberOfTakeover_Type()
)
chasControlNumberOfTakeover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlNumberOfTakeover.setStatus("current")


class _ChasControlDelayedRebootTimer_Type(Unsigned32):
    """Custom type chasControlDelayedRebootTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31622400),
    )


_ChasControlDelayedRebootTimer_Type.__name__ = "Unsigned32"
_ChasControlDelayedRebootTimer_Object = MibTableColumn
chasControlDelayedRebootTimer = _ChasControlDelayedRebootTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 2, 1, 2),
    _ChasControlDelayedRebootTimer_Type()
)
chasControlDelayedRebootTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasControlDelayedRebootTimer.setStatus("current")
_ChasChassisTable_Object = MibTable
chasChassisTable = _ChasChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    chasChassisTable.setStatus("current")
_ChasChassisEntry_Object = MibTableRow
chasChassisEntry = _ChasChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1)
)
chasChassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    chasChassisEntry.setStatus("current")


class _ChasFreeSlots_Type(Unsigned32):
    """Custom type chasFreeSlots based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_ChasFreeSlots_Type.__name__ = "Unsigned32"
_ChasFreeSlots_Object = MibTableColumn
chasFreeSlots = _ChasFreeSlots_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 1),
    _ChasFreeSlots_Type()
)
chasFreeSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasFreeSlots.setStatus("current")


class _ChasPowerLeft_Type(Integer32):
    """Custom type chasPowerLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_ChasPowerLeft_Type.__name__ = "Integer32"
_ChasPowerLeft_Object = MibTableColumn
chasPowerLeft = _ChasPowerLeft_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 2),
    _ChasPowerLeft_Type()
)
chasPowerLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPowerLeft.setStatus("current")
_ChasNumberOfResets_Type = Counter32
_ChasNumberOfResets_Object = MibTableColumn
chasNumberOfResets = _ChasNumberOfResets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 3),
    _ChasNumberOfResets_Type()
)
chasNumberOfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasNumberOfResets.setStatus("current")


class _ChasHardwareBoardTemp_Type(Integer32):
    """Custom type chasHardwareBoardTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasHardwareBoardTemp_Type.__name__ = "Integer32"
_ChasHardwareBoardTemp_Object = MibTableColumn
chasHardwareBoardTemp = _ChasHardwareBoardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 4),
    _ChasHardwareBoardTemp_Type()
)
chasHardwareBoardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasHardwareBoardTemp.setStatus("current")


class _ChasHardwareCpuTemp_Type(Integer32):
    """Custom type chasHardwareCpuTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ChasHardwareCpuTemp_Type.__name__ = "Integer32"
_ChasHardwareCpuTemp_Object = MibTableColumn
chasHardwareCpuTemp = _ChasHardwareCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 5),
    _ChasHardwareCpuTemp_Type()
)
chasHardwareCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasHardwareCpuTemp.setStatus("current")


class _ChasTempRange_Type(Integer32):
    """Custom type chasTempRange based on Integer32"""
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
        *(("unknown", 1),
          ("notPresent", 2),
          ("underThreshold", 3),
          ("overFirstThreshold", 4),
          ("overDangerThreshold", 5))
    )


_ChasTempRange_Type.__name__ = "Integer32"
_ChasTempRange_Object = MibTableColumn
chasTempRange = _ChasTempRange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 6),
    _ChasTempRange_Type()
)
chasTempRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTempRange.setStatus("current")


class _ChasTempThreshold_Type(Integer32):
    """Custom type chasTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_ChasTempThreshold_Type.__name__ = "Integer32"
_ChasTempThreshold_Object = MibTableColumn
chasTempThreshold = _ChasTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 7),
    _ChasTempThreshold_Type()
)
chasTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasTempThreshold.setStatus("current")


class _ChasDangerTempThreshold_Type(Integer32):
    """Custom type chasDangerTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_ChasDangerTempThreshold_Type.__name__ = "Integer32"
_ChasDangerTempThreshold_Object = MibTableColumn
chasDangerTempThreshold = _ChasDangerTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 8),
    _ChasDangerTempThreshold_Type()
)
chasDangerTempThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasDangerTempThreshold.setStatus("current")


class _ChasPrimaryPhysicalIndex_Type(Integer32):
    """Custom type chasPrimaryPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChasPrimaryPhysicalIndex_Type.__name__ = "Integer32"
_ChasPrimaryPhysicalIndex_Object = MibTableColumn
chasPrimaryPhysicalIndex = _ChasPrimaryPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 3, 1, 9),
    _ChasPrimaryPhysicalIndex_Type()
)
chasPrimaryPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasPrimaryPhysicalIndex.setStatus("current")
_ChasSupervisionRfsLsTable_Object = MibTable
chasSupervisionRfsLsTable = _ChasSupervisionRfsLsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    chasSupervisionRfsLsTable.setStatus("current")
_ChasSupervisionRfsLsEntry_Object = MibTableRow
chasSupervisionRfsLsEntry = _ChasSupervisionRfsLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1)
)
chasSupervisionRfsLsEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsLsFileIndex"),
)
if mibBuilder.loadTexts:
    chasSupervisionRfsLsEntry.setStatus("current")


class _ChasSupervisionRfsLsFileIndex_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChasSupervisionRfsLsFileIndex_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileIndex_Object = MibTableColumn
chasSupervisionRfsLsFileIndex = _ChasSupervisionRfsLsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 1),
    _ChasSupervisionRfsLsFileIndex_Type()
)
chasSupervisionRfsLsFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileIndex.setStatus("current")
_ChasSupervisionRfsLsSlot_Type = Unsigned32
_ChasSupervisionRfsLsSlot_Object = MibTableColumn
chasSupervisionRfsLsSlot = _ChasSupervisionRfsLsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 2),
    _ChasSupervisionRfsLsSlot_Type()
)
chasSupervisionRfsLsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsSlot.setStatus("current")


class _ChasSupervisionRfsLsDirName_Type(DisplayString):
    """Custom type chasSupervisionRfsLsDirName based on DisplayString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsLsDirName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsLsDirName_Object = MibTableColumn
chasSupervisionRfsLsDirName = _ChasSupervisionRfsLsDirName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 3),
    _ChasSupervisionRfsLsDirName_Type()
)
chasSupervisionRfsLsDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsDirName.setStatus("current")


class _ChasSupervisionRfsLsFileName_Type(DisplayString):
    """Custom type chasSupervisionRfsLsFileName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ChasSupervisionRfsLsFileName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsLsFileName_Object = MibTableColumn
chasSupervisionRfsLsFileName = _ChasSupervisionRfsLsFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 4),
    _ChasSupervisionRfsLsFileName_Type()
)
chasSupervisionRfsLsFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileName.setStatus("current")


class _ChasSupervisionRfsLsFileType_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileType based on Integer32"""
    defaultValue = 3

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
        *(("file", 1),
          ("directory", 2),
          ("undefined", 3),
          ("tarArchive", 4))
    )


_ChasSupervisionRfsLsFileType_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileType_Object = MibTableColumn
chasSupervisionRfsLsFileType = _ChasSupervisionRfsLsFileType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 5),
    _ChasSupervisionRfsLsFileType_Type()
)
chasSupervisionRfsLsFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileType.setStatus("current")


class _ChasSupervisionRfsLsFileSize_Type(Unsigned32):
    """Custom type chasSupervisionRfsLsFileSize based on Unsigned32"""
    defaultValue = 0


_ChasSupervisionRfsLsFileSize_Type.__name__ = "Unsigned32"
_ChasSupervisionRfsLsFileSize_Object = MibTableColumn
chasSupervisionRfsLsFileSize = _ChasSupervisionRfsLsFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 6),
    _ChasSupervisionRfsLsFileSize_Type()
)
chasSupervisionRfsLsFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileSize.setStatus("current")


class _ChasSupervisionRfsLsFileAttr_Type(Integer32):
    """Custom type chasSupervisionRfsLsFileAttr based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("writeOnly", 4))
    )


_ChasSupervisionRfsLsFileAttr_Type.__name__ = "Integer32"
_ChasSupervisionRfsLsFileAttr_Object = MibTableColumn
chasSupervisionRfsLsFileAttr = _ChasSupervisionRfsLsFileAttr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 7),
    _ChasSupervisionRfsLsFileAttr_Type()
)
chasSupervisionRfsLsFileAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileAttr.setStatus("current")


class _ChasSupervisionRfsLsFileDateTime_Type(DisplayString):
    """Custom type chasSupervisionRfsLsFileDateTime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChasSupervisionRfsLsFileDateTime_Type.__name__ = "DisplayString"
_ChasSupervisionRfsLsFileDateTime_Object = MibTableColumn
chasSupervisionRfsLsFileDateTime = _ChasSupervisionRfsLsFileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 4, 1, 8),
    _ChasSupervisionRfsLsFileDateTime_Type()
)
chasSupervisionRfsLsFileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsLsFileDateTime.setStatus("current")
_AlcatelIND1ChassisSupervisionRfsCommands_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisSupervisionRfsCommands = _AlcatelIND1ChassisSupervisionRfsCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisSupervisionRfsCommands.setStatus("current")
_ChasSupervisionRfsCommandsSlot_Type = Unsigned32
_ChasSupervisionRfsCommandsSlot_Object = MibScalar
chasSupervisionRfsCommandsSlot = _ChasSupervisionRfsCommandsSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 1),
    _ChasSupervisionRfsCommandsSlot_Type()
)
chasSupervisionRfsCommandsSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsSlot.setStatus("current")


class _ChasSupervisionRfsCommandsCommand_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsCommand based on Integer32"""
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
        *(("notSignificant", 0),
          ("rrm", 1),
          ("rcp", 2),
          ("rls", 3),
          ("rdf", 4),
          ("reserved", 5))
    )


_ChasSupervisionRfsCommandsCommand_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsCommand_Object = MibScalar
chasSupervisionRfsCommandsCommand = _ChasSupervisionRfsCommandsCommand_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 2),
    _ChasSupervisionRfsCommandsCommand_Type()
)
chasSupervisionRfsCommandsCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsCommand.setStatus("current")


class _ChasSupervisionRfsCommandsSrcFileName_Type(DisplayString):
    """Custom type chasSupervisionRfsCommandsSrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsSrcFileName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsCommandsSrcFileName_Object = MibScalar
chasSupervisionRfsCommandsSrcFileName = _ChasSupervisionRfsCommandsSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 3),
    _ChasSupervisionRfsCommandsSrcFileName_Type()
)
chasSupervisionRfsCommandsSrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsSrcFileName.setStatus("current")


class _ChasSupervisionRfsCommandsDestFileName_Type(DisplayString):
    """Custom type chasSupervisionRfsCommandsDestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsDestFileName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsCommandsDestFileName_Object = MibScalar
chasSupervisionRfsCommandsDestFileName = _ChasSupervisionRfsCommandsDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 4),
    _ChasSupervisionRfsCommandsDestFileName_Type()
)
chasSupervisionRfsCommandsDestFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsDestFileName.setStatus("current")


class _ChasSupervisionRfsCommandsRlsDirName_Type(DisplayString):
    """Custom type chasSupervisionRfsCommandsRlsDirName based on DisplayString"""
    defaultValue = OctetString("/flash")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ChasSupervisionRfsCommandsRlsDirName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsCommandsRlsDirName_Object = MibScalar
chasSupervisionRfsCommandsRlsDirName = _ChasSupervisionRfsCommandsRlsDirName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 5),
    _ChasSupervisionRfsCommandsRlsDirName_Type()
)
chasSupervisionRfsCommandsRlsDirName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsRlsDirName.setStatus("current")


class _ChasSupervisionRfsCommandsRlsFileName_Type(DisplayString):
    """Custom type chasSupervisionRfsCommandsRlsFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_ChasSupervisionRfsCommandsRlsFileName_Type.__name__ = "DisplayString"
_ChasSupervisionRfsCommandsRlsFileName_Object = MibScalar
chasSupervisionRfsCommandsRlsFileName = _ChasSupervisionRfsCommandsRlsFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 6),
    _ChasSupervisionRfsCommandsRlsFileName_Type()
)
chasSupervisionRfsCommandsRlsFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsRlsFileName.setStatus("current")


class _ChasSupervisionRfsCommandsProcessingState_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsProcessingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("ready", 2))
    )


_ChasSupervisionRfsCommandsProcessingState_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsProcessingState_Object = MibScalar
chasSupervisionRfsCommandsProcessingState = _ChasSupervisionRfsCommandsProcessingState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 7),
    _ChasSupervisionRfsCommandsProcessingState_Type()
)
chasSupervisionRfsCommandsProcessingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsProcessingState.setStatus("current")


class _ChasSupervisionRfsCommandsStatusCode_Type(Integer32):
    """Custom type chasSupervisionRfsCommandsStatusCode based on Integer32"""
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
        *(("success", 1),
          ("slotIsPrimary", 2),
          ("slotNotExist", 3),
          ("directoryNotExist", 4),
          ("fileNotExist", 5),
          ("maximumFilesExceed", 6),
          ("noDiskSpace", 7),
          ("systemBusy", 8),
          ("systemError", 9),
          ("directoryNotAllowToRemove", 10))
    )


_ChasSupervisionRfsCommandsStatusCode_Type.__name__ = "Integer32"
_ChasSupervisionRfsCommandsStatusCode_Object = MibScalar
chasSupervisionRfsCommandsStatusCode = _ChasSupervisionRfsCommandsStatusCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 5, 8),
    _ChasSupervisionRfsCommandsStatusCode_Type()
)
chasSupervisionRfsCommandsStatusCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsCommandsStatusCode.setStatus("current")
_ChasControlReloadStatusTable_Object = MibTable
chasControlReloadStatusTable = _ChasControlReloadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    chasControlReloadStatusTable.setStatus("current")
_ChasControlReloadEntry_Object = MibTableRow
chasControlReloadEntry = _ChasControlReloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 6, 1)
)
chasControlReloadEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasControlReloadIndex"),
)
if mibBuilder.loadTexts:
    chasControlReloadEntry.setStatus("current")


class _ChasControlReloadIndex_Type(Integer32):
    """Custom type chasControlReloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChasControlReloadIndex_Type.__name__ = "Integer32"
_ChasControlReloadIndex_Object = MibTableColumn
chasControlReloadIndex = _ChasControlReloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 6, 1, 1),
    _ChasControlReloadIndex_Type()
)
chasControlReloadIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasControlReloadIndex.setStatus("current")


class _ChasControlReloadStatus_Type(Integer32):
    """Custom type chasControlReloadStatus based on Integer32"""
    defaultValue = 2

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
        *(("reloadEnabled", 1),
          ("reloadDisabled", 2),
          ("noInterface", 3),
          ("unknown", 4))
    )


_ChasControlReloadStatus_Type.__name__ = "Integer32"
_ChasControlReloadStatus_Object = MibTableColumn
chasControlReloadStatus = _ChasControlReloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 6, 1, 2),
    _ChasControlReloadStatus_Type()
)
chasControlReloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasControlReloadStatus.setStatus("current")
_ChasGlobalControl_ObjectIdentity = ObjectIdentity
chasGlobalControl = _ChasGlobalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 7)
)


class _ChasGlobalControlDelayedResetAll_Type(Integer32):
    """Custom type chasGlobalControlDelayedResetAll based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_ChasGlobalControlDelayedResetAll_Type.__name__ = "Integer32"
_ChasGlobalControlDelayedResetAll_Object = MibScalar
chasGlobalControlDelayedResetAll = _ChasGlobalControlDelayedResetAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 7, 1),
    _ChasGlobalControlDelayedResetAll_Type()
)
chasGlobalControlDelayedResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasGlobalControlDelayedResetAll.setStatus("current")


class _ChasGlobalControlLongCommand_Type(Integer32):
    """Custom type chasGlobalControlLongCommand based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("certifySynchro", 2),
          ("certifyNoSynchro", 3),
          ("flashSynchro", 4),
          ("restore", 5))
    )


_ChasGlobalControlLongCommand_Type.__name__ = "Integer32"
_ChasGlobalControlLongCommand_Object = MibScalar
chasGlobalControlLongCommand = _ChasGlobalControlLongCommand_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 7, 2),
    _ChasGlobalControlLongCommand_Type()
)
chasGlobalControlLongCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlLongCommand.setStatus("current")


class _ChasGlobalControlLongCommandStatus_Type(Integer32):
    """Custom type chasGlobalControlLongCommandStatus based on Integer32"""
    defaultValue = 1

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
          ("inProgress", 2),
          ("completeSuccess", 3),
          ("completeFailure", 4))
    )


_ChasGlobalControlLongCommandStatus_Type.__name__ = "Integer32"
_ChasGlobalControlLongCommandStatus_Object = MibScalar
chasGlobalControlLongCommandStatus = _ChasGlobalControlLongCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 7, 3),
    _ChasGlobalControlLongCommandStatus_Type()
)
chasGlobalControlLongCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasGlobalControlLongCommandStatus.setStatus("current")
_ChasSupervisionRfsDfTable_Object = MibTable
chasSupervisionRfsDfTable = _ChasSupervisionRfsDfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    chasSupervisionRfsDfTable.setStatus("current")
_ChasSupervisionRfsDfEntry_Object = MibTableRow
chasSupervisionRfsDfEntry = _ChasSupervisionRfsDfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 8, 1)
)
chasSupervisionRfsDfEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionRfsDfSlot"),
)
if mibBuilder.loadTexts:
    chasSupervisionRfsDfEntry.setStatus("current")


class _ChasSupervisionRfsDfSlot_Type(Integer32):
    """Custom type chasSupervisionRfsDfSlot based on Integer32"""
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
        *(("slot1Flash", 1),
          ("slot2Flash", 2),
          ("slot3Flash", 3),
          ("slot4Flash", 4),
          ("slot5Flash", 5),
          ("slot6Flash", 6),
          ("slot7Flash", 7),
          ("slot8Flash", 8),
          ("slot9Flash", 9),
          ("slot10Flash", 10),
          ("slot11Flash", 11),
          ("slot12Flash", 12),
          ("slot13Flash", 13),
          ("slot14Flash", 14),
          ("slot15Flash", 15),
          ("slot16Flash", 16),
          ("slot1Uflash", 17),
          ("slot2Uflash", 18),
          ("slot3Uflash", 19),
          ("slot4Uflash", 20),
          ("slot5Uflash", 21),
          ("slot6Uflash", 22),
          ("slot7Uflash", 23),
          ("slot8Uflash", 24),
          ("slot9Uflash", 25),
          ("slot10Uflash", 26),
          ("slot11Uflash", 27),
          ("slot12Uflash", 28),
          ("slot13Uflash", 29),
          ("slot14Uflash", 30),
          ("slot15Uflash", 31),
          ("slot16Uflash", 32))
    )


_ChasSupervisionRfsDfSlot_Type.__name__ = "Integer32"
_ChasSupervisionRfsDfSlot_Object = MibTableColumn
chasSupervisionRfsDfSlot = _ChasSupervisionRfsDfSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 8, 1, 1),
    _ChasSupervisionRfsDfSlot_Type()
)
chasSupervisionRfsDfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfSlot.setStatus("current")
_ChasSupervisionRfsDfFlashFree_Type = Unsigned32
_ChasSupervisionRfsDfFlashFree_Object = MibTableColumn
chasSupervisionRfsDfFlashFree = _ChasSupervisionRfsDfFlashFree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 8, 1, 2),
    _ChasSupervisionRfsDfFlashFree_Type()
)
chasSupervisionRfsDfFlashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfFlashFree.setStatus("current")
_ChasSupervisionRfsDfFlashSize_Type = Unsigned32
_ChasSupervisionRfsDfFlashSize_Object = MibTableColumn
chasSupervisionRfsDfFlashSize = _ChasSupervisionRfsDfFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 8, 1, 3),
    _ChasSupervisionRfsDfFlashSize_Type()
)
chasSupervisionRfsDfFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionRfsDfFlashSize.setStatus("current")
_ChasSupervisionFlashMemTable_Object = MibTable
chasSupervisionFlashMemTable = _ChasSupervisionFlashMemTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    chasSupervisionFlashMemTable.setStatus("current")
_ChasSupervisionFlashMemEntry_Object = MibTableRow
chasSupervisionFlashMemEntry = _ChasSupervisionFlashMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9, 1)
)
chasSupervisionFlashMemEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionSlot"),
)
if mibBuilder.loadTexts:
    chasSupervisionFlashMemEntry.setStatus("current")


class _ChasSupervisionSlot_Type(Integer32):
    """Custom type chasSupervisionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChasSupervisionSlot_Type.__name__ = "Integer32"
_ChasSupervisionSlot_Object = MibTableColumn
chasSupervisionSlot = _ChasSupervisionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9, 1, 1),
    _ChasSupervisionSlot_Type()
)
chasSupervisionSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionSlot.setStatus("current")
_ChasSupervisionFlashSize_Type = Unsigned32
_ChasSupervisionFlashSize_Object = MibTableColumn
chasSupervisionFlashSize = _ChasSupervisionFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9, 1, 2),
    _ChasSupervisionFlashSize_Type()
)
chasSupervisionFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashSize.setStatus("current")
_ChasSupervisionFlashFree_Type = Unsigned32
_ChasSupervisionFlashFree_Object = MibTableColumn
chasSupervisionFlashFree = _ChasSupervisionFlashFree_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9, 1, 3),
    _ChasSupervisionFlashFree_Type()
)
chasSupervisionFlashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashFree.setStatus("current")


class _ChasSupervisionFlashUsed_Type(Integer32):
    """Custom type chasSupervisionFlashUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChasSupervisionFlashUsed_Type.__name__ = "Integer32"
_ChasSupervisionFlashUsed_Object = MibTableColumn
chasSupervisionFlashUsed = _ChasSupervisionFlashUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 9, 1, 4),
    _ChasSupervisionFlashUsed_Type()
)
chasSupervisionFlashUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionFlashUsed.setStatus("current")
_ChasSupervisionCmmCertifiedTable_Object = MibTable
chasSupervisionCmmCertifiedTable = _ChasSupervisionCmmCertifiedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedTable.setStatus("current")
_ChasSupervisionCmmCertifiedEntry_Object = MibTableRow
chasSupervisionCmmCertifiedEntry = _ChasSupervisionCmmCertifiedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 10, 1)
)
chasSupervisionCmmCertifiedEntry.setIndexNames(
    (0, "ALCATEL-IND1-CHASSIS-MIB", "chasSupervisionCmmNum"),
)
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedEntry.setStatus("current")


class _ChasSupervisionCmmNum_Type(Integer32):
    """Custom type chasSupervisionCmmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ChasSupervisionCmmNum_Type.__name__ = "Integer32"
_ChasSupervisionCmmNum_Object = MibTableColumn
chasSupervisionCmmNum = _ChasSupervisionCmmNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 10, 1, 1),
    _ChasSupervisionCmmNum_Type()
)
chasSupervisionCmmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasSupervisionCmmNum.setStatus("current")


class _ChasSupervisionCmmCertifiedStatus_Type(Integer32):
    """Custom type chasSupervisionCmmCertifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("yes", 1),
          ("no", 2))
    )


_ChasSupervisionCmmCertifiedStatus_Type.__name__ = "Integer32"
_ChasSupervisionCmmCertifiedStatus_Object = MibTableColumn
chasSupervisionCmmCertifiedStatus = _ChasSupervisionCmmCertifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 10, 1, 2),
    _ChasSupervisionCmmCertifiedStatus_Type()
)
chasSupervisionCmmCertifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasSupervisionCmmCertifiedStatus.setStatus("current")
_AlaChasEntPhysFanTable_Object = MibTable
alaChasEntPhysFanTable = _AlaChasEntPhysFanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanTable.setStatus("current")
_AlaChasEntPhysFanEntry_Object = MibTableRow
alaChasEntPhysFanEntry = _AlaChasEntPhysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 11, 1)
)
alaChasEntPhysFanEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanLocalIndex"),
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanEntry.setStatus("current")


class _AlaChasEntPhysFanLocalIndex_Type(Integer32):
    """Custom type alaChasEntPhysFanLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaChasEntPhysFanLocalIndex_Type.__name__ = "Integer32"
_AlaChasEntPhysFanLocalIndex_Object = MibTableColumn
alaChasEntPhysFanLocalIndex = _AlaChasEntPhysFanLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 11, 1, 1),
    _AlaChasEntPhysFanLocalIndex_Type()
)
alaChasEntPhysFanLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaChasEntPhysFanLocalIndex.setStatus("current")


class _AlaChasEntPhysFanStatus_Type(Integer32):
    """Custom type alaChasEntPhysFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 0),
          ("notRunning", 1),
          ("running", 2))
    )


_AlaChasEntPhysFanStatus_Type.__name__ = "Integer32"
_AlaChasEntPhysFanStatus_Object = MibTableColumn
alaChasEntPhysFanStatus = _AlaChasEntPhysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 11, 1, 2),
    _AlaChasEntPhysFanStatus_Type()
)
alaChasEntPhysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaChasEntPhysFanStatus.setStatus("current")


class _AlaChasHashMode_Type(Integer32):
    """Custom type alaChasHashMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("brief", 1),
          ("extended", 2))
    )


_AlaChasHashMode_Type.__name__ = "Integer32"
_AlaChasHashMode_Object = MibScalar
alaChasHashMode = _AlaChasHashMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 12),
    _AlaChasHashMode_Type()
)
alaChasHashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasHashMode.setStatus("current")


class _AlaChasUdpTcpPortMode_Type(Integer32):
    """Custom type alaChasUdpTcpPortMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AlaChasUdpTcpPortMode_Type.__name__ = "Integer32"
_AlaChasUdpTcpPortMode_Object = MibScalar
alaChasUdpTcpPortMode = _AlaChasUdpTcpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 13),
    _AlaChasUdpTcpPortMode_Type()
)
alaChasUdpTcpPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasUdpTcpPortMode.setStatus("current")


class _AlaChasNonUCHashControl_Type(Integer32):
    """Custom type alaChasNonUCHashControl based on Integer32"""
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


_AlaChasNonUCHashControl_Type.__name__ = "Integer32"
_AlaChasNonUCHashControl_Object = MibScalar
alaChasNonUCHashControl = _AlaChasNonUCHashControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 1, 14),
    _AlaChasNonUCHashControl_Type()
)
alaChasNonUCHashControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaChasNonUCHashControl.setStatus("current")
_AlcatelIND1ChassisMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBConformance = _AlcatelIND1ChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBConformance.setStatus("current")
_AlcatelIND1ChassisMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBGroups = _AlcatelIND1ChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBGroups.setStatus("current")
_AlcatelIND1ChassisMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ChassisMIBCompliances = _AlcatelIND1ChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBCompliances.setStatus("current")
_ChassisTrapsDesc_ObjectIdentity = ObjectIdentity
chassisTrapsDesc = _ChassisTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 1)
)
_ChassisTrapsObj_ObjectIdentity = ObjectIdentity
chassisTrapsObj = _ChassisTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2)
)
_ChassisTrapsStrLevel_Type = ChassisTrapsStrLevel
_ChassisTrapsStrLevel_Object = MibScalar
chassisTrapsStrLevel = _ChassisTrapsStrLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 1),
    _ChassisTrapsStrLevel_Type()
)
chassisTrapsStrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrLevel.setStatus("current")
_ChassisTrapsStrAppID_Type = ChassisTrapsStrAppID
_ChassisTrapsStrAppID_Object = MibScalar
chassisTrapsStrAppID = _ChassisTrapsStrAppID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 2),
    _ChassisTrapsStrAppID_Type()
)
chassisTrapsStrAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrAppID.setStatus("current")
_ChassisTrapsStrSnapID_Type = ChassisTrapsStrSnapID
_ChassisTrapsStrSnapID_Object = MibScalar
chassisTrapsStrSnapID = _ChassisTrapsStrSnapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 3),
    _ChassisTrapsStrSnapID_Type()
)
chassisTrapsStrSnapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrSnapID.setStatus("current")


class _ChassisTrapsStrfileName_Type(SnmpAdminString):
    """Custom type chassisTrapsStrfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ChassisTrapsStrfileName_Type.__name__ = "SnmpAdminString"
_ChassisTrapsStrfileName_Object = MibScalar
chassisTrapsStrfileName = _ChassisTrapsStrfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 4),
    _ChassisTrapsStrfileName_Type()
)
chassisTrapsStrfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrfileName.setStatus("current")
_ChassisTrapsStrfileLineNb_Type = ChassisTrapsStrfileLineNb
_ChassisTrapsStrfileLineNb_Object = MibScalar
chassisTrapsStrfileLineNb = _ChassisTrapsStrfileLineNb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 5),
    _ChassisTrapsStrfileLineNb_Type()
)
chassisTrapsStrfileLineNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrfileLineNb.setStatus("current")
_ChassisTrapsStrErrorNb_Type = ChassisTrapsStrErrorNb
_ChassisTrapsStrErrorNb_Object = MibScalar
chassisTrapsStrErrorNb = _ChassisTrapsStrErrorNb_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 6),
    _ChassisTrapsStrErrorNb_Type()
)
chassisTrapsStrErrorNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrErrorNb.setStatus("current")


class _ChassisTrapsStrcomments_Type(SnmpAdminString):
    """Custom type chassisTrapsStrcomments based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ChassisTrapsStrcomments_Type.__name__ = "SnmpAdminString"
_ChassisTrapsStrcomments_Object = MibScalar
chassisTrapsStrcomments = _ChassisTrapsStrcomments_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 7),
    _ChassisTrapsStrcomments_Type()
)
chassisTrapsStrcomments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrcomments.setStatus("current")
_ChassisTrapsStrdataInfo_Type = ChassisTrapsStrdataInfo
_ChassisTrapsStrdataInfo_Object = MibScalar
chassisTrapsStrdataInfo = _ChassisTrapsStrdataInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 8),
    _ChassisTrapsStrdataInfo_Type()
)
chassisTrapsStrdataInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsStrdataInfo.setStatus("current")
_ChassisTrapsObjectType_Type = ChassisTrapsObjectType
_ChassisTrapsObjectType_Object = MibScalar
chassisTrapsObjectType = _ChassisTrapsObjectType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 9),
    _ChassisTrapsObjectType_Type()
)
chassisTrapsObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsObjectType.setStatus("current")
_ChassisTrapsObjectNumber_Type = ChassisTrapsObjectNumber
_ChassisTrapsObjectNumber_Object = MibScalar
chassisTrapsObjectNumber = _ChassisTrapsObjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 10),
    _ChassisTrapsObjectNumber_Type()
)
chassisTrapsObjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsObjectNumber.setStatus("current")
_ChassisTrapsAlertNumber_Type = ChassisTrapsAlertNumber
_ChassisTrapsAlertNumber_Object = MibScalar
chassisTrapsAlertNumber = _ChassisTrapsAlertNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 11),
    _ChassisTrapsAlertNumber_Type()
)
chassisTrapsAlertNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsAlertNumber.setStatus("current")


class _ChassisTrapsAlertDescr_Type(SnmpAdminString):
    """Custom type chassisTrapsAlertDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ChassisTrapsAlertDescr_Type.__name__ = "SnmpAdminString"
_ChassisTrapsAlertDescr_Object = MibScalar
chassisTrapsAlertDescr = _ChassisTrapsAlertDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 12),
    _ChassisTrapsAlertDescr_Type()
)
chassisTrapsAlertDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTrapsAlertDescr.setStatus("current")
_PhysicalIndex_Type = PhysicalIndex
_PhysicalIndex_Object = MibScalar
physicalIndex = _PhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 2, 13),
    _PhysicalIndex_Type()
)
physicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalIndex.setStatus("current")

# Managed Objects groups

chasEntPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2, 1, 1)
)
chasEntPhysicalGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysAdminStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysOperStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatus"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPower"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysModuleType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysMfgDate"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPartNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusOk1"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusOk2"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusPrimaryCMM"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusSecondaryCMM"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusTemperature"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFan"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFan1"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFan2"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFan3"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusBackupPS"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusInternalPS"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusControl"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusFabric"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysLedStatusPSU"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPowerType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysPowerControlChecksum"))
)
if mibBuilder.loadTexts:
    chasEntPhysicalGroup.setStatus("current")

chasControlModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 1)
)
chasControlModuleGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasControlRunningVersion"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlActivateTimeout"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlVersionMngt"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlDelayedActivateTimer"))
)
if mibBuilder.loadTexts:
    chasControlModuleGroup.setStatus("current")

chasControlRedundantGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 2)
)
chasControlRedundantGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasControlNumberOfTakeover"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlDelayedRebootTimer"))
)
if mibBuilder.loadTexts:
    chasControlRedundantGroup.setStatus("current")

chasChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 3)
)
chasChassisGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasFreeSlots"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasPowerLeft"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasNumberOfResets"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasHardwareBoardTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasHardwareCpuTemp"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTempRange"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasTempThreshold"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasDangerTempThreshold"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasPrimaryPhysicalIndex"))
)
if mibBuilder.loadTexts:
    chasChassisGroup.setStatus("current")

chasControlReloadStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 4)
)
chasControlReloadStatusGroup.setObjects(
    ("ALCATEL-IND1-CHASSIS-MIB", "chasControlReloadStatus")
)
if mibBuilder.loadTexts:
    chasControlReloadStatusGroup.setStatus("current")

chasGlobalControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 5)
)
chasGlobalControlGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlDelayedResetAll"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlLongCommand"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlLongCommandStatus"))
)
if mibBuilder.loadTexts:
    chasGlobalControlGroup.setStatus("current")

alaChasEntPhysFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 7)
)
alaChasEntPhysFanGroup.setObjects(
    ("ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanStatus")
)
if mibBuilder.loadTexts:
    alaChasEntPhysFanGroup.setStatus("current")

alaChasHashControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 8)
)
alaChasHashControlGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "alaChasHashMode"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasUdpTcpPortMode"))
)
if mibBuilder.loadTexts:
    alaChasHashControlGroup.setStatus("current")


# Notification objects

chassisTrapsStr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 1, 0, 1)
)
chassisTrapsStr.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrLevel"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrAppID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrSnapID"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileName"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrfileLineNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrErrorNb"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrcomments"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStrdataInfo"))
)
if mibBuilder.loadTexts:
    chassisTrapsStr.setStatus(
        "current"
    )

chassisTrapsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 1, 0, 2)
)
chassisTrapsAlert.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlertDescr"))
)
if mibBuilder.loadTexts:
    chassisTrapsAlert.setStatus(
        "current"
    )

chassisTrapsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 4, 1, 0, 3)
)
chassisTrapsStateChange.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectType"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsObjectNumber"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysOperStatus"))
)
if mibBuilder.loadTexts:
    chassisTrapsStateChange.setStatus(
        "current"
    )


# Notifications groups

chassisPhysNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2, 1, 2)
)
chassisPhysNotificationGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlert"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStateChange"))
)
if mibBuilder.loadTexts:
    chassisPhysNotificationGroup.setStatus(
        "current"
    )

chassisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 1, 6)
)
chassisNotificationGroup.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsStr"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisTrapsAlert"))
)
if mibBuilder.loadTexts:
    chassisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1ChassisPhysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 1, 2, 2, 1)
)
alcatelIND1ChassisPhysMIBCompliance.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasEntPhysicalGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisPhysNotificationGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisPhysMIBCompliance.setStatus(
        "current"
    )

alcatelIND1ChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 1, 1, 3, 1, 2, 2, 1)
)
alcatelIND1ChassisMIBCompliance.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "chasControlModuleGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlRedundantGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasChassisGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasControlReloadStatusGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chasGlobalControlGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "chassisNotificationGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasEntPhysFanGroup"),
        ("ALCATEL-IND1-CHASSIS-MIB", "alaChasHashControlGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1ChassisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-CHASSIS-MIB",
    **{"ChasEntPhysLed": ChasEntPhysLed,
       "ChasEntPhysPowerType": ChasEntPhysPowerType,
       "ChassisTrapsStrLevel": ChassisTrapsStrLevel,
       "ChassisTrapsStrAppID": ChassisTrapsStrAppID,
       "ChassisTrapsStrSnapID": ChassisTrapsStrSnapID,
       "ChassisTrapsStrfileLineNb": ChassisTrapsStrfileLineNb,
       "ChassisTrapsStrErrorNb": ChassisTrapsStrErrorNb,
       "ChassisTrapsStrdataInfo": ChassisTrapsStrdataInfo,
       "ChassisTrapsObjectType": ChassisTrapsObjectType,
       "ChassisTrapsObjectNumber": ChassisTrapsObjectNumber,
       "ChassisTrapsAlertNumber": ChassisTrapsAlertNumber,
       "alcatelIND1ChassisPhysMIBObjects": alcatelIND1ChassisPhysMIBObjects,
       "chasEntPhysicalTable": chasEntPhysicalTable,
       "chasEntPhysicalEntry": chasEntPhysicalEntry,
       "chasEntPhysAdminStatus": chasEntPhysAdminStatus,
       "chasEntPhysOperStatus": chasEntPhysOperStatus,
       "chasEntPhysLedStatus": chasEntPhysLedStatus,
       "chasEntPhysPower": chasEntPhysPower,
       "chasEntPhysModuleType": chasEntPhysModuleType,
       "chasEntPhysMfgDate": chasEntPhysMfgDate,
       "chasEntPhysPartNumber": chasEntPhysPartNumber,
       "chasEntPhysLedStatusOk1": chasEntPhysLedStatusOk1,
       "chasEntPhysLedStatusOk2": chasEntPhysLedStatusOk2,
       "chasEntPhysLedStatusPrimaryCMM": chasEntPhysLedStatusPrimaryCMM,
       "chasEntPhysLedStatusSecondaryCMM": chasEntPhysLedStatusSecondaryCMM,
       "chasEntPhysLedStatusTemperature": chasEntPhysLedStatusTemperature,
       "chasEntPhysLedStatusFan": chasEntPhysLedStatusFan,
       "chasEntPhysLedStatusFan1": chasEntPhysLedStatusFan1,
       "chasEntPhysLedStatusFan2": chasEntPhysLedStatusFan2,
       "chasEntPhysLedStatusFan3": chasEntPhysLedStatusFan3,
       "chasEntPhysLedStatusBackupPS": chasEntPhysLedStatusBackupPS,
       "chasEntPhysLedStatusInternalPS": chasEntPhysLedStatusInternalPS,
       "chasEntPhysLedStatusControl": chasEntPhysLedStatusControl,
       "chasEntPhysLedStatusFabric": chasEntPhysLedStatusFabric,
       "chasEntPhysLedStatusPSU": chasEntPhysLedStatusPSU,
       "chasEntPhysAsicRev": chasEntPhysAsicRev,
       "chasEntPhysCpldRev": chasEntPhysCpldRev,
       "chasEntPhysDefaultMinibootRev": chasEntPhysDefaultMinibootRev,
       "chasEntPhysBackUpMinibootRev": chasEntPhysBackUpMinibootRev,
       "chasEntPhysBootromRev": chasEntPhysBootromRev,
       "chasEntPhysNiNum": chasEntPhysNiNum,
       "chasEntPhysGbicNum": chasEntPhysGbicNum,
       "chasEntPhysWaveLen": chasEntPhysWaveLen,
       "chasEntPhysUbootRev": chasEntPhysUbootRev,
       "chasEntPhysUbootMinibootRev": chasEntPhysUbootMinibootRev,
       "chasEntPhysMacAddress": chasEntPhysMacAddress,
       "chasEntPhysPoeSwVersion": chasEntPhysPoeSwVersion,
       "chasEntPhysC20LFailCont": chasEntPhysC20LFailCont,
       "chasEntPhysCpuModel": chasEntPhysCpuModel,
       "chasEntPhysPowerType": chasEntPhysPowerType,
       "chasEntPhysPowerControlChecksum": chasEntPhysPowerControlChecksum,
       "alcatelIND1ChassisPhysMIBConformance": alcatelIND1ChassisPhysMIBConformance,
       "alcatelIND1ChassisPhysMIBGroups": alcatelIND1ChassisPhysMIBGroups,
       "chasEntPhysicalGroup": chasEntPhysicalGroup,
       "chassisPhysNotificationGroup": chassisPhysNotificationGroup,
       "alcatelIND1ChassisPhysMIBCompliances": alcatelIND1ChassisPhysMIBCompliances,
       "alcatelIND1ChassisPhysMIBCompliance": alcatelIND1ChassisPhysMIBCompliance,
       "alcatelIND1ChassisMIB": alcatelIND1ChassisMIB,
       "alcatelIND1ChassisMIBObjects": alcatelIND1ChassisMIBObjects,
       "chasControlModuleTable": chasControlModuleTable,
       "chasControlModuleEntry": chasControlModuleEntry,
       "chasControlRunningVersion": chasControlRunningVersion,
       "chasControlActivateTimeout": chasControlActivateTimeout,
       "chasControlVersionMngt": chasControlVersionMngt,
       "chasControlDelayedActivateTimer": chasControlDelayedActivateTimer,
       "chasControlCertifyStatus": chasControlCertifyStatus,
       "chasControlSynchronizationStatus": chasControlSynchronizationStatus,
       "chasControlAcrossCmmWorkingSynchroStatus": chasControlAcrossCmmWorkingSynchroStatus,
       "chasControlAcrossCmmCertifiedSynchroStatus": chasControlAcrossCmmCertifiedSynchroStatus,
       "chasControlRedundantTable": chasControlRedundantTable,
       "chasControlRedundantEntry": chasControlRedundantEntry,
       "chasControlNumberOfTakeover": chasControlNumberOfTakeover,
       "chasControlDelayedRebootTimer": chasControlDelayedRebootTimer,
       "chasChassisTable": chasChassisTable,
       "chasChassisEntry": chasChassisEntry,
       "chasFreeSlots": chasFreeSlots,
       "chasPowerLeft": chasPowerLeft,
       "chasNumberOfResets": chasNumberOfResets,
       "chasHardwareBoardTemp": chasHardwareBoardTemp,
       "chasHardwareCpuTemp": chasHardwareCpuTemp,
       "chasTempRange": chasTempRange,
       "chasTempThreshold": chasTempThreshold,
       "chasDangerTempThreshold": chasDangerTempThreshold,
       "chasPrimaryPhysicalIndex": chasPrimaryPhysicalIndex,
       "chasSupervisionRfsLsTable": chasSupervisionRfsLsTable,
       "chasSupervisionRfsLsEntry": chasSupervisionRfsLsEntry,
       "chasSupervisionRfsLsFileIndex": chasSupervisionRfsLsFileIndex,
       "chasSupervisionRfsLsSlot": chasSupervisionRfsLsSlot,
       "chasSupervisionRfsLsDirName": chasSupervisionRfsLsDirName,
       "chasSupervisionRfsLsFileName": chasSupervisionRfsLsFileName,
       "chasSupervisionRfsLsFileType": chasSupervisionRfsLsFileType,
       "chasSupervisionRfsLsFileSize": chasSupervisionRfsLsFileSize,
       "chasSupervisionRfsLsFileAttr": chasSupervisionRfsLsFileAttr,
       "chasSupervisionRfsLsFileDateTime": chasSupervisionRfsLsFileDateTime,
       "alcatelIND1ChassisSupervisionRfsCommands": alcatelIND1ChassisSupervisionRfsCommands,
       "chasSupervisionRfsCommandsSlot": chasSupervisionRfsCommandsSlot,
       "chasSupervisionRfsCommandsCommand": chasSupervisionRfsCommandsCommand,
       "chasSupervisionRfsCommandsSrcFileName": chasSupervisionRfsCommandsSrcFileName,
       "chasSupervisionRfsCommandsDestFileName": chasSupervisionRfsCommandsDestFileName,
       "chasSupervisionRfsCommandsRlsDirName": chasSupervisionRfsCommandsRlsDirName,
       "chasSupervisionRfsCommandsRlsFileName": chasSupervisionRfsCommandsRlsFileName,
       "chasSupervisionRfsCommandsProcessingState": chasSupervisionRfsCommandsProcessingState,
       "chasSupervisionRfsCommandsStatusCode": chasSupervisionRfsCommandsStatusCode,
       "chasControlReloadStatusTable": chasControlReloadStatusTable,
       "chasControlReloadEntry": chasControlReloadEntry,
       "chasControlReloadIndex": chasControlReloadIndex,
       "chasControlReloadStatus": chasControlReloadStatus,
       "chasGlobalControl": chasGlobalControl,
       "chasGlobalControlDelayedResetAll": chasGlobalControlDelayedResetAll,
       "chasGlobalControlLongCommand": chasGlobalControlLongCommand,
       "chasGlobalControlLongCommandStatus": chasGlobalControlLongCommandStatus,
       "chasSupervisionRfsDfTable": chasSupervisionRfsDfTable,
       "chasSupervisionRfsDfEntry": chasSupervisionRfsDfEntry,
       "chasSupervisionRfsDfSlot": chasSupervisionRfsDfSlot,
       "chasSupervisionRfsDfFlashFree": chasSupervisionRfsDfFlashFree,
       "chasSupervisionRfsDfFlashSize": chasSupervisionRfsDfFlashSize,
       "chasSupervisionFlashMemTable": chasSupervisionFlashMemTable,
       "chasSupervisionFlashMemEntry": chasSupervisionFlashMemEntry,
       "chasSupervisionSlot": chasSupervisionSlot,
       "chasSupervisionFlashSize": chasSupervisionFlashSize,
       "chasSupervisionFlashFree": chasSupervisionFlashFree,
       "chasSupervisionFlashUsed": chasSupervisionFlashUsed,
       "chasSupervisionCmmCertifiedTable": chasSupervisionCmmCertifiedTable,
       "chasSupervisionCmmCertifiedEntry": chasSupervisionCmmCertifiedEntry,
       "chasSupervisionCmmNum": chasSupervisionCmmNum,
       "chasSupervisionCmmCertifiedStatus": chasSupervisionCmmCertifiedStatus,
       "alaChasEntPhysFanTable": alaChasEntPhysFanTable,
       "alaChasEntPhysFanEntry": alaChasEntPhysFanEntry,
       "alaChasEntPhysFanLocalIndex": alaChasEntPhysFanLocalIndex,
       "alaChasEntPhysFanStatus": alaChasEntPhysFanStatus,
       "alaChasHashMode": alaChasHashMode,
       "alaChasUdpTcpPortMode": alaChasUdpTcpPortMode,
       "alaChasNonUCHashControl": alaChasNonUCHashControl,
       "alcatelIND1ChassisMIBConformance": alcatelIND1ChassisMIBConformance,
       "alcatelIND1ChassisMIBGroups": alcatelIND1ChassisMIBGroups,
       "chasControlModuleGroup": chasControlModuleGroup,
       "chasControlRedundantGroup": chasControlRedundantGroup,
       "chasChassisGroup": chasChassisGroup,
       "chasControlReloadStatusGroup": chasControlReloadStatusGroup,
       "chasGlobalControlGroup": chasGlobalControlGroup,
       "chassisNotificationGroup": chassisNotificationGroup,
       "alaChasEntPhysFanGroup": alaChasEntPhysFanGroup,
       "alaChasHashControlGroup": alaChasHashControlGroup,
       "alcatelIND1ChassisMIBCompliances": alcatelIND1ChassisMIBCompliances,
       "alcatelIND1ChassisMIBCompliance": alcatelIND1ChassisMIBCompliance,
       "chassisTrapsDesc": chassisTrapsDesc,
       "chassisTrapsStr": chassisTrapsStr,
       "chassisTrapsAlert": chassisTrapsAlert,
       "chassisTrapsStateChange": chassisTrapsStateChange,
       "chassisTrapsObj": chassisTrapsObj,
       "chassisTrapsStrLevel": chassisTrapsStrLevel,
       "chassisTrapsStrAppID": chassisTrapsStrAppID,
       "chassisTrapsStrSnapID": chassisTrapsStrSnapID,
       "chassisTrapsStrfileName": chassisTrapsStrfileName,
       "chassisTrapsStrfileLineNb": chassisTrapsStrfileLineNb,
       "chassisTrapsStrErrorNb": chassisTrapsStrErrorNb,
       "chassisTrapsStrcomments": chassisTrapsStrcomments,
       "chassisTrapsStrdataInfo": chassisTrapsStrdataInfo,
       "chassisTrapsObjectType": chassisTrapsObjectType,
       "chassisTrapsObjectNumber": chassisTrapsObjectNumber,
       "chassisTrapsAlertNumber": chassisTrapsAlertNumber,
       "chassisTrapsAlertDescr": chassisTrapsAlertDescr,
       "physicalIndex": physicalIndex}
)
