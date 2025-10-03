# SNMP MIB module (CIENA-CES-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:30 2025
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

(TceHealthCategory,
 TceHealthStatus) = mibBuilder.importSymbols(
    "CIENA-CES-MODULE-MIB",
    "TceHealthCategory",
    "TceHealthStatus")

(cienaGlobalSeverity,) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cienaCesChassisMIB.setRevisions(
        ("2018-10-17 00:00",
         "2018-01-31 00:00",
         "2017-06-07 00:00",
         "2017-05-31 00:00",
         "2017-03-24 00:00",
         "2017-02-09 00:00",
         "2016-10-20 00:00",
         "2016-09-20 00:00",
         "2016-03-28 00:00",
         "2016-03-16 00:00",
         "2015-07-06 00:00",
         "2015-06-02 00:00",
         "2015-05-07 00:00",
         "2015-03-02 00:00",
         "2015-02-25 00:00",
         "2014-11-10 00:00",
         "2014-11-01 00:00",
         "2014-02-25 00:00",
         "2014-01-23 00:00",
         "2013-12-18 00:00",
         "2013-12-05 00:00",
         "2013-03-28 00:00",
         "2013-03-07 00:00",
         "2013-02-06 00:00",
         "2012-06-28 00:00",
         "2012-06-04 00:00",
         "2010-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesChassisMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBObjects = _CienaCesChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1)
)
_CienaCesChassisGlobal_ObjectIdentity = ObjectIdentity
cienaCesChassisGlobal = _CienaCesChassisGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1)
)
_CienaCesChassisMacAddress_Type = MacAddress
_CienaCesChassisMacAddress_Object = MibScalar
cienaCesChassisMacAddress = _CienaCesChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 1),
    _CienaCesChassisMacAddress_Type()
)
cienaCesChassisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMacAddress.setStatus("current")
_CienaCesChassisDeviceId_Type = DisplayString
_CienaCesChassisDeviceId_Object = MibScalar
cienaCesChassisDeviceId = _CienaCesChassisDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 2),
    _CienaCesChassisDeviceId_Type()
)
cienaCesChassisDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDeviceId.setStatus("current")
_CienaCesChassisPartNumber_Type = DisplayString
_CienaCesChassisPartNumber_Object = MibScalar
cienaCesChassisPartNumber = _CienaCesChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 3),
    _CienaCesChassisPartNumber_Type()
)
cienaCesChassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPartNumber.setStatus("current")
_CienaCesChassisSerialNumber_Type = DisplayString
_CienaCesChassisSerialNumber_Object = MibScalar
cienaCesChassisSerialNumber = _CienaCesChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 4),
    _CienaCesChassisSerialNumber_Type()
)
cienaCesChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSerialNumber.setStatus("current")
_CienaCesChassisMfgDate_Type = DateAndTime
_CienaCesChassisMfgDate_Object = MibScalar
cienaCesChassisMfgDate = _CienaCesChassisMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 5),
    _CienaCesChassisMfgDate_Type()
)
cienaCesChassisMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMfgDate.setStatus("current")
_CienaCesChassisParamVersion_Type = DisplayString
_CienaCesChassisParamVersion_Object = MibScalar
cienaCesChassisParamVersion = _CienaCesChassisParamVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 6),
    _CienaCesChassisParamVersion_Type()
)
cienaCesChassisParamVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisParamVersion.setStatus("current")
_CienaCesChassisSystemDateAndTime_Type = DisplayString
_CienaCesChassisSystemDateAndTime_Object = MibScalar
cienaCesChassisSystemDateAndTime = _CienaCesChassisSystemDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 7),
    _CienaCesChassisSystemDateAndTime_Type()
)
cienaCesChassisSystemDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSystemDateAndTime.setStatus("current")
_CienaCesChassisSystemUTCDateAndTime_Type = DisplayString
_CienaCesChassisSystemUTCDateAndTime_Object = MibScalar
cienaCesChassisSystemUTCDateAndTime = _CienaCesChassisSystemUTCDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 8),
    _CienaCesChassisSystemUTCDateAndTime_Type()
)
cienaCesChassisSystemUTCDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSystemUTCDateAndTime.setStatus("current")
_CienaCesChassisSystemTimeOffset_Type = Integer32
_CienaCesChassisSystemTimeOffset_Object = MibScalar
cienaCesChassisSystemTimeOffset = _CienaCesChassisSystemTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 9),
    _CienaCesChassisSystemTimeOffset_Type()
)
cienaCesChassisSystemTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSystemTimeOffset.setStatus("current")


class _CienaCesChassisRebootReasonErrorType_Type(Integer32):
    """Custom type cienaCesChassisRebootReasonErrorType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("user", 2),
          ("powerFailure", 3),
          ("upgrade", 4),
          ("resetButton", 5),
          ("coldFailover", 6),
          ("faultManager", 7),
          ("communicationFailure", 8),
          ("autoRevert", 9),
          ("unprotectedFailure", 10),
          ("bootFailure", 11),
          ("softwareRevert", 12),
          ("snmp", 13),
          ("appLoad", 14),
          ("errorHandler", 15),
          ("watchdog", 16))
    )


_CienaCesChassisRebootReasonErrorType_Type.__name__ = "Integer32"
_CienaCesChassisRebootReasonErrorType_Object = MibScalar
cienaCesChassisRebootReasonErrorType = _CienaCesChassisRebootReasonErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 10),
    _CienaCesChassisRebootReasonErrorType_Type()
)
cienaCesChassisRebootReasonErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisRebootReasonErrorType.setStatus("current")
_CienaCesChassisSystemId_Type = DisplayString
_CienaCesChassisSystemId_Object = MibScalar
cienaCesChassisSystemId = _CienaCesChassisSystemId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 11),
    _CienaCesChassisSystemId_Type()
)
cienaCesChassisSystemId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisSystemId.setStatus("current")


class _CienaCesChassisAlarmCutoffOrigin_Type(Integer32):
    """Custom type cienaCesChassisAlarmCutoffOrigin based on Integer32"""
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
        *(("cli", 1),
          ("snmp", 2),
          ("primaryCm", 3),
          ("secondaryCm", 4))
    )


_CienaCesChassisAlarmCutoffOrigin_Type.__name__ = "Integer32"
_CienaCesChassisAlarmCutoffOrigin_Object = MibScalar
cienaCesChassisAlarmCutoffOrigin = _CienaCesChassisAlarmCutoffOrigin_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 12),
    _CienaCesChassisAlarmCutoffOrigin_Type()
)
cienaCesChassisAlarmCutoffOrigin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisAlarmCutoffOrigin.setStatus("current")


class _CienaCesChassisRestart_Type(TruthValue):
    """Custom type cienaCesChassisRestart based on TruthValue"""
    defaultValue = 2


_CienaCesChassisRestart_Type.__name__ = "TruthValue"
_CienaCesChassisRestart_Object = MibScalar
cienaCesChassisRestart = _CienaCesChassisRestart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 13),
    _CienaCesChassisRestart_Type()
)
cienaCesChassisRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCesChassisRestart.setStatus("current")
_CienaCesChassisMefSourceMacAddress_Type = MacAddress
_CienaCesChassisMefSourceMacAddress_Object = MibScalar
cienaCesChassisMefSourceMacAddress = _CienaCesChassisMefSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 1, 14),
    _CienaCesChassisMefSourceMacAddress_Type()
)
cienaCesChassisMefSourceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMefSourceMacAddress.setStatus("current")
_CienaCesChassisObjects_ObjectIdentity = ObjectIdentity
cienaCesChassisObjects = _CienaCesChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2)
)
_CienaCesChassis_ObjectIdentity = ObjectIdentity
cienaCesChassis = _CienaCesChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1)
)
_CienaCesChassisPowerModule_ObjectIdentity = ObjectIdentity
cienaCesChassisPowerModule = _CienaCesChassisPowerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1)
)
_CienaCesChassisPowerTable_Object = MibTable
cienaCesChassisPowerTable = _CienaCesChassisPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerTable.setStatus("current")
_CienaCesChassisPowerEntry_Object = MibTableRow
cienaCesChassisPowerEntry = _CienaCesChassisPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1)
)
cienaCesChassisPowerEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyIndx"),
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerEntry.setStatus("current")


class _CienaCesChassisPowerSupplyIndx_Type(Integer32):
    """Custom type cienaCesChassisPowerSupplyIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CienaCesChassisPowerSupplyIndx_Type.__name__ = "Integer32"
_CienaCesChassisPowerSupplyIndx_Object = MibTableColumn
cienaCesChassisPowerSupplyIndx = _CienaCesChassisPowerSupplyIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 1),
    _CienaCesChassisPowerSupplyIndx_Type()
)
cienaCesChassisPowerSupplyIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyIndx.setStatus("current")


class _CienaCesChassisPowerSupplyState_Type(Integer32):
    """Custom type cienaCesChassisPowerSupplyState based on Integer32"""
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
        *(("online", 1),
          ("faulted", 2),
          ("offline", 3),
          ("uninstalled", 4))
    )


_CienaCesChassisPowerSupplyState_Type.__name__ = "Integer32"
_CienaCesChassisPowerSupplyState_Object = MibTableColumn
cienaCesChassisPowerSupplyState = _CienaCesChassisPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 2),
    _CienaCesChassisPowerSupplyState_Type()
)
cienaCesChassisPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyState.setStatus("current")


class _CienaCesChassisPowerSupplyType_Type(Integer32):
    """Custom type cienaCesChassisPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("unequipped", 3),
          ("unknown", 99))
    )


_CienaCesChassisPowerSupplyType_Type.__name__ = "Integer32"
_CienaCesChassisPowerSupplyType_Object = MibTableColumn
cienaCesChassisPowerSupplyType = _CienaCesChassisPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 3),
    _CienaCesChassisPowerSupplyType_Type()
)
cienaCesChassisPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyType.setStatus("current")
_CienaCesChassisPowerSupplyManufacturer_Type = DisplayString
_CienaCesChassisPowerSupplyManufacturer_Object = MibTableColumn
cienaCesChassisPowerSupplyManufacturer = _CienaCesChassisPowerSupplyManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 4),
    _CienaCesChassisPowerSupplyManufacturer_Type()
)
cienaCesChassisPowerSupplyManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyManufacturer.setStatus("current")
_CienaCesChassisPowerSupplySerialNumber_Type = DisplayString
_CienaCesChassisPowerSupplySerialNumber_Object = MibTableColumn
cienaCesChassisPowerSupplySerialNumber = _CienaCesChassisPowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 5),
    _CienaCesChassisPowerSupplySerialNumber_Type()
)
cienaCesChassisPowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplySerialNumber.setStatus("current")
_CienaCesChassisPowerSupplyPartNum_Type = DisplayString
_CienaCesChassisPowerSupplyPartNum_Object = MibTableColumn
cienaCesChassisPowerSupplyPartNum = _CienaCesChassisPowerSupplyPartNum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 6),
    _CienaCesChassisPowerSupplyPartNum_Type()
)
cienaCesChassisPowerSupplyPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyPartNum.setStatus("current")


class _CienaCesChassisPowerSupplyNotifIndx_Type(Integer32):
    """Custom type cienaCesChassisPowerSupplyNotifIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCesChassisPowerSupplyNotifIndx_Type.__name__ = "Integer32"
_CienaCesChassisPowerSupplyNotifIndx_Object = MibTableColumn
cienaCesChassisPowerSupplyNotifIndx = _CienaCesChassisPowerSupplyNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 7),
    _CienaCesChassisPowerSupplyNotifIndx_Type()
)
cienaCesChassisPowerSupplyNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyNotifIndx.setStatus("current")
_CienaCesChassisPowerSupplyFRU_Type = TruthValue
_CienaCesChassisPowerSupplyFRU_Object = MibTableColumn
cienaCesChassisPowerSupplyFRU = _CienaCesChassisPowerSupplyFRU_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 8),
    _CienaCesChassisPowerSupplyFRU_Type()
)
cienaCesChassisPowerSupplyFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyFRU.setStatus("current")
_CienaCesChassisPowerSupplySlotName_Type = DisplayString
_CienaCesChassisPowerSupplySlotName_Object = MibTableColumn
cienaCesChassisPowerSupplySlotName = _CienaCesChassisPowerSupplySlotName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 9),
    _CienaCesChassisPowerSupplySlotName_Type()
)
cienaCesChassisPowerSupplySlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplySlotName.setStatus("current")
_CienaCesChassisPowerSupplyRevInfo_Type = DisplayString
_CienaCesChassisPowerSupplyRevInfo_Object = MibTableColumn
cienaCesChassisPowerSupplyRevInfo = _CienaCesChassisPowerSupplyRevInfo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 10),
    _CienaCesChassisPowerSupplyRevInfo_Type()
)
cienaCesChassisPowerSupplyRevInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyRevInfo.setStatus("current")


class _CienaCesChassisPowerSupplyChassisIndx_Type(Unsigned32):
    """Custom type cienaCesChassisPowerSupplyChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChassisPowerSupplyChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisPowerSupplyChassisIndx_Object = MibTableColumn
cienaCesChassisPowerSupplyChassisIndx = _CienaCesChassisPowerSupplyChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 11),
    _CienaCesChassisPowerSupplyChassisIndx_Type()
)
cienaCesChassisPowerSupplyChassisIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyChassisIndx.setStatus("current")


class _CienaCesChassisPowerSupplyShelfIndx_Type(Unsigned32):
    """Custom type cienaCesChassisPowerSupplyShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChassisPowerSupplyShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisPowerSupplyShelfIndx_Object = MibTableColumn
cienaCesChassisPowerSupplyShelfIndx = _CienaCesChassisPowerSupplyShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 12),
    _CienaCesChassisPowerSupplyShelfIndx_Type()
)
cienaCesChassisPowerSupplyShelfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyShelfIndx.setStatus("current")


class _CienaCesChassisPowerSupplySlotIndx_Type(Unsigned32):
    """Custom type cienaCesChassisPowerSupplySlotIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesChassisPowerSupplySlotIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisPowerSupplySlotIndx_Object = MibTableColumn
cienaCesChassisPowerSupplySlotIndx = _CienaCesChassisPowerSupplySlotIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 1, 1, 1, 13),
    _CienaCesChassisPowerSupplySlotIndx_Type()
)
cienaCesChassisPowerSupplySlotIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplySlotIndx.setStatus("current")
_CienaCesChassisFanModule_ObjectIdentity = ObjectIdentity
cienaCesChassisFanModule = _CienaCesChassisFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2)
)
_CienaCesChassisFanTable_Object = MibTable
cienaCesChassisFanTable = _CienaCesChassisFanTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTable.setStatus("current")
_CienaCesChassisFanEntry_Object = MibTableRow
cienaCesChassisFanEntry = _CienaCesChassisFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1)
)
cienaCesChassisFanEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayIndx"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanIndx"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanEntry.setStatus("current")


class _CienaCesChassisFanTrayIndx_Type(Integer32):
    """Custom type cienaCesChassisFanTrayIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CienaCesChassisFanTrayIndx_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayIndx_Object = MibTableColumn
cienaCesChassisFanTrayIndx = _CienaCesChassisFanTrayIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 1),
    _CienaCesChassisFanTrayIndx_Type()
)
cienaCesChassisFanTrayIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayIndx.setStatus("current")


class _CienaCesChassisFanIndx_Type(Integer32):
    """Custom type cienaCesChassisFanIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanIndx_Type.__name__ = "Integer32"
_CienaCesChassisFanIndx_Object = MibTableColumn
cienaCesChassisFanIndx = _CienaCesChassisFanIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 2),
    _CienaCesChassisFanIndx_Type()
)
cienaCesChassisFanIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanIndx.setStatus("current")


class _CienaCesChassisFanStatus_Type(Integer32):
    """Custom type cienaCesChassisFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("pending", 2),
          ("rpm-warning", 3),
          ("uninstalled", 4),
          ("unknown", 99))
    )


_CienaCesChassisFanStatus_Type.__name__ = "Integer32"
_CienaCesChassisFanStatus_Object = MibTableColumn
cienaCesChassisFanStatus = _CienaCesChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 3),
    _CienaCesChassisFanStatus_Type()
)
cienaCesChassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanStatus.setStatus("current")
_CienaCesChassisFanAvgSpeed_Type = Integer32
_CienaCesChassisFanAvgSpeed_Object = MibTableColumn
cienaCesChassisFanAvgSpeed = _CienaCesChassisFanAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 4),
    _CienaCesChassisFanAvgSpeed_Type()
)
cienaCesChassisFanAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanAvgSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanAvgSpeed.setUnits("rpm")
_CienaCesChassisFanCurrentSpeed_Type = Integer32
_CienaCesChassisFanCurrentSpeed_Object = MibTableColumn
cienaCesChassisFanCurrentSpeed = _CienaCesChassisFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 5),
    _CienaCesChassisFanCurrentSpeed_Type()
)
cienaCesChassisFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanCurrentSpeed.setUnits("rpm")
_CienaCesChassisFanMinSpeed_Type = Integer32
_CienaCesChassisFanMinSpeed_Object = MibTableColumn
cienaCesChassisFanMinSpeed = _CienaCesChassisFanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 6),
    _CienaCesChassisFanMinSpeed_Type()
)
cienaCesChassisFanMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanMinSpeed.setUnits("rpm")


class _CienaCesChassisFanTrayNotifIndex_Type(Integer32):
    """Custom type cienaCesChassisFanTrayNotifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CienaCesChassisFanTrayNotifIndex_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayNotifIndex_Object = MibTableColumn
cienaCesChassisFanTrayNotifIndex = _CienaCesChassisFanTrayNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 7),
    _CienaCesChassisFanTrayNotifIndex_Type()
)
cienaCesChassisFanTrayNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayNotifIndex.setStatus("current")


class _CienaCesChassisFanNotifIndex_Type(Integer32):
    """Custom type cienaCesChassisFanNotifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanNotifIndex_Type.__name__ = "Integer32"
_CienaCesChassisFanNotifIndex_Object = MibTableColumn
cienaCesChassisFanNotifIndex = _CienaCesChassisFanNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 8),
    _CienaCesChassisFanNotifIndex_Type()
)
cienaCesChassisFanNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisFanNotifIndex.setStatus("current")
_CienaCesChassisFanName_Type = DisplayString
_CienaCesChassisFanName_Object = MibTableColumn
cienaCesChassisFanName = _CienaCesChassisFanName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 9),
    _CienaCesChassisFanName_Type()
)
cienaCesChassisFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanName.setStatus("current")


class _CienaCesChassisFanChassisIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChassisFanChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanChassisIndx_Object = MibTableColumn
cienaCesChassisFanChassisIndx = _CienaCesChassisFanChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 10),
    _CienaCesChassisFanChassisIndx_Type()
)
cienaCesChassisFanChassisIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanChassisIndx.setStatus("current")


class _CienaCesChassisFanShelfIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChassisFanShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanShelfIndx_Object = MibTableColumn
cienaCesChassisFanShelfIndx = _CienaCesChassisFanShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 1, 1, 11),
    _CienaCesChassisFanShelfIndx_Type()
)
cienaCesChassisFanShelfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanShelfIndx.setStatus("current")
_CienaCesChassisFanTrayTable_Object = MibTable
cienaCesChassisFanTrayTable = _CienaCesChassisFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayTable.setStatus("current")
_CienaCesChassisFanTrayEntry_Object = MibTableRow
cienaCesChassisFanTrayEntry = _CienaCesChassisFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1)
)
cienaCesChassisFanTrayEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayIndx"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayEntry.setStatus("current")


class _CienaCesChassisFanTrayStatus_Type(Integer32):
    """Custom type cienaCesChassisFanTrayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("pending", 2),
          ("rpm-warning", 3),
          ("uninstalled", 4),
          ("unknown", 99))
    )


_CienaCesChassisFanTrayStatus_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayStatus_Object = MibTableColumn
cienaCesChassisFanTrayStatus = _CienaCesChassisFanTrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 1),
    _CienaCesChassisFanTrayStatus_Type()
)
cienaCesChassisFanTrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayStatus.setStatus("current")


class _CienaCesChassisFanTrayType_Type(Integer32):
    """Custom type cienaCesChassisFanTrayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("hotSwappable", 2),
          ("unequipped", 3))
    )


_CienaCesChassisFanTrayType_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayType_Object = MibTableColumn
cienaCesChassisFanTrayType = _CienaCesChassisFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 2),
    _CienaCesChassisFanTrayType_Type()
)
cienaCesChassisFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayType.setStatus("current")


class _CienaCesChassisFanTrayMode_Type(Integer32):
    """Custom type cienaCesChassisFanTrayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("full", 2),
          ("auto", 3))
    )


_CienaCesChassisFanTrayMode_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayMode_Object = MibTableColumn
cienaCesChassisFanTrayMode = _CienaCesChassisFanTrayMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 3),
    _CienaCesChassisFanTrayMode_Type()
)
cienaCesChassisFanTrayMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayMode.setStatus("current")
_CienaCesChassisFanTrayNumFans_Type = Integer32
_CienaCesChassisFanTrayNumFans_Object = MibTableColumn
cienaCesChassisFanTrayNumFans = _CienaCesChassisFanTrayNumFans_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 4),
    _CienaCesChassisFanTrayNumFans_Type()
)
cienaCesChassisFanTrayNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayNumFans.setStatus("current")
_CienaCesChassisFanTrayName_Type = DisplayString
_CienaCesChassisFanTrayName_Object = MibTableColumn
cienaCesChassisFanTrayName = _CienaCesChassisFanTrayName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 5),
    _CienaCesChassisFanTrayName_Type()
)
cienaCesChassisFanTrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayName.setStatus("current")


class _CienaCesChassisFanTrayChassisIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanTrayChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChassisFanTrayChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanTrayChassisIndx_Object = MibTableColumn
cienaCesChassisFanTrayChassisIndx = _CienaCesChassisFanTrayChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 6),
    _CienaCesChassisFanTrayChassisIndx_Type()
)
cienaCesChassisFanTrayChassisIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayChassisIndx.setStatus("current")


class _CienaCesChassisFanTrayShelfIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanTrayShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChassisFanTrayShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanTrayShelfIndx_Object = MibTableColumn
cienaCesChassisFanTrayShelfIndx = _CienaCesChassisFanTrayShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 7),
    _CienaCesChassisFanTrayShelfIndx_Type()
)
cienaCesChassisFanTrayShelfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayShelfIndx.setStatus("current")


class _CienaCesChassisFanTraySlotIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanTraySlotIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesChassisFanTraySlotIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanTraySlotIndx_Object = MibTableColumn
cienaCesChassisFanTraySlotIndx = _CienaCesChassisFanTraySlotIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 8),
    _CienaCesChassisFanTraySlotIndx_Type()
)
cienaCesChassisFanTraySlotIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySlotIndx.setStatus("current")
_CienaCesChassisFanTraySerialNumber_Type = DisplayString
_CienaCesChassisFanTraySerialNumber_Object = MibTableColumn
cienaCesChassisFanTraySerialNumber = _CienaCesChassisFanTraySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 2, 2, 1, 9),
    _CienaCesChassisFanTraySerialNumber_Type()
)
cienaCesChassisFanTraySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySerialNumber.setStatus("current")
_CienaCesChassisFanModuleTemp_ObjectIdentity = ObjectIdentity
cienaCesChassisFanModuleTemp = _CienaCesChassisFanModuleTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3)
)
_CienaCesChassisFanTempTable_Object = MibTable
cienaCesChassisFanTempTable = _CienaCesChassisFanTempTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTempTable.setStatus("current")
_CienaCesChassisFanTempEntry_Object = MibTableRow
cienaCesChassisFanTempEntry = _CienaCesChassisFanTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1)
)
cienaCesChassisFanTempEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempTrayIndx"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempId"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTempEntry.setStatus("current")


class _CienaCesChassisFanTempTrayIndx_Type(Integer32):
    """Custom type cienaCesChassisFanTempTrayIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanTempTrayIndx_Type.__name__ = "Integer32"
_CienaCesChassisFanTempTrayIndx_Object = MibTableColumn
cienaCesChassisFanTempTrayIndx = _CienaCesChassisFanTempTrayIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 1),
    _CienaCesChassisFanTempTrayIndx_Type()
)
cienaCesChassisFanTempTrayIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempTrayIndx.setStatus("current")


class _CienaCesChassisFanTempId_Type(Integer32):
    """Custom type cienaCesChassisFanTempId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanTempId_Type.__name__ = "Integer32"
_CienaCesChassisFanTempId_Object = MibTableColumn
cienaCesChassisFanTempId = _CienaCesChassisFanTempId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 2),
    _CienaCesChassisFanTempId_Type()
)
cienaCesChassisFanTempId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempId.setStatus("current")
_CienaCesChassisFanTempDesc_Type = DisplayString
_CienaCesChassisFanTempDesc_Object = MibTableColumn
cienaCesChassisFanTempDesc = _CienaCesChassisFanTempDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 3),
    _CienaCesChassisFanTempDesc_Type()
)
cienaCesChassisFanTempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempDesc.setStatus("current")
_CienaCesChassisFanTemp_Type = Integer32
_CienaCesChassisFanTemp_Object = MibTableColumn
cienaCesChassisFanTemp = _CienaCesChassisFanTemp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 4),
    _CienaCesChassisFanTemp_Type()
)
cienaCesChassisFanTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTemp.setStatus("current")
_CienaCesChassisFanTempHigh_Type = Integer32
_CienaCesChassisFanTempHigh_Object = MibTableColumn
cienaCesChassisFanTempHigh = _CienaCesChassisFanTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 5),
    _CienaCesChassisFanTempHigh_Type()
)
cienaCesChassisFanTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHigh.setStatus("current")
_CienaCesChassisFanTempLow_Type = Integer32
_CienaCesChassisFanTempLow_Object = MibTableColumn
cienaCesChassisFanTempLow = _CienaCesChassisFanTempLow_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 6),
    _CienaCesChassisFanTempLow_Type()
)
cienaCesChassisFanTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempLow.setStatus("current")


class _CienaCesChassisFanTempLoThreshold_Type(Integer32):
    """Custom type cienaCesChassisFanTempLoThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CienaCesChassisFanTempLoThreshold_Type.__name__ = "Integer32"
_CienaCesChassisFanTempLoThreshold_Object = MibTableColumn
cienaCesChassisFanTempLoThreshold = _CienaCesChassisFanTempLoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 7),
    _CienaCesChassisFanTempLoThreshold_Type()
)
cienaCesChassisFanTempLoThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempLoThreshold.setStatus("current")


class _CienaCesChassisFanTempHiThreshold_Type(Integer32):
    """Custom type cienaCesChassisFanTempHiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CienaCesChassisFanTempHiThreshold_Type.__name__ = "Integer32"
_CienaCesChassisFanTempHiThreshold_Object = MibTableColumn
cienaCesChassisFanTempHiThreshold = _CienaCesChassisFanTempHiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 8),
    _CienaCesChassisFanTempHiThreshold_Type()
)
cienaCesChassisFanTempHiThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHiThreshold.setStatus("current")


class _CienaCesChassisFanTempTrayNotifIndx_Type(Integer32):
    """Custom type cienaCesChassisFanTempTrayNotifIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanTempTrayNotifIndx_Type.__name__ = "Integer32"
_CienaCesChassisFanTempTrayNotifIndx_Object = MibTableColumn
cienaCesChassisFanTempTrayNotifIndx = _CienaCesChassisFanTempTrayNotifIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 9),
    _CienaCesChassisFanTempTrayNotifIndx_Type()
)
cienaCesChassisFanTempTrayNotifIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempTrayNotifIndx.setStatus("current")


class _CienaCesChassisFanTempNotifId_Type(Integer32):
    """Custom type cienaCesChassisFanTempNotifId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesChassisFanTempNotifId_Type.__name__ = "Integer32"
_CienaCesChassisFanTempNotifId_Object = MibTableColumn
cienaCesChassisFanTempNotifId = _CienaCesChassisFanTempNotifId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 10),
    _CienaCesChassisFanTempNotifId_Type()
)
cienaCesChassisFanTempNotifId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempNotifId.setStatus("current")
_CienaCesChassisFanTempName_Type = DisplayString
_CienaCesChassisFanTempName_Object = MibTableColumn
cienaCesChassisFanTempName = _CienaCesChassisFanTempName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 11),
    _CienaCesChassisFanTempName_Type()
)
cienaCesChassisFanTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempName.setStatus("current")


class _CienaCesChassisFanTempChassisIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanTempChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChassisFanTempChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanTempChassisIndx_Object = MibTableColumn
cienaCesChassisFanTempChassisIndx = _CienaCesChassisFanTempChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 12),
    _CienaCesChassisFanTempChassisIndx_Type()
)
cienaCesChassisFanTempChassisIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempChassisIndx.setStatus("current")


class _CienaCesChassisFanTempShelfIndx_Type(Unsigned32):
    """Custom type cienaCesChassisFanTempShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChassisFanTempShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisFanTempShelfIndx_Object = MibTableColumn
cienaCesChassisFanTempShelfIndx = _CienaCesChassisFanTempShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 3, 2, 1, 13),
    _CienaCesChassisFanTempShelfIndx_Type()
)
cienaCesChassisFanTempShelfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempShelfIndx.setStatus("current")
_CienaCesChassisHealth_ObjectIdentity = ObjectIdentity
cienaCesChassisHealth = _CienaCesChassisHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4)
)
_CienaCesChassisHealthCategory_Type = TceHealthCategory
_CienaCesChassisHealthCategory_Object = MibScalar
cienaCesChassisHealthCategory = _CienaCesChassisHealthCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 1),
    _CienaCesChassisHealthCategory_Type()
)
cienaCesChassisHealthCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisHealthCategory.setStatus("current")
_CienaCesChassisHealthSubCategory_Type = Unsigned32
_CienaCesChassisHealthSubCategory_Object = MibScalar
cienaCesChassisHealthSubCategory = _CienaCesChassisHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 2),
    _CienaCesChassisHealthSubCategory_Type()
)
cienaCesChassisHealthSubCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisHealthSubCategory.setStatus("current")
_CienaCesChassisHealthStatus_Type = TceHealthStatus
_CienaCesChassisHealthStatus_Object = MibScalar
cienaCesChassisHealthStatus = _CienaCesChassisHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 3),
    _CienaCesChassisHealthStatus_Type()
)
cienaCesChassisHealthStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatus.setStatus("current")
_CienaCesChassisHealthStatusLast_Type = TceHealthStatus
_CienaCesChassisHealthStatusLast_Object = MibScalar
cienaCesChassisHealthStatusLast = _CienaCesChassisHealthStatusLast_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 4),
    _CienaCesChassisHealthStatusLast_Type()
)
cienaCesChassisHealthStatusLast.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusLast.setStatus("current")
_CienaCesChassisCPUHealthTable_Object = MibTable
cienaCesChassisCPUHealthTable = _CienaCesChassisCPUHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthTable.setStatus("current")
_CienaCesChassisCPUHealthEntry_Object = MibTableRow
cienaCesChassisCPUHealthEntry = _CienaCesChassisCPUHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1)
)
cienaCesChassisCPUHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisCPUHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisCPUHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthEntry.setStatus("current")


class _CienaCesChassisCPUHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisCPUHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cpu-Usage", 1))
    )


_CienaCesChassisCPUHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisCPUHealthSubCategory_Object = MibTableColumn
cienaCesChassisCPUHealthSubCategory = _CienaCesChassisCPUHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 1),
    _CienaCesChassisCPUHealthSubCategory_Type()
)
cienaCesChassisCPUHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthSubCategory.setStatus("current")
_CienaCesChassisCPUHealthOriginIndex_Type = Unsigned32
_CienaCesChassisCPUHealthOriginIndex_Object = MibTableColumn
cienaCesChassisCPUHealthOriginIndex = _CienaCesChassisCPUHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 2),
    _CienaCesChassisCPUHealthOriginIndex_Type()
)
cienaCesChassisCPUHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthOriginIndex.setStatus("current")
_CienaCesChassisCPUHealthState_Type = TceHealthStatus
_CienaCesChassisCPUHealthState_Object = MibTableColumn
cienaCesChassisCPUHealthState = _CienaCesChassisCPUHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 3),
    _CienaCesChassisCPUHealthState_Type()
)
cienaCesChassisCPUHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthState.setStatus("current")
_CienaCesChassisCPUHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisCPUHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisCPUHealthCurrMeasurement = _CienaCesChassisCPUHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 4),
    _CienaCesChassisCPUHealthCurrMeasurement_Type()
)
cienaCesChassisCPUHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthCurrMeasurement.setUnits("percent")
_CienaCesChassisCPUHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisCPUHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisCPUHealthMaxMeasurement = _CienaCesChassisCPUHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 5),
    _CienaCesChassisCPUHealthMaxMeasurement_Type()
)
cienaCesChassisCPUHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthMaxMeasurement.setUnits("percent")
_CienaCesChassisCPUHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisCPUHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisCPUHealthMaxThreshold = _CienaCesChassisCPUHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 5, 1, 6),
    _CienaCesChassisCPUHealthMaxThreshold_Type()
)
cienaCesChassisCPUHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisCPUHealthMaxThreshold.setUnits("percent")
_CienaCesChassisDatapathHealthTable_Object = MibTable
cienaCesChassisDatapathHealthTable = _CienaCesChassisDatapathHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    cienaCesChassisDatapathHealthTable.setStatus("current")
_CienaCesChassisDatapathHealthEntry_Object = MibTableRow
cienaCesChassisDatapathHealthEntry = _CienaCesChassisDatapathHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 6, 1)
)
cienaCesChassisDatapathHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisDatapathHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisDatapathHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisDatapathHealthEntry.setStatus("current")


class _CienaCesChassisDatapathHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisDatapathHealthSubCategory based on Integer32"""
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
        *(("none", 0),
          ("status", 1),
          ("dataPlane", 2),
          ("system", 3),
          ("controlPlane", 4))
    )


_CienaCesChassisDatapathHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisDatapathHealthSubCategory_Object = MibTableColumn
cienaCesChassisDatapathHealthSubCategory = _CienaCesChassisDatapathHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 6, 1, 1),
    _CienaCesChassisDatapathHealthSubCategory_Type()
)
cienaCesChassisDatapathHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisDatapathHealthSubCategory.setStatus("current")
_CienaCesChassisDatapathHealthOriginIndex_Type = Unsigned32
_CienaCesChassisDatapathHealthOriginIndex_Object = MibTableColumn
cienaCesChassisDatapathHealthOriginIndex = _CienaCesChassisDatapathHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 6, 1, 2),
    _CienaCesChassisDatapathHealthOriginIndex_Type()
)
cienaCesChassisDatapathHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisDatapathHealthOriginIndex.setStatus("current")
_CienaCesChassisDatapathHealthState_Type = TceHealthStatus
_CienaCesChassisDatapathHealthState_Object = MibTableColumn
cienaCesChassisDatapathHealthState = _CienaCesChassisDatapathHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 6, 1, 3),
    _CienaCesChassisDatapathHealthState_Type()
)
cienaCesChassisDatapathHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDatapathHealthState.setStatus("current")
_CienaCesChassisControlPlaneHealthTable_Object = MibTable
cienaCesChassisControlPlaneHealthTable = _CienaCesChassisControlPlaneHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7)
)
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthTable.setStatus("current")
_CienaCesChassisControlPlaneHealthEntry_Object = MibTableRow
cienaCesChassisControlPlaneHealthEntry = _CienaCesChassisControlPlaneHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1)
)
cienaCesChassisControlPlaneHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisControlPlaneHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisControlPlaneHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthEntry.setStatus("current")


class _CienaCesChassisControlPlaneHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisControlPlaneHealthSubCategory based on Integer32"""
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
          ("droppedPackets", 1),
          ("cRCErrors", 2),
          ("errorPackets", 3))
    )


_CienaCesChassisControlPlaneHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisControlPlaneHealthSubCategory_Object = MibTableColumn
cienaCesChassisControlPlaneHealthSubCategory = _CienaCesChassisControlPlaneHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 1),
    _CienaCesChassisControlPlaneHealthSubCategory_Type()
)
cienaCesChassisControlPlaneHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthSubCategory.setStatus("current")
_CienaCesChassisControlPlaneHealthOriginIndex_Type = Unsigned32
_CienaCesChassisControlPlaneHealthOriginIndex_Object = MibTableColumn
cienaCesChassisControlPlaneHealthOriginIndex = _CienaCesChassisControlPlaneHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 2),
    _CienaCesChassisControlPlaneHealthOriginIndex_Type()
)
cienaCesChassisControlPlaneHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthOriginIndex.setStatus("current")
_CienaCesChassisControlPlaneHealthState_Type = TceHealthStatus
_CienaCesChassisControlPlaneHealthState_Object = MibTableColumn
cienaCesChassisControlPlaneHealthState = _CienaCesChassisControlPlaneHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 3),
    _CienaCesChassisControlPlaneHealthState_Type()
)
cienaCesChassisControlPlaneHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthState.setStatus("current")
_CienaCesChassisControlPlaneHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisControlPlaneHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisControlPlaneHealthCurrMeasurement = _CienaCesChassisControlPlaneHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 4),
    _CienaCesChassisControlPlaneHealthCurrMeasurement_Type()
)
cienaCesChassisControlPlaneHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthCurrMeasurement.setUnits("percent")
_CienaCesChassisControlPlaneHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisControlPlaneHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisControlPlaneHealthMaxMeasurement = _CienaCesChassisControlPlaneHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 5),
    _CienaCesChassisControlPlaneHealthMaxMeasurement_Type()
)
cienaCesChassisControlPlaneHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthMaxMeasurement.setUnits("percent")
_CienaCesChassisControlPlaneHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisControlPlaneHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisControlPlaneHealthMaxThreshold = _CienaCesChassisControlPlaneHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 7, 1, 6),
    _CienaCesChassisControlPlaneHealthMaxThreshold_Type()
)
cienaCesChassisControlPlaneHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisControlPlaneHealthMaxThreshold.setUnits("percent")
_CienaCesChassisFabricHealthTable_Object = MibTable
cienaCesChassisFabricHealthTable = _CienaCesChassisFabricHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 8)
)
if mibBuilder.loadTexts:
    cienaCesChassisFabricHealthTable.setStatus("current")
_CienaCesChassisFabricHealthEntry_Object = MibTableRow
cienaCesChassisFabricHealthEntry = _CienaCesChassisFabricHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 8, 1)
)
cienaCesChassisFabricHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFabricHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFabricHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFabricHealthEntry.setStatus("current")


class _CienaCesChassisFabricHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFabricHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisFabricHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFabricHealthSubCategory_Object = MibTableColumn
cienaCesChassisFabricHealthSubCategory = _CienaCesChassisFabricHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 8, 1, 1),
    _CienaCesChassisFabricHealthSubCategory_Type()
)
cienaCesChassisFabricHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFabricHealthSubCategory.setStatus("current")
_CienaCesChassisFabricHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFabricHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFabricHealthOriginIndex = _CienaCesChassisFabricHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 8, 1, 2),
    _CienaCesChassisFabricHealthOriginIndex_Type()
)
cienaCesChassisFabricHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFabricHealthOriginIndex.setStatus("current")
_CienaCesChassisFabricHealthState_Type = TceHealthStatus
_CienaCesChassisFabricHealthState_Object = MibTableColumn
cienaCesChassisFabricHealthState = _CienaCesChassisFabricHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 8, 1, 4),
    _CienaCesChassisFabricHealthState_Type()
)
cienaCesChassisFabricHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFabricHealthState.setStatus("current")
_CienaCesChassisSMHealthTable_Object = MibTable
cienaCesChassisSMHealthTable = _CienaCesChassisSMHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 9)
)
if mibBuilder.loadTexts:
    cienaCesChassisSMHealthTable.setStatus("current")
_CienaCesChassisSMHealthEntry_Object = MibTableRow
cienaCesChassisSMHealthEntry = _CienaCesChassisSMHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 9, 1)
)
cienaCesChassisSMHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisSMHealthEntry.setStatus("current")


class _CienaCesChassisSMHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisSMHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisSMHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisSMHealthSubCategory_Object = MibTableColumn
cienaCesChassisSMHealthSubCategory = _CienaCesChassisSMHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 9, 1, 1),
    _CienaCesChassisSMHealthSubCategory_Type()
)
cienaCesChassisSMHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMHealthSubCategory.setStatus("current")
_CienaCesChassisSMHealthOriginIndex_Type = Unsigned32
_CienaCesChassisSMHealthOriginIndex_Object = MibTableColumn
cienaCesChassisSMHealthOriginIndex = _CienaCesChassisSMHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 9, 1, 2),
    _CienaCesChassisSMHealthOriginIndex_Type()
)
cienaCesChassisSMHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMHealthOriginIndex.setStatus("current")
_CienaCesChassisSMHealthState_Type = TceHealthStatus
_CienaCesChassisSMHealthState_Object = MibTableColumn
cienaCesChassisSMHealthState = _CienaCesChassisSMHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 9, 1, 4),
    _CienaCesChassisSMHealthState_Type()
)
cienaCesChassisSMHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMHealthState.setStatus("current")
_CienaCesChassisSMTempHealthTable_Object = MibTable
cienaCesChassisSMTempHealthTable = _CienaCesChassisSMTempHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10)
)
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthTable.setStatus("current")
_CienaCesChassisSMTempHealthEntry_Object = MibTableRow
cienaCesChassisSMTempHealthEntry = _CienaCesChassisSMTempHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1)
)
cienaCesChassisSMTempHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMTempHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMTempHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthEntry.setStatus("current")


class _CienaCesChassisSMTempHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisSMTempHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("temperature", 1))
    )


_CienaCesChassisSMTempHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisSMTempHealthSubCategory_Object = MibTableColumn
cienaCesChassisSMTempHealthSubCategory = _CienaCesChassisSMTempHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 1),
    _CienaCesChassisSMTempHealthSubCategory_Type()
)
cienaCesChassisSMTempHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthSubCategory.setStatus("current")
_CienaCesChassisSMTempHealthOriginIndex_Type = Unsigned32
_CienaCesChassisSMTempHealthOriginIndex_Object = MibTableColumn
cienaCesChassisSMTempHealthOriginIndex = _CienaCesChassisSMTempHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 2),
    _CienaCesChassisSMTempHealthOriginIndex_Type()
)
cienaCesChassisSMTempHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthOriginIndex.setStatus("current")
_CienaCesChassisSMTempHealthState_Type = TceHealthStatus
_CienaCesChassisSMTempHealthState_Object = MibTableColumn
cienaCesChassisSMTempHealthState = _CienaCesChassisSMTempHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 3),
    _CienaCesChassisSMTempHealthState_Type()
)
cienaCesChassisSMTempHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthState.setStatus("current")
_CienaCesChassisSMTempHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisSMTempHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisSMTempHealthCurrMeasurement = _CienaCesChassisSMTempHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 4),
    _CienaCesChassisSMTempHealthCurrMeasurement_Type()
)
cienaCesChassisSMTempHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthCurrMeasurement.setUnits("deg C")
_CienaCesChassisSMTempHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisSMTempHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisSMTempHealthMinMeasurement = _CienaCesChassisSMTempHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 5),
    _CienaCesChassisSMTempHealthMinMeasurement_Type()
)
cienaCesChassisSMTempHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMinMeasurement.setUnits("deg C")
_CienaCesChassisSMTempHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisSMTempHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisSMTempHealthMaxMeasurement = _CienaCesChassisSMTempHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 6),
    _CienaCesChassisSMTempHealthMaxMeasurement_Type()
)
cienaCesChassisSMTempHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMaxMeasurement.setUnits("deg C")
_CienaCesChassisSMTempHealthMinThreshold_Type = Unsigned32
_CienaCesChassisSMTempHealthMinThreshold_Object = MibTableColumn
cienaCesChassisSMTempHealthMinThreshold = _CienaCesChassisSMTempHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 7),
    _CienaCesChassisSMTempHealthMinThreshold_Type()
)
cienaCesChassisSMTempHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMinThreshold.setUnits("deg C")
_CienaCesChassisSMTempHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisSMTempHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisSMTempHealthMaxThreshold = _CienaCesChassisSMTempHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 10, 1, 8),
    _CienaCesChassisSMTempHealthMaxThreshold_Type()
)
cienaCesChassisSMTempHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisSMTempHealthMaxThreshold.setUnits("deg C")
_CienaCesChassisSMSamplesHealthTable_Object = MibTable
cienaCesChassisSMSamplesHealthTable = _CienaCesChassisSMSamplesHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11)
)
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthTable.setStatus("current")
_CienaCesChassisSMSamplesHealthEntry_Object = MibTableRow
cienaCesChassisSMSamplesHealthEntry = _CienaCesChassisSMSamplesHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1)
)
cienaCesChassisSMSamplesHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMSamplesHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMSamplesHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthEntry.setStatus("current")


class _CienaCesChassisSMSamplesHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisSMSamplesHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid", 1))
    )


_CienaCesChassisSMSamplesHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisSMSamplesHealthSubCategory_Object = MibTableColumn
cienaCesChassisSMSamplesHealthSubCategory = _CienaCesChassisSMSamplesHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1, 1),
    _CienaCesChassisSMSamplesHealthSubCategory_Type()
)
cienaCesChassisSMSamplesHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthSubCategory.setStatus("current")
_CienaCesChassisSMSamplesHealthOriginIndex_Type = Unsigned32
_CienaCesChassisSMSamplesHealthOriginIndex_Object = MibTableColumn
cienaCesChassisSMSamplesHealthOriginIndex = _CienaCesChassisSMSamplesHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1, 2),
    _CienaCesChassisSMSamplesHealthOriginIndex_Type()
)
cienaCesChassisSMSamplesHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthOriginIndex.setStatus("current")
_CienaCesChassisSMSamplesHealthState_Type = TceHealthStatus
_CienaCesChassisSMSamplesHealthState_Object = MibTableColumn
cienaCesChassisSMSamplesHealthState = _CienaCesChassisSMSamplesHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1, 3),
    _CienaCesChassisSMSamplesHealthState_Type()
)
cienaCesChassisSMSamplesHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthState.setStatus("current")
_CienaCesChassisSMSamplesHealthCurrMeasurement_Type = Integer32
_CienaCesChassisSMSamplesHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisSMSamplesHealthCurrMeasurement = _CienaCesChassisSMSamplesHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1, 4),
    _CienaCesChassisSMSamplesHealthCurrMeasurement_Type()
)
cienaCesChassisSMSamplesHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthCurrMeasurement.setStatus("current")
_CienaCesChassisSMSamplesHealthMaxMeasurement_Type = Integer32
_CienaCesChassisSMSamplesHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisSMSamplesHealthMaxMeasurement = _CienaCesChassisSMSamplesHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 11, 1, 5),
    _CienaCesChassisSMSamplesHealthMaxMeasurement_Type()
)
cienaCesChassisSMSamplesHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMSamplesHealthMaxMeasurement.setStatus("current")
_CienaCesChassisDiskHealthTable_Object = MibTable
cienaCesChassisDiskHealthTable = _CienaCesChassisDiskHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12)
)
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthTable.setStatus("current")
_CienaCesChassisDiskHealthEntry_Object = MibTableRow
cienaCesChassisDiskHealthEntry = _CienaCesChassisDiskHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1)
)
cienaCesChassisDiskHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisDiskHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisDiskHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthEntry.setStatus("current")


class _CienaCesChassisDiskHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisDiskHealthSubCategory based on Integer32"""
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
          ("flash0", 1),
          ("ram", 2),
          ("usb", 3))
    )


_CienaCesChassisDiskHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisDiskHealthSubCategory_Object = MibTableColumn
cienaCesChassisDiskHealthSubCategory = _CienaCesChassisDiskHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 1),
    _CienaCesChassisDiskHealthSubCategory_Type()
)
cienaCesChassisDiskHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthSubCategory.setStatus("current")
_CienaCesChassisDiskHealthOriginIndex_Type = Unsigned32
_CienaCesChassisDiskHealthOriginIndex_Object = MibTableColumn
cienaCesChassisDiskHealthOriginIndex = _CienaCesChassisDiskHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 2),
    _CienaCesChassisDiskHealthOriginIndex_Type()
)
cienaCesChassisDiskHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthOriginIndex.setStatus("current")
_CienaCesChassisDiskHealthState_Type = TceHealthStatus
_CienaCesChassisDiskHealthState_Object = MibTableColumn
cienaCesChassisDiskHealthState = _CienaCesChassisDiskHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 3),
    _CienaCesChassisDiskHealthState_Type()
)
cienaCesChassisDiskHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthState.setStatus("current")
_CienaCesChassisDiskHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisDiskHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisDiskHealthCurrMeasurement = _CienaCesChassisDiskHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 4),
    _CienaCesChassisDiskHealthCurrMeasurement_Type()
)
cienaCesChassisDiskHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthCurrMeasurement.setUnits("KB")
_CienaCesChassisDiskHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisDiskHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisDiskHealthMaxMeasurement = _CienaCesChassisDiskHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 5),
    _CienaCesChassisDiskHealthMaxMeasurement_Type()
)
cienaCesChassisDiskHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthMaxMeasurement.setUnits("KB")
_CienaCesChassisDiskHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisDiskHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisDiskHealthMaxThreshold = _CienaCesChassisDiskHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 12, 1, 6),
    _CienaCesChassisDiskHealthMaxThreshold_Type()
)
cienaCesChassisDiskHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisDiskHealthMaxThreshold.setUnits("KB")
_CienaCesChassisModuleTempHealthTable_Object = MibTable
cienaCesChassisModuleTempHealthTable = _CienaCesChassisModuleTempHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13)
)
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthTable.setStatus("current")
_CienaCesChassisModuleTempHealthEntry_Object = MibTableRow
cienaCesChassisModuleTempHealthEntry = _CienaCesChassisModuleTempHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1)
)
cienaCesChassisModuleTempHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModuleTempHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModuleTempHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthEntry.setStatus("current")


class _CienaCesChassisModuleTempHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisModuleTempHealthSubCategory based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("sensor1", 1),
          ("sensor2", 2),
          ("sensor3", 3),
          ("sensor4", 4),
          ("sensor5", 5),
          ("sensor6", 6),
          ("sensor7", 7),
          ("sensor8", 8),
          ("sensor9", 9),
          ("sensor10", 10),
          ("sensor11", 11),
          ("sensor12", 12),
          ("sensor13", 13),
          ("sensor14", 14),
          ("sensor15", 15),
          ("sensor16", 16),
          ("sensor17", 17),
          ("sensor18", 18),
          ("sensor19", 19),
          ("sensor20", 20),
          ("sensor21", 21),
          ("sensor22", 22),
          ("sensor23", 23),
          ("sensor24", 24),
          ("sensor25", 25),
          ("sensor26", 26),
          ("sensor27", 27))
    )


_CienaCesChassisModuleTempHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisModuleTempHealthSubCategory_Object = MibTableColumn
cienaCesChassisModuleTempHealthSubCategory = _CienaCesChassisModuleTempHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 1),
    _CienaCesChassisModuleTempHealthSubCategory_Type()
)
cienaCesChassisModuleTempHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthSubCategory.setStatus("current")
_CienaCesChassisModuleTempHealthOriginIndex_Type = Unsigned32
_CienaCesChassisModuleTempHealthOriginIndex_Object = MibTableColumn
cienaCesChassisModuleTempHealthOriginIndex = _CienaCesChassisModuleTempHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 2),
    _CienaCesChassisModuleTempHealthOriginIndex_Type()
)
cienaCesChassisModuleTempHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthOriginIndex.setStatus("current")
_CienaCesChassisModuleTempHealthState_Type = TceHealthStatus
_CienaCesChassisModuleTempHealthState_Object = MibTableColumn
cienaCesChassisModuleTempHealthState = _CienaCesChassisModuleTempHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 3),
    _CienaCesChassisModuleTempHealthState_Type()
)
cienaCesChassisModuleTempHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthState.setStatus("current")
_CienaCesChassisModuleTempHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisModuleTempHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisModuleTempHealthCurrMeasurement = _CienaCesChassisModuleTempHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 4),
    _CienaCesChassisModuleTempHealthCurrMeasurement_Type()
)
cienaCesChassisModuleTempHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthCurrMeasurement.setUnits("deg C")
_CienaCesChassisModuleTempHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisModuleTempHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisModuleTempHealthMinMeasurement = _CienaCesChassisModuleTempHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 5),
    _CienaCesChassisModuleTempHealthMinMeasurement_Type()
)
cienaCesChassisModuleTempHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMinMeasurement.setUnits("deg C")
_CienaCesChassisModuleTempHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisModuleTempHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisModuleTempHealthMaxMeasurement = _CienaCesChassisModuleTempHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 6),
    _CienaCesChassisModuleTempHealthMaxMeasurement_Type()
)
cienaCesChassisModuleTempHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMaxMeasurement.setUnits("deg C")
_CienaCesChassisModuleTempHealthMinThreshold_Type = Unsigned32
_CienaCesChassisModuleTempHealthMinThreshold_Object = MibTableColumn
cienaCesChassisModuleTempHealthMinThreshold = _CienaCesChassisModuleTempHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 7),
    _CienaCesChassisModuleTempHealthMinThreshold_Type()
)
cienaCesChassisModuleTempHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMinThreshold.setUnits("deg C")
_CienaCesChassisModuleTempHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisModuleTempHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisModuleTempHealthMaxThreshold = _CienaCesChassisModuleTempHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 13, 1, 8),
    _CienaCesChassisModuleTempHealthMaxThreshold_Type()
)
cienaCesChassisModuleTempHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModuleTempHealthMaxThreshold.setUnits("deg C")
_CienaCesChassisModuleSamplesHealthTable_Object = MibTable
cienaCesChassisModuleSamplesHealthTable = _CienaCesChassisModuleSamplesHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14)
)
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthTable.setStatus("current")
_CienaCesChassisModuleSamplesHealthEntry_Object = MibTableRow
cienaCesChassisModuleSamplesHealthEntry = _CienaCesChassisModuleSamplesHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1)
)
cienaCesChassisModuleSamplesHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModuleSamplesHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModuleSamplesHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthEntry.setStatus("current")


class _CienaCesChassisModuleSamplesHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisModuleSamplesHealthSubCategory based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sensor1Invalid", 1),
          ("sensor2Invalid", 2),
          ("sensor3Invalid", 3),
          ("sensor4Invalid", 4),
          ("sensor5Invalid", 5),
          ("sensor6Invalid", 6),
          ("sensor7Invalid", 7),
          ("sensor8Invalid", 8),
          ("sensor9Invalid", 9),
          ("sensor10Invalid", 10),
          ("sensor11Invalid", 11),
          ("sensor12Invalid", 12),
          ("sensor13Invalid", 13),
          ("sensor14Invalid", 14),
          ("sensor15Invalid", 15),
          ("sensor16Invalid", 16),
          ("sensor17Invalid", 17),
          ("sensor18Invalid", 18),
          ("sensor19Invalid", 19),
          ("sensor20Invalid", 20),
          ("sensor21Invalid", 21),
          ("sensor22Invalid", 22),
          ("sensor23Invalid", 23),
          ("sensor24Invalid", 24),
          ("sensor25Invalid", 25),
          ("sensor26Invalid", 26),
          ("sensor27Invalid", 27))
    )


_CienaCesChassisModuleSamplesHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisModuleSamplesHealthSubCategory_Object = MibTableColumn
cienaCesChassisModuleSamplesHealthSubCategory = _CienaCesChassisModuleSamplesHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1, 1),
    _CienaCesChassisModuleSamplesHealthSubCategory_Type()
)
cienaCesChassisModuleSamplesHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthSubCategory.setStatus("current")
_CienaCesChassisModuleSamplesHealthOriginIndex_Type = Unsigned32
_CienaCesChassisModuleSamplesHealthOriginIndex_Object = MibTableColumn
cienaCesChassisModuleSamplesHealthOriginIndex = _CienaCesChassisModuleSamplesHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1, 2),
    _CienaCesChassisModuleSamplesHealthOriginIndex_Type()
)
cienaCesChassisModuleSamplesHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthOriginIndex.setStatus("current")
_CienaCesChassisModuleSamplesHealthState_Type = TceHealthStatus
_CienaCesChassisModuleSamplesHealthState_Object = MibTableColumn
cienaCesChassisModuleSamplesHealthState = _CienaCesChassisModuleSamplesHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1, 3),
    _CienaCesChassisModuleSamplesHealthState_Type()
)
cienaCesChassisModuleSamplesHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthState.setStatus("current")
_CienaCesChassisModuleSamplesHealthCurrMeasurement_Type = Integer32
_CienaCesChassisModuleSamplesHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisModuleSamplesHealthCurrMeasurement = _CienaCesChassisModuleSamplesHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1, 4),
    _CienaCesChassisModuleSamplesHealthCurrMeasurement_Type()
)
cienaCesChassisModuleSamplesHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthCurrMeasurement.setStatus("current")
_CienaCesChassisModuleSamplesHealthMaxMeasurement_Type = Integer32
_CienaCesChassisModuleSamplesHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisModuleSamplesHealthMaxMeasurement = _CienaCesChassisModuleSamplesHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 14, 1, 5),
    _CienaCesChassisModuleSamplesHealthMaxMeasurement_Type()
)
cienaCesChassisModuleSamplesHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModuleSamplesHealthMaxMeasurement.setStatus("current")
_CienaCesChassisFanTrayHealthTable_Object = MibTable
cienaCesChassisFanTrayHealthTable = _CienaCesChassisFanTrayHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 15)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayHealthTable.setStatus("current")
_CienaCesChassisFanTrayHealthEntry_Object = MibTableRow
cienaCesChassisFanTrayHealthEntry = _CienaCesChassisFanTrayHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 15, 1)
)
cienaCesChassisFanTrayHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayHealthEntry.setStatus("current")


class _CienaCesChassisFanTrayHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanTrayHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisFanTrayHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanTrayHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanTrayHealthSubCategory = _CienaCesChassisFanTrayHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 15, 1, 1),
    _CienaCesChassisFanTrayHealthSubCategory_Type()
)
cienaCesChassisFanTrayHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayHealthSubCategory.setStatus("current")
_CienaCesChassisFanTrayHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanTrayHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanTrayHealthOriginIndex = _CienaCesChassisFanTrayHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 15, 1, 2),
    _CienaCesChassisFanTrayHealthOriginIndex_Type()
)
cienaCesChassisFanTrayHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayHealthOriginIndex.setStatus("current")
_CienaCesChassisFanTrayHealthState_Type = TceHealthStatus
_CienaCesChassisFanTrayHealthState_Object = MibTableColumn
cienaCesChassisFanTrayHealthState = _CienaCesChassisFanTrayHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 15, 1, 3),
    _CienaCesChassisFanTrayHealthState_Type()
)
cienaCesChassisFanTrayHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayHealthState.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthTable_Object = MibTable
cienaCesChassisFanTraySpeedMismatchHealthTable = _CienaCesChassisFanTraySpeedMismatchHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthTable.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthEntry_Object = MibTableRow
cienaCesChassisFanTraySpeedMismatchHealthEntry = _CienaCesChassisFanTraySpeedMismatchHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1)
)
cienaCesChassisFanTraySpeedMismatchHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySpeedMismatchHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySpeedMismatchHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthEntry.setStatus("current")


class _CienaCesChassisFanTraySpeedMismatchHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanTraySpeedMismatchHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("count", 1))
    )


_CienaCesChassisFanTraySpeedMismatchHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanTraySpeedMismatchHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthSubCategory = _CienaCesChassisFanTraySpeedMismatchHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 1),
    _CienaCesChassisFanTraySpeedMismatchHealthSubCategory_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthSubCategory.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanTraySpeedMismatchHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthOriginIndex = _CienaCesChassisFanTraySpeedMismatchHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 2),
    _CienaCesChassisFanTraySpeedMismatchHealthOriginIndex_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthOriginIndex.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthState_Type = TceHealthStatus
_CienaCesChassisFanTraySpeedMismatchHealthState_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthState = _CienaCesChassisFanTraySpeedMismatchHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 3),
    _CienaCesChassisFanTraySpeedMismatchHealthState_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthState.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement_Type = Integer32
_CienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement = _CienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 4),
    _CienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement_Type = Integer32
_CienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement = _CienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 5),
    _CienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement.setStatus("current")
_CienaCesChassisFanTraySpeedMismatchHealthMaxThreshold_Type = Integer32
_CienaCesChassisFanTraySpeedMismatchHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisFanTraySpeedMismatchHealthMaxThreshold = _CienaCesChassisFanTraySpeedMismatchHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 16, 1, 6),
    _CienaCesChassisFanTraySpeedMismatchHealthMaxThreshold_Type()
)
cienaCesChassisFanTraySpeedMismatchHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTraySpeedMismatchHealthMaxThreshold.setStatus("current")
_CienaCesChassisFanSpeedMismatchHealthTable_Object = MibTable
cienaCesChassisFanSpeedMismatchHealthTable = _CienaCesChassisFanSpeedMismatchHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 17)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMismatchHealthTable.setStatus("current")
_CienaCesChassisFanSpeedMismatchHealthEntry_Object = MibTableRow
cienaCesChassisFanSpeedMismatchHealthEntry = _CienaCesChassisFanSpeedMismatchHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 17, 1)
)
cienaCesChassisFanSpeedMismatchHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSpeedMismatchHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSpeedMismatchHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMismatchHealthEntry.setStatus("current")


class _CienaCesChassisFanSpeedMismatchHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanSpeedMismatchHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisFanSpeedMismatchHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanSpeedMismatchHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanSpeedMismatchHealthSubCategory = _CienaCesChassisFanSpeedMismatchHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 17, 1, 1),
    _CienaCesChassisFanSpeedMismatchHealthSubCategory_Type()
)
cienaCesChassisFanSpeedMismatchHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMismatchHealthSubCategory.setStatus("current")
_CienaCesChassisFanSpeedMismatchHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanSpeedMismatchHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanSpeedMismatchHealthOriginIndex = _CienaCesChassisFanSpeedMismatchHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 17, 1, 2),
    _CienaCesChassisFanSpeedMismatchHealthOriginIndex_Type()
)
cienaCesChassisFanSpeedMismatchHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMismatchHealthOriginIndex.setStatus("current")
_CienaCesChassisFanSpeedMismatchHealthState_Type = TceHealthStatus
_CienaCesChassisFanSpeedMismatchHealthState_Object = MibTableColumn
cienaCesChassisFanSpeedMismatchHealthState = _CienaCesChassisFanSpeedMismatchHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 17, 1, 3),
    _CienaCesChassisFanSpeedMismatchHealthState_Type()
)
cienaCesChassisFanSpeedMismatchHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMismatchHealthState.setStatus("current")
_CienaCesChassisFanTempHealthTable_Object = MibTable
cienaCesChassisFanTempHealthTable = _CienaCesChassisFanTempHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthTable.setStatus("current")
_CienaCesChassisFanTempHealthEntry_Object = MibTableRow
cienaCesChassisFanTempHealthEntry = _CienaCesChassisFanTempHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1)
)
cienaCesChassisFanTempHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthEntry.setStatus("current")


class _CienaCesChassisFanTempHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanTempHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("temperature", 1))
    )


_CienaCesChassisFanTempHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanTempHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanTempHealthSubCategory = _CienaCesChassisFanTempHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 1),
    _CienaCesChassisFanTempHealthSubCategory_Type()
)
cienaCesChassisFanTempHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthSubCategory.setStatus("current")
_CienaCesChassisFanTempHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanTempHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanTempHealthOriginIndex = _CienaCesChassisFanTempHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 2),
    _CienaCesChassisFanTempHealthOriginIndex_Type()
)
cienaCesChassisFanTempHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthOriginIndex.setStatus("current")
_CienaCesChassisFanTempHealthState_Type = TceHealthStatus
_CienaCesChassisFanTempHealthState_Object = MibTableColumn
cienaCesChassisFanTempHealthState = _CienaCesChassisFanTempHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 3),
    _CienaCesChassisFanTempHealthState_Type()
)
cienaCesChassisFanTempHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthState.setStatus("current")
_CienaCesChassisFanTempHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisFanTempHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFanTempHealthCurrMeasurement = _CienaCesChassisFanTempHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 4),
    _CienaCesChassisFanTempHealthCurrMeasurement_Type()
)
cienaCesChassisFanTempHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthCurrMeasurement.setUnits("deg C")
_CienaCesChassisFanTempHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisFanTempHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisFanTempHealthMinMeasurement = _CienaCesChassisFanTempHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 5),
    _CienaCesChassisFanTempHealthMinMeasurement_Type()
)
cienaCesChassisFanTempHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMinMeasurement.setUnits("deg C")
_CienaCesChassisFanTempHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisFanTempHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisFanTempHealthMaxMeasurement = _CienaCesChassisFanTempHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 6),
    _CienaCesChassisFanTempHealthMaxMeasurement_Type()
)
cienaCesChassisFanTempHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMaxMeasurement.setUnits("deg C")
_CienaCesChassisFanTempHealthMinThreshold_Type = Unsigned32
_CienaCesChassisFanTempHealthMinThreshold_Object = MibTableColumn
cienaCesChassisFanTempHealthMinThreshold = _CienaCesChassisFanTempHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 7),
    _CienaCesChassisFanTempHealthMinThreshold_Type()
)
cienaCesChassisFanTempHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMinThreshold.setUnits("deg C")
_CienaCesChassisFanTempHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisFanTempHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisFanTempHealthMaxThreshold = _CienaCesChassisFanTempHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 18, 1, 8),
    _CienaCesChassisFanTempHealthMaxThreshold_Type()
)
cienaCesChassisFanTempHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanTempHealthMaxThreshold.setUnits("deg C")
_CienaCesChassisFanSamplesHealthTable_Object = MibTable
cienaCesChassisFanSamplesHealthTable = _CienaCesChassisFanSamplesHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthTable.setStatus("current")
_CienaCesChassisFanSamplesHealthEntry_Object = MibTableRow
cienaCesChassisFanSamplesHealthEntry = _CienaCesChassisFanSamplesHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1)
)
cienaCesChassisFanSamplesHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSamplesHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSamplesHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthEntry.setStatus("current")


class _CienaCesChassisFanSamplesHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanSamplesHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid", 1))
    )


_CienaCesChassisFanSamplesHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanSamplesHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanSamplesHealthSubCategory = _CienaCesChassisFanSamplesHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1, 1),
    _CienaCesChassisFanSamplesHealthSubCategory_Type()
)
cienaCesChassisFanSamplesHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthSubCategory.setStatus("current")
_CienaCesChassisFanSamplesHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanSamplesHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanSamplesHealthOriginIndex = _CienaCesChassisFanSamplesHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1, 2),
    _CienaCesChassisFanSamplesHealthOriginIndex_Type()
)
cienaCesChassisFanSamplesHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthOriginIndex.setStatus("current")
_CienaCesChassisFanSamplesHealthState_Type = TceHealthStatus
_CienaCesChassisFanSamplesHealthState_Object = MibTableColumn
cienaCesChassisFanSamplesHealthState = _CienaCesChassisFanSamplesHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1, 3),
    _CienaCesChassisFanSamplesHealthState_Type()
)
cienaCesChassisFanSamplesHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthState.setStatus("current")
_CienaCesChassisFanSamplesHealthCurrMeasurement_Type = Integer32
_CienaCesChassisFanSamplesHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFanSamplesHealthCurrMeasurement = _CienaCesChassisFanSamplesHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1, 4),
    _CienaCesChassisFanSamplesHealthCurrMeasurement_Type()
)
cienaCesChassisFanSamplesHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthCurrMeasurement.setStatus("current")
_CienaCesChassisFanSamplesHealthMaxMeasurement_Type = Integer32
_CienaCesChassisFanSamplesHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisFanSamplesHealthMaxMeasurement = _CienaCesChassisFanSamplesHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 19, 1, 5),
    _CienaCesChassisFanSamplesHealthMaxMeasurement_Type()
)
cienaCesChassisFanSamplesHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanSamplesHealthMaxMeasurement.setStatus("current")
_CienaCesChassisFanRPMHealthTable_Object = MibTable
cienaCesChassisFanRPMHealthTable = _CienaCesChassisFanRPMHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20)
)
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthTable.setStatus("current")
_CienaCesChassisFanRPMHealthEntry_Object = MibTableRow
cienaCesChassisFanRPMHealthEntry = _CienaCesChassisFanRPMHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1)
)
cienaCesChassisFanRPMHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanRPMHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanRPMHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthEntry.setStatus("current")


class _CienaCesChassisFanRPMHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFanRPMHealthSubCategory based on Integer32"""
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
          ("maxSpeed", 1),
          ("minSpeed", 2))
    )


_CienaCesChassisFanRPMHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFanRPMHealthSubCategory_Object = MibTableColumn
cienaCesChassisFanRPMHealthSubCategory = _CienaCesChassisFanRPMHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 1),
    _CienaCesChassisFanRPMHealthSubCategory_Type()
)
cienaCesChassisFanRPMHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthSubCategory.setStatus("current")
_CienaCesChassisFanRPMHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFanRPMHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFanRPMHealthOriginIndex = _CienaCesChassisFanRPMHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 2),
    _CienaCesChassisFanRPMHealthOriginIndex_Type()
)
cienaCesChassisFanRPMHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthOriginIndex.setStatus("current")
_CienaCesChassisFanRPMHealthState_Type = TceHealthStatus
_CienaCesChassisFanRPMHealthState_Object = MibTableColumn
cienaCesChassisFanRPMHealthState = _CienaCesChassisFanRPMHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 3),
    _CienaCesChassisFanRPMHealthState_Type()
)
cienaCesChassisFanRPMHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthState.setStatus("current")
_CienaCesChassisFanRPMHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisFanRPMHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFanRPMHealthCurrMeasurement = _CienaCesChassisFanRPMHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 4),
    _CienaCesChassisFanRPMHealthCurrMeasurement_Type()
)
cienaCesChassisFanRPMHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthCurrMeasurement.setUnits("RPM")
_CienaCesChassisFanRPMHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisFanRPMHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisFanRPMHealthMinMeasurement = _CienaCesChassisFanRPMHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 5),
    _CienaCesChassisFanRPMHealthMinMeasurement_Type()
)
cienaCesChassisFanRPMHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthMinMeasurement.setUnits("RPM")
_CienaCesChassisFanRPMHealthMinThreshold_Type = Unsigned32
_CienaCesChassisFanRPMHealthMinThreshold_Object = MibTableColumn
cienaCesChassisFanRPMHealthMinThreshold = _CienaCesChassisFanRPMHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 20, 1, 6),
    _CienaCesChassisFanRPMHealthMinThreshold_Type()
)
cienaCesChassisFanRPMHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFanRPMHealthMinThreshold.setUnits("RPM")
_CienaCesChassisPowerHealthTable_Object = MibTable
cienaCesChassisPowerHealthTable = _CienaCesChassisPowerHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 21)
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerHealthTable.setStatus("current")
_CienaCesChassisPowerHealthEntry_Object = MibTableRow
cienaCesChassisPowerHealthEntry = _CienaCesChassisPowerHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 21, 1)
)
cienaCesChassisPowerHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerHealthEntry.setStatus("current")


class _CienaCesChassisPowerHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisPowerHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisPowerHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisPowerHealthSubCategory_Object = MibTableColumn
cienaCesChassisPowerHealthSubCategory = _CienaCesChassisPowerHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 21, 1, 1),
    _CienaCesChassisPowerHealthSubCategory_Type()
)
cienaCesChassisPowerHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerHealthSubCategory.setStatus("current")
_CienaCesChassisPowerHealthOriginIndex_Type = Unsigned32
_CienaCesChassisPowerHealthOriginIndex_Object = MibTableColumn
cienaCesChassisPowerHealthOriginIndex = _CienaCesChassisPowerHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 21, 1, 2),
    _CienaCesChassisPowerHealthOriginIndex_Type()
)
cienaCesChassisPowerHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerHealthOriginIndex.setStatus("current")
_CienaCesChassisPowerHealthState_Type = TceHealthStatus
_CienaCesChassisPowerHealthState_Object = MibTableColumn
cienaCesChassisPowerHealthState = _CienaCesChassisPowerHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 21, 1, 3),
    _CienaCesChassisPowerHealthState_Type()
)
cienaCesChassisPowerHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerHealthState.setStatus("current")
_CienaCesChassisFeedPowerHealthTable_Object = MibTable
cienaCesChassisFeedPowerHealthTable = _CienaCesChassisFeedPowerHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 22)
)
if mibBuilder.loadTexts:
    cienaCesChassisFeedPowerHealthTable.setStatus("current")
_CienaCesChassisFeedPowerHealthEntry_Object = MibTableRow
cienaCesChassisFeedPowerHealthEntry = _CienaCesChassisFeedPowerHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 22, 1)
)
cienaCesChassisFeedPowerHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFeedPowerHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFeedPowerHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFeedPowerHealthEntry.setStatus("current")


class _CienaCesChassisFeedPowerHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFeedPowerHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisFeedPowerHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFeedPowerHealthSubCategory_Object = MibTableColumn
cienaCesChassisFeedPowerHealthSubCategory = _CienaCesChassisFeedPowerHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 22, 1, 1),
    _CienaCesChassisFeedPowerHealthSubCategory_Type()
)
cienaCesChassisFeedPowerHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFeedPowerHealthSubCategory.setStatus("current")
_CienaCesChassisFeedPowerHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFeedPowerHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFeedPowerHealthOriginIndex = _CienaCesChassisFeedPowerHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 22, 1, 2),
    _CienaCesChassisFeedPowerHealthOriginIndex_Type()
)
cienaCesChassisFeedPowerHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFeedPowerHealthOriginIndex.setStatus("current")
_CienaCesChassisFeedPowerHealthState_Type = TceHealthStatus
_CienaCesChassisFeedPowerHealthState_Object = MibTableColumn
cienaCesChassisFeedPowerHealthState = _CienaCesChassisFeedPowerHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 22, 1, 3),
    _CienaCesChassisFeedPowerHealthState_Type()
)
cienaCesChassisFeedPowerHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFeedPowerHealthState.setStatus("current")
_CienaCesChassisResourceHealthTable_Object = MibTable
cienaCesChassisResourceHealthTable = _CienaCesChassisResourceHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23)
)
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthTable.setStatus("current")
_CienaCesChassisResourceHealthEntry_Object = MibTableRow
cienaCesChassisResourceHealthEntry = _CienaCesChassisResourceHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1)
)
cienaCesChassisResourceHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisResourceHealthSubCategory"),
)
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthEntry.setStatus("current")


class _CienaCesChassisResourceHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisResourceHealthSubCategory based on Integer32"""
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
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("aggTable", 1),
          ("meterProfileAttachmentTable", 2),
          ("meterProfileTable", 3),
          ("pbtDecapTable", 4),
          ("pbtEncapTable", 5),
          ("pbtServiceTable", 6),
          ("pbtTransitTable", 7),
          ("pbtTunnelGroupTable", 8),
          ("pbtLocalBridgeTable", 9),
          ("pbtRemoteBridgeTable", 10),
          ("perfMonBins", 11),
          ("perfMonInstances", 12),
          ("portStateGrpTable", 13),
          ("qosFlowTable", 14),
          ("subportTable", 15),
          ("vssTable", 16),
          ("trafficClassTermTable", 17),
          ("floodContainerTable", 18),
          ("floodContainerAttachments", 19),
          ("logicalInterfaces", 20),
          ("sharedRateProfiles", 21),
          ("sharedRateAttachments", 22),
          ("sharedRateTCEs", 23),
          ("sharedRateAclTCEs", 24),
          ("shapingProfiles", 25),
          ("shapingProfileAttachments", 26),
          ("cpuSubInterfaces", 27),
          ("accessFlows", 28),
          ("vIs", 29),
          ("mcastForwardingEnhancedVswitches", 30),
          ("statsAttachments", 31),
          ("cfmServices", 32),
          ("cfmMip", 33),
          ("cfmMep", 34),
          ("cfmRMep", 35),
          ("cfmLmm", 36),
          ("cfmDmm", 37),
          ("mplsTunnelPath", 38),
          ("mplsTunnelPathHops", 39),
          ("mplsTunnelGroups", 40),
          ("mplsEncapTunnels", 41),
          ("mplsNextHopEntries", 42),
          ("mplsDecapTunnels", 43),
          ("mplsVitualSwitchs", 44),
          ("mplsVCs", 45),
          ("mplsInterfaces", 46),
          ("vplsPeMeshGroups", 47),
          ("resolvedCosProfileTable", 48),
          ("resolvedCosMapTable", 49),
          ("frameCosMapTable", 50),
          ("congestionAvoidanceProfileTable", 51),
          ("rCosQueueMapTable", 52),
          ("queueGroupProfileTable", 53),
          ("queueGroupInstanceTable", 54),
          ("schedulerProfileTable", 55),
          ("schedulerInstanceTable", 56),
          ("smacId", 57),
          ("multicastGroup", 58),
          ("pltfmVfd", 59),
          ("pltfmMcGroupMap", 60),
          ("pltfmVInterface", 61),
          ("pltfmVpldIndex", 62),
          ("pltfmReservedMac", 63),
          ("pltfmRateProfile", 64),
          ("pltfmTokenBucket", 65),
          ("pltfmResolvedCosMap", 66),
          ("pltfmFrameCopsMap", 67),
          ("pltfmTunnelGroup", 68),
          ("pltfmEgressTunnel", 69),
          ("pltfmVirtualTcam", 70),
          ("pltfmAclTcam", 71),
          ("pltfmMstpInstance", 72),
          ("pltfmFlushGroupInstance", 73),
          ("pltfmVOQ", 74),
          ("pltfmCLScheduler", 75),
          ("pltfmFQScheduler", 76),
          ("pltfmSchedulerFlow", 77),
          ("pltfmDestFap", 78),
          ("pltfmMplsEncapIndex", 79),
          ("pltfmMplsVpldIndex", 80),
          ("pltfmEgressArpIndex", 81),
          ("pltfmEgressShapingCir", 82),
          ("mplsTransitTunnels", 83),
          ("pltfmLocalDestIndex", 84),
          ("pltfmBscp", 85),
          ("pltfmHighRateTokenBucket", 86),
          ("pltfmLowRateTokenBucket", 87),
          ("pltfmParentMeter", 88),
          ("pltfmChildMeter", 89),
          ("pltfmL2UserTypes", 90),
          ("pltfmLocalBridgeMacs", 91),
          ("pltfmPpRif", 92),
          ("pltfmLmPowerBudget", 93),
          ("pltfmPpIngressL2Xform", 94),
          ("pltfmPpEgressL2xform", 95),
          ("pltfmPpInternalTcam", 96),
          ("pltfmPpFECPointer", 97),
          ("ethLpTable", 98),
          ("pltfmPpFECPointerVRing", 99),
          ("l2CftProfile", 100),
          ("pfgProfile", 101),
          ("pltfmNpMaintPoint", 102),
          ("pltfmNpMaintPointSession", 103),
          ("pltfmNpFastTimer300Hz", 104),
          ("pltfmNpFastTimer10msec", 105),
          ("pltfmNpFastTimer100msec", 106),
          ("pltfmNpFastTimer1sec", 107),
          ("pltfmNpSlowTimer", 108),
          ("pltfmNpWatchdogTimer", 109),
          ("pltfmNpProtectionGroup", 110),
          ("benchmarkReflectorProfile", 111),
          ("aisSession", 112))
    )


_CienaCesChassisResourceHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisResourceHealthSubCategory_Object = MibTableColumn
cienaCesChassisResourceHealthSubCategory = _CienaCesChassisResourceHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1, 1),
    _CienaCesChassisResourceHealthSubCategory_Type()
)
cienaCesChassisResourceHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthSubCategory.setStatus("current")
_CienaCesChassisResourceHealthState_Type = TceHealthStatus
_CienaCesChassisResourceHealthState_Object = MibTableColumn
cienaCesChassisResourceHealthState = _CienaCesChassisResourceHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1, 2),
    _CienaCesChassisResourceHealthState_Type()
)
cienaCesChassisResourceHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthState.setStatus("current")
_CienaCesChassisResourceHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisResourceHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisResourceHealthCurrMeasurement = _CienaCesChassisResourceHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1, 3),
    _CienaCesChassisResourceHealthCurrMeasurement_Type()
)
cienaCesChassisResourceHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthCurrMeasurement.setStatus("current")
_CienaCesChassisResourceHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisResourceHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisResourceHealthMaxMeasurement = _CienaCesChassisResourceHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1, 4),
    _CienaCesChassisResourceHealthMaxMeasurement_Type()
)
cienaCesChassisResourceHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthMaxMeasurement.setStatus("current")
_CienaCesChassisResourceHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisResourceHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisResourceHealthMaxThreshold = _CienaCesChassisResourceHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 23, 1, 5),
    _CienaCesChassisResourceHealthMaxThreshold_Type()
)
cienaCesChassisResourceHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisResourceHealthMaxThreshold.setStatus("current")
_CienaCesChassisMemoryHealthTable_Object = MibTable
cienaCesChassisMemoryHealthTable = _CienaCesChassisMemoryHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24)
)
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthTable.setStatus("current")
_CienaCesChassisMemoryHealthEntry_Object = MibTableRow
cienaCesChassisMemoryHealthEntry = _CienaCesChassisMemoryHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1)
)
cienaCesChassisMemoryHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisMemoryHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisMemoryHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthEntry.setStatus("current")


class _CienaCesChassisMemoryHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisMemoryHealthSubCategory based on Integer32"""
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
        *(("none", 0),
          ("globalHeap", 1),
          ("heap1", 2),
          ("heap2", 3),
          ("pool1", 4),
          ("pool2", 5),
          ("heap", 6))
    )


_CienaCesChassisMemoryHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisMemoryHealthSubCategory_Object = MibTableColumn
cienaCesChassisMemoryHealthSubCategory = _CienaCesChassisMemoryHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 1),
    _CienaCesChassisMemoryHealthSubCategory_Type()
)
cienaCesChassisMemoryHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthSubCategory.setStatus("current")
_CienaCesChassisMemoryHealthOriginIndex_Type = Unsigned32
_CienaCesChassisMemoryHealthOriginIndex_Object = MibTableColumn
cienaCesChassisMemoryHealthOriginIndex = _CienaCesChassisMemoryHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 2),
    _CienaCesChassisMemoryHealthOriginIndex_Type()
)
cienaCesChassisMemoryHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthOriginIndex.setStatus("current")
_CienaCesChassisMemoryHealthState_Type = TceHealthStatus
_CienaCesChassisMemoryHealthState_Object = MibTableColumn
cienaCesChassisMemoryHealthState = _CienaCesChassisMemoryHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 3),
    _CienaCesChassisMemoryHealthState_Type()
)
cienaCesChassisMemoryHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthState.setStatus("current")
_CienaCesChassisMemoryHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisMemoryHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisMemoryHealthCurrMeasurement = _CienaCesChassisMemoryHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 4),
    _CienaCesChassisMemoryHealthCurrMeasurement_Type()
)
cienaCesChassisMemoryHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthCurrMeasurement.setUnits("KB")
_CienaCesChassisMemoryHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisMemoryHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisMemoryHealthMaxMeasurement = _CienaCesChassisMemoryHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 5),
    _CienaCesChassisMemoryHealthMaxMeasurement_Type()
)
cienaCesChassisMemoryHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthMaxMeasurement.setUnits("KB")
_CienaCesChassisMemoryHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisMemoryHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisMemoryHealthMaxThreshold = _CienaCesChassisMemoryHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 24, 1, 6),
    _CienaCesChassisMemoryHealthMaxThreshold_Type()
)
cienaCesChassisMemoryHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisMemoryHealthMaxThreshold.setUnits("KB")
_CienaCesChassisMACHealthTable_Object = MibTable
cienaCesChassisMACHealthTable = _CienaCesChassisMACHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25)
)
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthTable.setStatus("current")
_CienaCesChassisMACHealthEntry_Object = MibTableRow
cienaCesChassisMACHealthEntry = _CienaCesChassisMACHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1)
)
cienaCesChassisMACHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisMACHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisMACHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthEntry.setStatus("current")


class _CienaCesChassisMACHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisMACHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("mac-Table", 1))
    )


_CienaCesChassisMACHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisMACHealthSubCategory_Object = MibTableColumn
cienaCesChassisMACHealthSubCategory = _CienaCesChassisMACHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 1),
    _CienaCesChassisMACHealthSubCategory_Type()
)
cienaCesChassisMACHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthSubCategory.setStatus("current")
_CienaCesChassisMACHealthOriginIndex_Type = Unsigned32
_CienaCesChassisMACHealthOriginIndex_Object = MibTableColumn
cienaCesChassisMACHealthOriginIndex = _CienaCesChassisMACHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 2),
    _CienaCesChassisMACHealthOriginIndex_Type()
)
cienaCesChassisMACHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthOriginIndex.setStatus("current")
_CienaCesChassisMACHealthState_Type = TceHealthStatus
_CienaCesChassisMACHealthState_Object = MibTableColumn
cienaCesChassisMACHealthState = _CienaCesChassisMACHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 3),
    _CienaCesChassisMACHealthState_Type()
)
cienaCesChassisMACHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthState.setStatus("current")
_CienaCesChassisMACHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisMACHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisMACHealthCurrMeasurement = _CienaCesChassisMACHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 4),
    _CienaCesChassisMACHealthCurrMeasurement_Type()
)
cienaCesChassisMACHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthCurrMeasurement.setStatus("current")
_CienaCesChassisMACHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisMACHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisMACHealthMaxMeasurement = _CienaCesChassisMACHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 5),
    _CienaCesChassisMACHealthMaxMeasurement_Type()
)
cienaCesChassisMACHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthMaxMeasurement.setStatus("current")
_CienaCesChassisMACHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisMACHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisMACHealthMaxThreshold = _CienaCesChassisMACHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 25, 1, 6),
    _CienaCesChassisMACHealthMaxThreshold_Type()
)
cienaCesChassisMACHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMACHealthMaxThreshold.setStatus("current")
_CienaCesChassisI2CHealthTable_Object = MibTable
cienaCesChassisI2CHealthTable = _CienaCesChassisI2CHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 26)
)
if mibBuilder.loadTexts:
    cienaCesChassisI2CHealthTable.setStatus("current")
_CienaCesChassisI2CHealthEntry_Object = MibTableRow
cienaCesChassisI2CHealthEntry = _CienaCesChassisI2CHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 26, 1)
)
cienaCesChassisI2CHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisI2CHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisI2CHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisI2CHealthEntry.setStatus("current")


class _CienaCesChassisI2CHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisI2CHealthSubCategory based on Integer32"""
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
              47)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pS1", 1),
          ("pS2", 2),
          ("alarmCard", 3),
          ("fanTray", 4),
          ("iOM3", 5),
          ("iOM4", 6),
          ("iOM5", 7),
          ("iOM6", 8),
          ("iOM7", 9),
          ("pduA1", 10),
          ("pduB1", 11),
          ("pduA2", 12),
          ("pduB2", 13),
          ("pduA3", 14),
          ("pduB3", 15),
          ("pduA4", 16),
          ("pduB4", 17),
          ("cfu1", 18),
          ("cfu2", 19),
          ("cfu3", 20),
          ("cfu4", 21),
          ("pslm1", 22),
          ("pslm2", 23),
          ("pslm3", 24),
          ("pslm4", 25),
          ("pslm5", 26),
          ("pslm6", 27),
          ("pslm7", 28),
          ("pslm8", 29),
          ("pslm9", 30),
          ("pslm10", 31),
          ("pslm11", 32),
          ("pslm12", 33),
          ("pslm13", 34),
          ("pslm14", 35),
          ("pslm15", 36),
          ("pslm16", 37),
          ("pslm17", 38),
          ("pslm18", 39),
          ("pslm19", 40),
          ("pslm20", 41),
          ("sm1", 42),
          ("sm2", 43),
          ("sm3", 44),
          ("sm4", 45),
          ("sm5", 46),
          ("iom", 47))
    )


_CienaCesChassisI2CHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisI2CHealthSubCategory_Object = MibTableColumn
cienaCesChassisI2CHealthSubCategory = _CienaCesChassisI2CHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 26, 1, 1),
    _CienaCesChassisI2CHealthSubCategory_Type()
)
cienaCesChassisI2CHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisI2CHealthSubCategory.setStatus("current")
_CienaCesChassisI2CHealthOriginIndex_Type = Unsigned32
_CienaCesChassisI2CHealthOriginIndex_Object = MibTableColumn
cienaCesChassisI2CHealthOriginIndex = _CienaCesChassisI2CHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 26, 1, 3),
    _CienaCesChassisI2CHealthOriginIndex_Type()
)
cienaCesChassisI2CHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisI2CHealthOriginIndex.setStatus("current")
_CienaCesChassisI2CHealthState_Type = TceHealthStatus
_CienaCesChassisI2CHealthState_Object = MibTableColumn
cienaCesChassisI2CHealthState = _CienaCesChassisI2CHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 26, 1, 4),
    _CienaCesChassisI2CHealthState_Type()
)
cienaCesChassisI2CHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisI2CHealthState.setStatus("current")
_CienaCesChassisFlashDriverHealthTable_Object = MibTable
cienaCesChassisFlashDriverHealthTable = _CienaCesChassisFlashDriverHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27)
)
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthTable.setStatus("current")
_CienaCesChassisFlashDriverHealthEntry_Object = MibTableRow
cienaCesChassisFlashDriverHealthEntry = _CienaCesChassisFlashDriverHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1)
)
cienaCesChassisFlashDriverHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFlashDriverHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFlashDriverHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthEntry.setStatus("current")


class _CienaCesChassisFlashDriverHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFlashDriverHealthSubCategory based on Integer32"""
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
          ("writeErasePart1", 1),
          ("writeErasePart2", 2))
    )


_CienaCesChassisFlashDriverHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFlashDriverHealthSubCategory_Object = MibTableColumn
cienaCesChassisFlashDriverHealthSubCategory = _CienaCesChassisFlashDriverHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1, 1),
    _CienaCesChassisFlashDriverHealthSubCategory_Type()
)
cienaCesChassisFlashDriverHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthSubCategory.setStatus("current")
_CienaCesChassisFlashDriverHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFlashDriverHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFlashDriverHealthOriginIndex = _CienaCesChassisFlashDriverHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1, 2),
    _CienaCesChassisFlashDriverHealthOriginIndex_Type()
)
cienaCesChassisFlashDriverHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthOriginIndex.setStatus("current")
_CienaCesChassisFlashDriverHealthState_Type = TceHealthStatus
_CienaCesChassisFlashDriverHealthState_Object = MibTableColumn
cienaCesChassisFlashDriverHealthState = _CienaCesChassisFlashDriverHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1, 3),
    _CienaCesChassisFlashDriverHealthState_Type()
)
cienaCesChassisFlashDriverHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthState.setStatus("current")
_CienaCesChassisFlashDriverHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisFlashDriverHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFlashDriverHealthCurrMeasurement = _CienaCesChassisFlashDriverHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1, 4),
    _CienaCesChassisFlashDriverHealthCurrMeasurement_Type()
)
cienaCesChassisFlashDriverHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthCurrMeasurement.setUnits("ms")
_CienaCesChassisFlashDriverHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisFlashDriverHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisFlashDriverHealthMaxMeasurement = _CienaCesChassisFlashDriverHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 27, 1, 5),
    _CienaCesChassisFlashDriverHealthMaxMeasurement_Type()
)
cienaCesChassisFlashDriverHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisFlashDriverHealthMaxMeasurement.setUnits("ms")
_CienaCesChassisXcvrHealthTable_Object = MibTable
cienaCesChassisXcvrHealthTable = _CienaCesChassisXcvrHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28)
)
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthTable.setStatus("current")
_CienaCesChassisXcvrHealthEntry_Object = MibTableRow
cienaCesChassisXcvrHealthEntry = _CienaCesChassisXcvrHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1)
)
cienaCesChassisXcvrHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisXcvrHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisXcvrHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthEntry.setStatus("current")


class _CienaCesChassisXcvrHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisXcvrHealthSubCategory based on Integer32"""
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
              37)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("temp", 1),
          ("rxPower", 2),
          ("txPower", 3),
          ("bias", 4),
          ("vcc", 5),
          ("rxPowerLane1", 6),
          ("rxPowerLane2", 7),
          ("rxPowerLane3", 8),
          ("rxPowerLane4", 9),
          ("rxPowerLane5", 10),
          ("rxPowerLane6", 11),
          ("rxPowerLane7", 12),
          ("rxPowerLane8", 13),
          ("rxPowerLane9", 14),
          ("rxPowerLane10", 15),
          ("rxPowerLane11", 16),
          ("rxPowerLane12", 17),
          ("rxPowerLane13", 18),
          ("rxPowerLane14", 19),
          ("rxPowerLane15", 20),
          ("rxPowerLane16", 21),
          ("txPowerLane1", 22),
          ("txPowerLane2", 23),
          ("txPowerLane3", 24),
          ("txPowerLane4", 25),
          ("txPowerLane5", 26),
          ("txPowerLane6", 27),
          ("txPowerLane7", 28),
          ("txPowerLane8", 29),
          ("txPowerLane9", 30),
          ("txPowerLane10", 31),
          ("txPowerLane11", 32),
          ("txPowerLane12", 33),
          ("txPowerLane13", 34),
          ("txPowerLane14", 35),
          ("txPowerLane15", 36),
          ("txPowerLane16", 37))
    )


_CienaCesChassisXcvrHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisXcvrHealthSubCategory_Object = MibTableColumn
cienaCesChassisXcvrHealthSubCategory = _CienaCesChassisXcvrHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 1),
    _CienaCesChassisXcvrHealthSubCategory_Type()
)
cienaCesChassisXcvrHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthSubCategory.setStatus("current")
_CienaCesChassisXcvrHealthOriginIndex_Type = Unsigned32
_CienaCesChassisXcvrHealthOriginIndex_Object = MibTableColumn
cienaCesChassisXcvrHealthOriginIndex = _CienaCesChassisXcvrHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 2),
    _CienaCesChassisXcvrHealthOriginIndex_Type()
)
cienaCesChassisXcvrHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthOriginIndex.setStatus("current")
_CienaCesChassisXcvrHealthState_Type = TceHealthStatus
_CienaCesChassisXcvrHealthState_Object = MibTableColumn
cienaCesChassisXcvrHealthState = _CienaCesChassisXcvrHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 3),
    _CienaCesChassisXcvrHealthState_Type()
)
cienaCesChassisXcvrHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthState.setStatus("current")
_CienaCesChassisXcvrHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisXcvrHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisXcvrHealthCurrMeasurement = _CienaCesChassisXcvrHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 4),
    _CienaCesChassisXcvrHealthCurrMeasurement_Type()
)
cienaCesChassisXcvrHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthCurrMeasurement.setStatus("current")
_CienaCesChassisXcvrHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisXcvrHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisXcvrHealthMinMeasurement = _CienaCesChassisXcvrHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 5),
    _CienaCesChassisXcvrHealthMinMeasurement_Type()
)
cienaCesChassisXcvrHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthMinMeasurement.setStatus("current")
_CienaCesChassisXcvrHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisXcvrHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisXcvrHealthMaxMeasurement = _CienaCesChassisXcvrHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 6),
    _CienaCesChassisXcvrHealthMaxMeasurement_Type()
)
cienaCesChassisXcvrHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthMaxMeasurement.setStatus("current")
_CienaCesChassisXcvrHealthMinThreshold_Type = Unsigned32
_CienaCesChassisXcvrHealthMinThreshold_Object = MibTableColumn
cienaCesChassisXcvrHealthMinThreshold = _CienaCesChassisXcvrHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 7),
    _CienaCesChassisXcvrHealthMinThreshold_Type()
)
cienaCesChassisXcvrHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthMinThreshold.setStatus("current")
_CienaCesChassisXcvrHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisXcvrHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisXcvrHealthMaxThreshold = _CienaCesChassisXcvrHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 8),
    _CienaCesChassisXcvrHealthMaxThreshold_Type()
)
cienaCesChassisXcvrHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthMaxThreshold.setStatus("current")


class _CienaCesChassisXcvrHealthUnit_Type(Integer32):
    """Custom type cienaCesChassisXcvrHealthUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deg-C", 1),
          ("milli-watts", 2))
    )


_CienaCesChassisXcvrHealthUnit_Type.__name__ = "Integer32"
_CienaCesChassisXcvrHealthUnit_Object = MibTableColumn
cienaCesChassisXcvrHealthUnit = _CienaCesChassisXcvrHealthUnit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 28, 1, 9),
    _CienaCesChassisXcvrHealthUnit_Type()
)
cienaCesChassisXcvrHealthUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisXcvrHealthUnit.setStatus("current")
_CienaCesChassisPortLinkHealthTable_Object = MibTable
cienaCesChassisPortLinkHealthTable = _CienaCesChassisPortLinkHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 29)
)
if mibBuilder.loadTexts:
    cienaCesChassisPortLinkHealthTable.setStatus("current")
_CienaCesChassisPortLinkHealthEntry_Object = MibTableRow
cienaCesChassisPortLinkHealthEntry = _CienaCesChassisPortLinkHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 29, 1)
)
cienaCesChassisPortLinkHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPortLinkHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPortLinkHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisPortLinkHealthEntry.setStatus("current")


class _CienaCesChassisPortLinkHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisPortLinkHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("portLink-State", 1))
    )


_CienaCesChassisPortLinkHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisPortLinkHealthSubCategory_Object = MibTableColumn
cienaCesChassisPortLinkHealthSubCategory = _CienaCesChassisPortLinkHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 29, 1, 1),
    _CienaCesChassisPortLinkHealthSubCategory_Type()
)
cienaCesChassisPortLinkHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPortLinkHealthSubCategory.setStatus("current")
_CienaCesChassisPortLinkHealthOriginIndex_Type = Unsigned32
_CienaCesChassisPortLinkHealthOriginIndex_Object = MibTableColumn
cienaCesChassisPortLinkHealthOriginIndex = _CienaCesChassisPortLinkHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 29, 1, 2),
    _CienaCesChassisPortLinkHealthOriginIndex_Type()
)
cienaCesChassisPortLinkHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPortLinkHealthOriginIndex.setStatus("current")
_CienaCesChassisPortLinkHealthState_Type = TceHealthStatus
_CienaCesChassisPortLinkHealthState_Object = MibTableColumn
cienaCesChassisPortLinkHealthState = _CienaCesChassisPortLinkHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 29, 1, 3),
    _CienaCesChassisPortLinkHealthState_Type()
)
cienaCesChassisPortLinkHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPortLinkHealthState.setStatus("current")
_CienaCesChassisIOMStatusHealthTable_Object = MibTable
cienaCesChassisIOMStatusHealthTable = _CienaCesChassisIOMStatusHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 30)
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMStatusHealthTable.setStatus("current")
_CienaCesChassisIOMStatusHealthEntry_Object = MibTableRow
cienaCesChassisIOMStatusHealthEntry = _CienaCesChassisIOMStatusHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 30, 1)
)
cienaCesChassisIOMStatusHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMStatusHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMStatusHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMStatusHealthEntry.setStatus("current")


class _CienaCesChassisIOMStatusHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisIOMStatusHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("state", 1))
    )


_CienaCesChassisIOMStatusHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisIOMStatusHealthSubCategory_Object = MibTableColumn
cienaCesChassisIOMStatusHealthSubCategory = _CienaCesChassisIOMStatusHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 30, 1, 1),
    _CienaCesChassisIOMStatusHealthSubCategory_Type()
)
cienaCesChassisIOMStatusHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIOMStatusHealthSubCategory.setStatus("current")
_CienaCesChassisIOMStatusHealthOriginIndex_Type = Unsigned32
_CienaCesChassisIOMStatusHealthOriginIndex_Object = MibTableColumn
cienaCesChassisIOMStatusHealthOriginIndex = _CienaCesChassisIOMStatusHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 30, 1, 2),
    _CienaCesChassisIOMStatusHealthOriginIndex_Type()
)
cienaCesChassisIOMStatusHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIOMStatusHealthOriginIndex.setStatus("current")
_CienaCesChassisIOMStatusHealthState_Type = TceHealthStatus
_CienaCesChassisIOMStatusHealthState_Object = MibTableColumn
cienaCesChassisIOMStatusHealthState = _CienaCesChassisIOMStatusHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 30, 1, 3),
    _CienaCesChassisIOMStatusHealthState_Type()
)
cienaCesChassisIOMStatusHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMStatusHealthState.setStatus("current")
_CienaCesChassisLinxStatHealthTable_Object = MibTable
cienaCesChassisLinxStatHealthTable = _CienaCesChassisLinxStatHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31)
)
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthTable.setStatus("current")
_CienaCesChassisLinxStatHealthEntry_Object = MibTableRow
cienaCesChassisLinxStatHealthEntry = _CienaCesChassisLinxStatHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1)
)
cienaCesChassisLinxStatHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisLinxStatHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisLinxStatHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthEntry.setStatus("current")


class _CienaCesChassisLinxStatHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisLinxStatHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timers", 1),
          ("attachments", 2))
    )


_CienaCesChassisLinxStatHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisLinxStatHealthSubCategory_Object = MibTableColumn
cienaCesChassisLinxStatHealthSubCategory = _CienaCesChassisLinxStatHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 1),
    _CienaCesChassisLinxStatHealthSubCategory_Type()
)
cienaCesChassisLinxStatHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthSubCategory.setStatus("current")
_CienaCesChassisLinxStatHealthOriginIndex_Type = Unsigned32
_CienaCesChassisLinxStatHealthOriginIndex_Object = MibTableColumn
cienaCesChassisLinxStatHealthOriginIndex = _CienaCesChassisLinxStatHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 2),
    _CienaCesChassisLinxStatHealthOriginIndex_Type()
)
cienaCesChassisLinxStatHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthOriginIndex.setStatus("current")
_CienaCesChassisLinxStatHealthState_Type = TceHealthStatus
_CienaCesChassisLinxStatHealthState_Object = MibTableColumn
cienaCesChassisLinxStatHealthState = _CienaCesChassisLinxStatHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 3),
    _CienaCesChassisLinxStatHealthState_Type()
)
cienaCesChassisLinxStatHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthState.setStatus("current")
_CienaCesChassisLinxStatHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisLinxStatHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisLinxStatHealthCurrMeasurement = _CienaCesChassisLinxStatHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 4),
    _CienaCesChassisLinxStatHealthCurrMeasurement_Type()
)
cienaCesChassisLinxStatHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthCurrMeasurement.setStatus("current")
_CienaCesChassisLinxStatHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisLinxStatHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisLinxStatHealthMaxMeasurement = _CienaCesChassisLinxStatHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 5),
    _CienaCesChassisLinxStatHealthMaxMeasurement_Type()
)
cienaCesChassisLinxStatHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthMaxMeasurement.setStatus("current")
_CienaCesChassisLinxStatHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisLinxStatHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisLinxStatHealthMaxThreshold = _CienaCesChassisLinxStatHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 31, 1, 6),
    _CienaCesChassisLinxStatHealthMaxThreshold_Type()
)
cienaCesChassisLinxStatHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisLinxStatHealthMaxThreshold.setStatus("current")
_CienaCesChassisSMFabricHealthTable_Object = MibTable
cienaCesChassisSMFabricHealthTable = _CienaCesChassisSMFabricHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 32)
)
if mibBuilder.loadTexts:
    cienaCesChassisSMFabricHealthTable.setStatus("current")
_CienaCesChassisSMFabricHealthEntry_Object = MibTableRow
cienaCesChassisSMFabricHealthEntry = _CienaCesChassisSMFabricHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 32, 1)
)
cienaCesChassisSMFabricHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMFabricHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSMFabricHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisSMFabricHealthEntry.setStatus("current")


class _CienaCesChassisSMFabricHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisSMFabricHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("status", 1))
    )


_CienaCesChassisSMFabricHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisSMFabricHealthSubCategory_Object = MibTableColumn
cienaCesChassisSMFabricHealthSubCategory = _CienaCesChassisSMFabricHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 32, 1, 1),
    _CienaCesChassisSMFabricHealthSubCategory_Type()
)
cienaCesChassisSMFabricHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMFabricHealthSubCategory.setStatus("current")
_CienaCesChassisSMFabricHealthOriginIndex_Type = Unsigned32
_CienaCesChassisSMFabricHealthOriginIndex_Object = MibTableColumn
cienaCesChassisSMFabricHealthOriginIndex = _CienaCesChassisSMFabricHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 32, 1, 2),
    _CienaCesChassisSMFabricHealthOriginIndex_Type()
)
cienaCesChassisSMFabricHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSMFabricHealthOriginIndex.setStatus("current")
_CienaCesChassisSMFabricHealthState_Type = TceHealthStatus
_CienaCesChassisSMFabricHealthState_Object = MibTableColumn
cienaCesChassisSMFabricHealthState = _CienaCesChassisSMFabricHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 32, 1, 3),
    _CienaCesChassisSMFabricHealthState_Type()
)
cienaCesChassisSMFabricHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSMFabricHealthState.setStatus("current")
_CienaCesChassisSPIHealthTable_Object = MibTable
cienaCesChassisSPIHealthTable = _CienaCesChassisSPIHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 33)
)
if mibBuilder.loadTexts:
    cienaCesChassisSPIHealthTable.setStatus("current")
_CienaCesChassisSPIHealthEntry_Object = MibTableRow
cienaCesChassisSPIHealthEntry = _CienaCesChassisSPIHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 33, 1)
)
cienaCesChassisSPIHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSPIHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisSPIHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisSPIHealthEntry.setStatus("current")


class _CienaCesChassisSPIHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisSPIHealthSubCategory based on Integer32"""
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
          ("cfu1", 1),
          ("cfu2", 2),
          ("iom", 3))
    )


_CienaCesChassisSPIHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisSPIHealthSubCategory_Object = MibTableColumn
cienaCesChassisSPIHealthSubCategory = _CienaCesChassisSPIHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 33, 1, 1),
    _CienaCesChassisSPIHealthSubCategory_Type()
)
cienaCesChassisSPIHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSPIHealthSubCategory.setStatus("current")
_CienaCesChassisSPIHealthOriginIndex_Type = Unsigned32
_CienaCesChassisSPIHealthOriginIndex_Object = MibTableColumn
cienaCesChassisSPIHealthOriginIndex = _CienaCesChassisSPIHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 33, 1, 3),
    _CienaCesChassisSPIHealthOriginIndex_Type()
)
cienaCesChassisSPIHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisSPIHealthOriginIndex.setStatus("current")
_CienaCesChassisSPIHealthState_Type = TceHealthStatus
_CienaCesChassisSPIHealthState_Object = MibTableColumn
cienaCesChassisSPIHealthState = _CienaCesChassisSPIHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 33, 1, 4),
    _CienaCesChassisSPIHealthState_Type()
)
cienaCesChassisSPIHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSPIHealthState.setStatus("current")
_CienaCesChassisUsbFlashHealthTable_Object = MibTable
cienaCesChassisUsbFlashHealthTable = _CienaCesChassisUsbFlashHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 34)
)
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashHealthTable.setStatus("current")
_CienaCesChassisUsbFlashHealthEntry_Object = MibTableRow
cienaCesChassisUsbFlashHealthEntry = _CienaCesChassisUsbFlashHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 34, 1)
)
cienaCesChassisUsbFlashHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisUsbFlashHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisUsbFlashHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashHealthEntry.setStatus("current")


class _CienaCesChassisUsbFlashHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisUsbFlashHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("devicePresent", 1))
    )


_CienaCesChassisUsbFlashHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisUsbFlashHealthSubCategory_Object = MibTableColumn
cienaCesChassisUsbFlashHealthSubCategory = _CienaCesChassisUsbFlashHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 34, 1, 1),
    _CienaCesChassisUsbFlashHealthSubCategory_Type()
)
cienaCesChassisUsbFlashHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashHealthSubCategory.setStatus("current")
_CienaCesChassisUsbFlashHealthOriginIndex_Type = Unsigned32
_CienaCesChassisUsbFlashHealthOriginIndex_Object = MibTableColumn
cienaCesChassisUsbFlashHealthOriginIndex = _CienaCesChassisUsbFlashHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 34, 1, 3),
    _CienaCesChassisUsbFlashHealthOriginIndex_Type()
)
cienaCesChassisUsbFlashHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashHealthOriginIndex.setStatus("current")
_CienaCesChassisUsbFlashHealthState_Type = TceHealthStatus
_CienaCesChassisUsbFlashHealthState_Object = MibTableColumn
cienaCesChassisUsbFlashHealthState = _CienaCesChassisUsbFlashHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 34, 1, 4),
    _CienaCesChassisUsbFlashHealthState_Type()
)
cienaCesChassisUsbFlashHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashHealthState.setStatus("current")
_CienaCesChassisIomTempHealthTable_Object = MibTable
cienaCesChassisIomTempHealthTable = _CienaCesChassisIomTempHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35)
)
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthTable.setStatus("current")
_CienaCesChassisIomTempHealthEntry_Object = MibTableRow
cienaCesChassisIomTempHealthEntry = _CienaCesChassisIomTempHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1)
)
cienaCesChassisIomTempHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIomTempHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIomTempHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthEntry.setStatus("current")


class _CienaCesChassisIomTempHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisIomTempHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("temperature", 1))
    )


_CienaCesChassisIomTempHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisIomTempHealthSubCategory_Object = MibTableColumn
cienaCesChassisIomTempHealthSubCategory = _CienaCesChassisIomTempHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 1),
    _CienaCesChassisIomTempHealthSubCategory_Type()
)
cienaCesChassisIomTempHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthSubCategory.setStatus("current")
_CienaCesChassisIomTempHealthOriginIndex_Type = Unsigned32
_CienaCesChassisIomTempHealthOriginIndex_Object = MibTableColumn
cienaCesChassisIomTempHealthOriginIndex = _CienaCesChassisIomTempHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 2),
    _CienaCesChassisIomTempHealthOriginIndex_Type()
)
cienaCesChassisIomTempHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthOriginIndex.setStatus("current")
_CienaCesChassisIomTempHealthState_Type = TceHealthStatus
_CienaCesChassisIomTempHealthState_Object = MibTableColumn
cienaCesChassisIomTempHealthState = _CienaCesChassisIomTempHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 3),
    _CienaCesChassisIomTempHealthState_Type()
)
cienaCesChassisIomTempHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthState.setStatus("current")
_CienaCesChassisIomTempHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisIomTempHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisIomTempHealthCurrMeasurement = _CienaCesChassisIomTempHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 4),
    _CienaCesChassisIomTempHealthCurrMeasurement_Type()
)
cienaCesChassisIomTempHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthCurrMeasurement.setUnits("deg C")
_CienaCesChassisIomTempHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisIomTempHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisIomTempHealthMinMeasurement = _CienaCesChassisIomTempHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 5),
    _CienaCesChassisIomTempHealthMinMeasurement_Type()
)
cienaCesChassisIomTempHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMinMeasurement.setUnits("deg C")
_CienaCesChassisIomTempHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisIomTempHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisIomTempHealthMaxMeasurement = _CienaCesChassisIomTempHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 6),
    _CienaCesChassisIomTempHealthMaxMeasurement_Type()
)
cienaCesChassisIomTempHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMaxMeasurement.setUnits("deg C")
_CienaCesChassisIomTempHealthMinThreshold_Type = Unsigned32
_CienaCesChassisIomTempHealthMinThreshold_Object = MibTableColumn
cienaCesChassisIomTempHealthMinThreshold = _CienaCesChassisIomTempHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 7),
    _CienaCesChassisIomTempHealthMinThreshold_Type()
)
cienaCesChassisIomTempHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMinThreshold.setUnits("deg C")
_CienaCesChassisIomTempHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisIomTempHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisIomTempHealthMaxThreshold = _CienaCesChassisIomTempHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 35, 1, 8),
    _CienaCesChassisIomTempHealthMaxThreshold_Type()
)
cienaCesChassisIomTempHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisIomTempHealthMaxThreshold.setUnits("deg C")
_CienaCesChassisPowerParamsHealthTable_Object = MibTable
cienaCesChassisPowerParamsHealthTable = _CienaCesChassisPowerParamsHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 36)
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerParamsHealthTable.setStatus("current")
_CienaCesChassisPowerParamsHealthEntry_Object = MibTableRow
cienaCesChassisPowerParamsHealthEntry = _CienaCesChassisPowerParamsHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 36, 1)
)
cienaCesChassisPowerParamsHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerParamsHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerParamsHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerParamsHealthEntry.setStatus("current")


class _CienaCesChassisPowerParamsHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisPowerParamsHealthSubCategory based on Integer32"""
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
          ("loadFuse", 1),
          ("internalFuse", 2),
          ("voltageRegulator", 3),
          ("temperature", 4),
          ("acInput", 5),
          ("overloadProtection", 6),
          ("fan", 7))
    )


_CienaCesChassisPowerParamsHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisPowerParamsHealthSubCategory_Object = MibTableColumn
cienaCesChassisPowerParamsHealthSubCategory = _CienaCesChassisPowerParamsHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 36, 1, 1),
    _CienaCesChassisPowerParamsHealthSubCategory_Type()
)
cienaCesChassisPowerParamsHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerParamsHealthSubCategory.setStatus("current")
_CienaCesChassisPowerParamsHealthOriginIndex_Type = Unsigned32
_CienaCesChassisPowerParamsHealthOriginIndex_Object = MibTableColumn
cienaCesChassisPowerParamsHealthOriginIndex = _CienaCesChassisPowerParamsHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 36, 1, 2),
    _CienaCesChassisPowerParamsHealthOriginIndex_Type()
)
cienaCesChassisPowerParamsHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerParamsHealthOriginIndex.setStatus("current")
_CienaCesChassisPowerParamsHealthState_Type = TceHealthStatus
_CienaCesChassisPowerParamsHealthState_Object = MibTableColumn
cienaCesChassisPowerParamsHealthState = _CienaCesChassisPowerParamsHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 36, 1, 3),
    _CienaCesChassisPowerParamsHealthState_Type()
)
cienaCesChassisPowerParamsHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerParamsHealthState.setStatus("current")
_CienaCesChassisPowerOutputVoltageHealthTable_Object = MibTable
cienaCesChassisPowerOutputVoltageHealthTable = _CienaCesChassisPowerOutputVoltageHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37)
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthTable.setStatus("current")
_CienaCesChassisPowerOutputVoltageHealthEntry_Object = MibTableRow
cienaCesChassisPowerOutputVoltageHealthEntry = _CienaCesChassisPowerOutputVoltageHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1)
)
cienaCesChassisPowerOutputVoltageHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerOutputVoltageHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerOutputVoltageHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthEntry.setStatus("current")


class _CienaCesChassisPowerOutputVoltageHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisPowerOutputVoltageHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("voltage", 1))
    )


_CienaCesChassisPowerOutputVoltageHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisPowerOutputVoltageHealthSubCategory_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthSubCategory = _CienaCesChassisPowerOutputVoltageHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 1),
    _CienaCesChassisPowerOutputVoltageHealthSubCategory_Type()
)
cienaCesChassisPowerOutputVoltageHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthSubCategory.setStatus("current")
_CienaCesChassisPowerOutputVoltageHealthOriginIndex_Type = Unsigned32
_CienaCesChassisPowerOutputVoltageHealthOriginIndex_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthOriginIndex = _CienaCesChassisPowerOutputVoltageHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 2),
    _CienaCesChassisPowerOutputVoltageHealthOriginIndex_Type()
)
cienaCesChassisPowerOutputVoltageHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthOriginIndex.setStatus("current")
_CienaCesChassisPowerOutputVoltageHealthState_Type = TceHealthStatus
_CienaCesChassisPowerOutputVoltageHealthState_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthState = _CienaCesChassisPowerOutputVoltageHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 3),
    _CienaCesChassisPowerOutputVoltageHealthState_Type()
)
cienaCesChassisPowerOutputVoltageHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthState.setStatus("current")
_CienaCesChassisPowerOutputVoltageHealthCurrMeasurement_Type = Integer32
_CienaCesChassisPowerOutputVoltageHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthCurrMeasurement = _CienaCesChassisPowerOutputVoltageHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 4),
    _CienaCesChassisPowerOutputVoltageHealthCurrMeasurement_Type()
)
cienaCesChassisPowerOutputVoltageHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthCurrMeasurement.setUnits("mV")
_CienaCesChassisPowerOutputVoltageHealthMinMeasurement_Type = Integer32
_CienaCesChassisPowerOutputVoltageHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthMinMeasurement = _CienaCesChassisPowerOutputVoltageHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 5),
    _CienaCesChassisPowerOutputVoltageHealthMinMeasurement_Type()
)
cienaCesChassisPowerOutputVoltageHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMinMeasurement.setUnits("mV")
_CienaCesChassisPowerOutputVoltageHealthMaxMeasurement_Type = Integer32
_CienaCesChassisPowerOutputVoltageHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthMaxMeasurement = _CienaCesChassisPowerOutputVoltageHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 6),
    _CienaCesChassisPowerOutputVoltageHealthMaxMeasurement_Type()
)
cienaCesChassisPowerOutputVoltageHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMaxMeasurement.setUnits("mV")
_CienaCesChassisPowerOutputVoltageHealthMinThreshold_Type = Integer32
_CienaCesChassisPowerOutputVoltageHealthMinThreshold_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthMinThreshold = _CienaCesChassisPowerOutputVoltageHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 7),
    _CienaCesChassisPowerOutputVoltageHealthMinThreshold_Type()
)
cienaCesChassisPowerOutputVoltageHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMinThreshold.setUnits("mV")
_CienaCesChassisPowerOutputVoltageHealthMaxThreshold_Type = Integer32
_CienaCesChassisPowerOutputVoltageHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisPowerOutputVoltageHealthMaxThreshold = _CienaCesChassisPowerOutputVoltageHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 37, 1, 8),
    _CienaCesChassisPowerOutputVoltageHealthMaxThreshold_Type()
)
cienaCesChassisPowerOutputVoltageHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisPowerOutputVoltageHealthMaxThreshold.setUnits("mV")
_CienaCesChassisModemTempHealthTable_Object = MibTable
cienaCesChassisModemTempHealthTable = _CienaCesChassisModemTempHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38)
)
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthTable.setStatus("current")
_CienaCesChassisModemTempHealthEntry_Object = MibTableRow
cienaCesChassisModemTempHealthEntry = _CienaCesChassisModemTempHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1)
)
cienaCesChassisModemTempHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModemTempHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModemTempHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthEntry.setStatus("current")


class _CienaCesChassisModemTempHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisModemTempHealthSubCategory based on Integer32"""
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
          ("sensor1", 1),
          ("sensor2", 2),
          ("sensor3", 3),
          ("sensor4", 4),
          ("sensor5", 5))
    )


_CienaCesChassisModemTempHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisModemTempHealthSubCategory_Object = MibTableColumn
cienaCesChassisModemTempHealthSubCategory = _CienaCesChassisModemTempHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 1),
    _CienaCesChassisModemTempHealthSubCategory_Type()
)
cienaCesChassisModemTempHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthSubCategory.setStatus("current")
_CienaCesChassisModemTempHealthOriginIndex_Type = Unsigned32
_CienaCesChassisModemTempHealthOriginIndex_Object = MibTableColumn
cienaCesChassisModemTempHealthOriginIndex = _CienaCesChassisModemTempHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 2),
    _CienaCesChassisModemTempHealthOriginIndex_Type()
)
cienaCesChassisModemTempHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthOriginIndex.setStatus("current")
_CienaCesChassisModemTempHealthState_Type = TceHealthStatus
_CienaCesChassisModemTempHealthState_Object = MibTableColumn
cienaCesChassisModemTempHealthState = _CienaCesChassisModemTempHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 3),
    _CienaCesChassisModemTempHealthState_Type()
)
cienaCesChassisModemTempHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthState.setStatus("current")
_CienaCesChassisModemTempHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisModemTempHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisModemTempHealthCurrMeasurement = _CienaCesChassisModemTempHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 4),
    _CienaCesChassisModemTempHealthCurrMeasurement_Type()
)
cienaCesChassisModemTempHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthCurrMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthCurrMeasurement.setUnits("deg C")
_CienaCesChassisModemTempHealthMinMeasurement_Type = Unsigned32
_CienaCesChassisModemTempHealthMinMeasurement_Object = MibTableColumn
cienaCesChassisModemTempHealthMinMeasurement = _CienaCesChassisModemTempHealthMinMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 5),
    _CienaCesChassisModemTempHealthMinMeasurement_Type()
)
cienaCesChassisModemTempHealthMinMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMinMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMinMeasurement.setUnits("deg C")
_CienaCesChassisModemTempHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisModemTempHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisModemTempHealthMaxMeasurement = _CienaCesChassisModemTempHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 6),
    _CienaCesChassisModemTempHealthMaxMeasurement_Type()
)
cienaCesChassisModemTempHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMaxMeasurement.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMaxMeasurement.setUnits("deg C")
_CienaCesChassisModemTempHealthMinThreshold_Type = Unsigned32
_CienaCesChassisModemTempHealthMinThreshold_Object = MibTableColumn
cienaCesChassisModemTempHealthMinThreshold = _CienaCesChassisModemTempHealthMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 7),
    _CienaCesChassisModemTempHealthMinThreshold_Type()
)
cienaCesChassisModemTempHealthMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMinThreshold.setUnits("deg C")
_CienaCesChassisModemTempHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisModemTempHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisModemTempHealthMaxThreshold = _CienaCesChassisModemTempHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 38, 1, 8),
    _CienaCesChassisModemTempHealthMaxThreshold_Type()
)
cienaCesChassisModemTempHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesChassisModemTempHealthMaxThreshold.setUnits("deg C")
_CienaCesChassisModemWatermarkHealthTable_Object = MibTable
cienaCesChassisModemWatermarkHealthTable = _CienaCesChassisModemWatermarkHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 39)
)
if mibBuilder.loadTexts:
    cienaCesChassisModemWatermarkHealthTable.setStatus("current")
_CienaCesChassisModemWatermarkHealthEntry_Object = MibTableRow
cienaCesChassisModemWatermarkHealthEntry = _CienaCesChassisModemWatermarkHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 39, 1)
)
cienaCesChassisModemWatermarkHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModemWatermarkHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisModemWatermarkHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisModemWatermarkHealthEntry.setStatus("current")


class _CienaCesChassisModemWatermarkHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisModemWatermarkHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("watermark", 1))
    )


_CienaCesChassisModemWatermarkHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisModemWatermarkHealthSubCategory_Object = MibTableColumn
cienaCesChassisModemWatermarkHealthSubCategory = _CienaCesChassisModemWatermarkHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 39, 1, 1),
    _CienaCesChassisModemWatermarkHealthSubCategory_Type()
)
cienaCesChassisModemWatermarkHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModemWatermarkHealthSubCategory.setStatus("current")
_CienaCesChassisModemWatermarkHealthOriginIndex_Type = Unsigned32
_CienaCesChassisModemWatermarkHealthOriginIndex_Object = MibTableColumn
cienaCesChassisModemWatermarkHealthOriginIndex = _CienaCesChassisModemWatermarkHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 39, 1, 2),
    _CienaCesChassisModemWatermarkHealthOriginIndex_Type()
)
cienaCesChassisModemWatermarkHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisModemWatermarkHealthOriginIndex.setStatus("current")
_CienaCesChassisModemWatermarkHealthState_Type = TceHealthStatus
_CienaCesChassisModemWatermarkHealthState_Object = MibTableColumn
cienaCesChassisModemWatermarkHealthState = _CienaCesChassisModemWatermarkHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 39, 1, 3),
    _CienaCesChassisModemWatermarkHealthState_Type()
)
cienaCesChassisModemWatermarkHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisModemWatermarkHealthState.setStatus("current")
_CienaCesChassisFileDescriptorHealthTable_Object = MibTable
cienaCesChassisFileDescriptorHealthTable = _CienaCesChassisFileDescriptorHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40)
)
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthTable.setStatus("current")
_CienaCesChassisFileDescriptorHealthEntry_Object = MibTableRow
cienaCesChassisFileDescriptorHealthEntry = _CienaCesChassisFileDescriptorHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1)
)
cienaCesChassisFileDescriptorHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFileDescriptorHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisFileDescriptorHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthEntry.setStatus("current")


class _CienaCesChassisFileDescriptorHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisFileDescriptorHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("saos", 1))
    )


_CienaCesChassisFileDescriptorHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisFileDescriptorHealthSubCategory_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthSubCategory = _CienaCesChassisFileDescriptorHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 1),
    _CienaCesChassisFileDescriptorHealthSubCategory_Type()
)
cienaCesChassisFileDescriptorHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthSubCategory.setStatus("current")
_CienaCesChassisFileDescriptorHealthOriginIndex_Type = Unsigned32
_CienaCesChassisFileDescriptorHealthOriginIndex_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthOriginIndex = _CienaCesChassisFileDescriptorHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 2),
    _CienaCesChassisFileDescriptorHealthOriginIndex_Type()
)
cienaCesChassisFileDescriptorHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthOriginIndex.setStatus("current")
_CienaCesChassisFileDescriptorHealthState_Type = TceHealthStatus
_CienaCesChassisFileDescriptorHealthState_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthState = _CienaCesChassisFileDescriptorHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 3),
    _CienaCesChassisFileDescriptorHealthState_Type()
)
cienaCesChassisFileDescriptorHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthState.setStatus("current")
_CienaCesChassisFileDescriptorHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisFileDescriptorHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthCurrMeasurement = _CienaCesChassisFileDescriptorHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 4),
    _CienaCesChassisFileDescriptorHealthCurrMeasurement_Type()
)
cienaCesChassisFileDescriptorHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthCurrMeasurement.setStatus("current")
_CienaCesChassisFileDescriptorHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisFileDescriptorHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthMaxMeasurement = _CienaCesChassisFileDescriptorHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 5),
    _CienaCesChassisFileDescriptorHealthMaxMeasurement_Type()
)
cienaCesChassisFileDescriptorHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthMaxMeasurement.setStatus("current")
_CienaCesChassisFileDescriptorHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisFileDescriptorHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisFileDescriptorHealthMaxThreshold = _CienaCesChassisFileDescriptorHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 40, 1, 6),
    _CienaCesChassisFileDescriptorHealthMaxThreshold_Type()
)
cienaCesChassisFileDescriptorHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFileDescriptorHealthMaxThreshold.setStatus("current")
_CienaCesChassisProcessHealthTable_Object = MibTable
cienaCesChassisProcessHealthTable = _CienaCesChassisProcessHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41)
)
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthTable.setStatus("current")
_CienaCesChassisProcessHealthEntry_Object = MibTableRow
cienaCesChassisProcessHealthEntry = _CienaCesChassisProcessHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1)
)
cienaCesChassisProcessHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisProcessHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisProcessHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthEntry.setStatus("current")


class _CienaCesChassisProcessHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisProcessHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("linux", 1))
    )


_CienaCesChassisProcessHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisProcessHealthSubCategory_Object = MibTableColumn
cienaCesChassisProcessHealthSubCategory = _CienaCesChassisProcessHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 1),
    _CienaCesChassisProcessHealthSubCategory_Type()
)
cienaCesChassisProcessHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthSubCategory.setStatus("current")
_CienaCesChassisProcessHealthOriginIndex_Type = Unsigned32
_CienaCesChassisProcessHealthOriginIndex_Object = MibTableColumn
cienaCesChassisProcessHealthOriginIndex = _CienaCesChassisProcessHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 2),
    _CienaCesChassisProcessHealthOriginIndex_Type()
)
cienaCesChassisProcessHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthOriginIndex.setStatus("current")
_CienaCesChassisProcessHealthState_Type = TceHealthStatus
_CienaCesChassisProcessHealthState_Object = MibTableColumn
cienaCesChassisProcessHealthState = _CienaCesChassisProcessHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 3),
    _CienaCesChassisProcessHealthState_Type()
)
cienaCesChassisProcessHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthState.setStatus("current")
_CienaCesChassisProcessHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisProcessHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisProcessHealthCurrMeasurement = _CienaCesChassisProcessHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 4),
    _CienaCesChassisProcessHealthCurrMeasurement_Type()
)
cienaCesChassisProcessHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthCurrMeasurement.setStatus("current")
_CienaCesChassisProcessHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisProcessHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisProcessHealthMaxMeasurement = _CienaCesChassisProcessHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 5),
    _CienaCesChassisProcessHealthMaxMeasurement_Type()
)
cienaCesChassisProcessHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthMaxMeasurement.setStatus("current")
_CienaCesChassisProcessHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisProcessHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisProcessHealthMaxThreshold = _CienaCesChassisProcessHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 41, 1, 6),
    _CienaCesChassisProcessHealthMaxThreshold_Type()
)
cienaCesChassisProcessHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisProcessHealthMaxThreshold.setStatus("current")
_CienaCesChassisThreadHealthTable_Object = MibTable
cienaCesChassisThreadHealthTable = _CienaCesChassisThreadHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42)
)
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthTable.setStatus("current")
_CienaCesChassisThreadHealthEntry_Object = MibTableRow
cienaCesChassisThreadHealthEntry = _CienaCesChassisThreadHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1)
)
cienaCesChassisThreadHealthEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisThreadHealthSubCategory"),
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisThreadHealthOriginIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthEntry.setStatus("current")


class _CienaCesChassisThreadHealthSubCategory_Type(Integer32):
    """Custom type cienaCesChassisThreadHealthSubCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("saos", 1))
    )


_CienaCesChassisThreadHealthSubCategory_Type.__name__ = "Integer32"
_CienaCesChassisThreadHealthSubCategory_Object = MibTableColumn
cienaCesChassisThreadHealthSubCategory = _CienaCesChassisThreadHealthSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 1),
    _CienaCesChassisThreadHealthSubCategory_Type()
)
cienaCesChassisThreadHealthSubCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthSubCategory.setStatus("current")
_CienaCesChassisThreadHealthOriginIndex_Type = Unsigned32
_CienaCesChassisThreadHealthOriginIndex_Object = MibTableColumn
cienaCesChassisThreadHealthOriginIndex = _CienaCesChassisThreadHealthOriginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 2),
    _CienaCesChassisThreadHealthOriginIndex_Type()
)
cienaCesChassisThreadHealthOriginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthOriginIndex.setStatus("current")
_CienaCesChassisThreadHealthState_Type = TceHealthStatus
_CienaCesChassisThreadHealthState_Object = MibTableColumn
cienaCesChassisThreadHealthState = _CienaCesChassisThreadHealthState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 3),
    _CienaCesChassisThreadHealthState_Type()
)
cienaCesChassisThreadHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthState.setStatus("current")
_CienaCesChassisThreadHealthCurrMeasurement_Type = Unsigned32
_CienaCesChassisThreadHealthCurrMeasurement_Object = MibTableColumn
cienaCesChassisThreadHealthCurrMeasurement = _CienaCesChassisThreadHealthCurrMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 4),
    _CienaCesChassisThreadHealthCurrMeasurement_Type()
)
cienaCesChassisThreadHealthCurrMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthCurrMeasurement.setStatus("current")
_CienaCesChassisThreadHealthMaxMeasurement_Type = Unsigned32
_CienaCesChassisThreadHealthMaxMeasurement_Object = MibTableColumn
cienaCesChassisThreadHealthMaxMeasurement = _CienaCesChassisThreadHealthMaxMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 5),
    _CienaCesChassisThreadHealthMaxMeasurement_Type()
)
cienaCesChassisThreadHealthMaxMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthMaxMeasurement.setStatus("current")
_CienaCesChassisThreadHealthMaxThreshold_Type = Unsigned32
_CienaCesChassisThreadHealthMaxThreshold_Object = MibTableColumn
cienaCesChassisThreadHealthMaxThreshold = _CienaCesChassisThreadHealthMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 4, 42, 1, 6),
    _CienaCesChassisThreadHealthMaxThreshold_Type()
)
cienaCesChassisThreadHealthMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisThreadHealthMaxThreshold.setStatus("current")
_CienaCesChassisIDP_ObjectIdentity = ObjectIdentity
cienaCesChassisIDP = _CienaCesChassisIDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5)
)
_CienaCesChassisIDPEthBaseMac_Type = MacAddress
_CienaCesChassisIDPEthBaseMac_Object = MibScalar
cienaCesChassisIDPEthBaseMac = _CienaCesChassisIDPEthBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 1),
    _CienaCesChassisIDPEthBaseMac_Type()
)
cienaCesChassisIDPEthBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPEthBaseMac.setStatus("current")
_CienaCesChassisIDPEthBaseMacRange_Type = Integer32
_CienaCesChassisIDPEthBaseMacRange_Object = MibScalar
cienaCesChassisIDPEthBaseMacRange = _CienaCesChassisIDPEthBaseMacRange_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 2),
    _CienaCesChassisIDPEthBaseMacRange_Type()
)
cienaCesChassisIDPEthBaseMacRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPEthBaseMacRange.setStatus("current")
_CienaCesChassisIDPModuleSerialNumber_Type = DisplayString
_CienaCesChassisIDPModuleSerialNumber_Object = MibScalar
cienaCesChassisIDPModuleSerialNumber = _CienaCesChassisIDPModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 3),
    _CienaCesChassisIDPModuleSerialNumber_Type()
)
cienaCesChassisIDPModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPModuleSerialNumber.setStatus("current")
_CienaCesChassisIDPModelPartNumber_Type = DisplayString
_CienaCesChassisIDPModelPartNumber_Object = MibScalar
cienaCesChassisIDPModelPartNumber = _CienaCesChassisIDPModelPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 4),
    _CienaCesChassisIDPModelPartNumber_Type()
)
cienaCesChassisIDPModelPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPModelPartNumber.setStatus("current")
_CienaCesChassisIDPModelRevision_Type = DisplayString
_CienaCesChassisIDPModelRevision_Object = MibScalar
cienaCesChassisIDPModelRevision = _CienaCesChassisIDPModelRevision_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 5),
    _CienaCesChassisIDPModelRevision_Type()
)
cienaCesChassisIDPModelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPModelRevision.setStatus("current")
_CienaCesChassisIDPProductID_Type = DisplayString
_CienaCesChassisIDPProductID_Object = MibScalar
cienaCesChassisIDPProductID = _CienaCesChassisIDPProductID_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 6),
    _CienaCesChassisIDPProductID_Type()
)
cienaCesChassisIDPProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPProductID.setStatus("current")
_CienaCesChassisIDPMfgDate_Type = DisplayString
_CienaCesChassisIDPMfgDate_Object = MibScalar
cienaCesChassisIDPMfgDate = _CienaCesChassisIDPMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 7),
    _CienaCesChassisIDPMfgDate_Type()
)
cienaCesChassisIDPMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPMfgDate.setStatus("current")
_CienaCesChassisIDPCleiCode_Type = DisplayString
_CienaCesChassisIDPCleiCode_Object = MibScalar
cienaCesChassisIDPCleiCode = _CienaCesChassisIDPCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 8),
    _CienaCesChassisIDPCleiCode_Type()
)
cienaCesChassisIDPCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPCleiCode.setStatus("current")
_CienaCesChassisIDPBarcode_Type = DisplayString
_CienaCesChassisIDPBarcode_Object = MibScalar
cienaCesChassisIDPBarcode = _CienaCesChassisIDPBarcode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 9),
    _CienaCesChassisIDPBarcode_Type()
)
cienaCesChassisIDPBarcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPBarcode.setStatus("current")
_CienaCesChassisIDPSWCompat_Type = Integer32
_CienaCesChassisIDPSWCompat_Object = MibScalar
cienaCesChassisIDPSWCompat = _CienaCesChassisIDPSWCompat_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 10),
    _CienaCesChassisIDPSWCompat_Type()
)
cienaCesChassisIDPSWCompat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPSWCompat.setStatus("current")
_CienaCesChassisIDPFTC_Type = Integer32
_CienaCesChassisIDPFTC_Object = MibScalar
cienaCesChassisIDPFTC = _CienaCesChassisIDPFTC_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 5, 11),
    _CienaCesChassisIDPFTC_Type()
)
cienaCesChassisIDPFTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIDPFTC.setStatus("current")
_CienaCesChassisIOM_ObjectIdentity = ObjectIdentity
cienaCesChassisIOM = _CienaCesChassisIOM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6)
)


class _CienaCesChassisIOMState_Type(Integer32):
    """Custom type cienaCesChassisIOMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("faulted", 2),
          ("uninstalled", 3))
    )


_CienaCesChassisIOMState_Type.__name__ = "Integer32"
_CienaCesChassisIOMState_Object = MibScalar
cienaCesChassisIOMState = _CienaCesChassisIOMState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 1),
    _CienaCesChassisIOMState_Type()
)
cienaCesChassisIOMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMState.setStatus("current")
_CienaCesChassisIOMBuzzerEnable_Type = TruthValue
_CienaCesChassisIOMBuzzerEnable_Object = MibScalar
cienaCesChassisIOMBuzzerEnable = _CienaCesChassisIOMBuzzerEnable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 2),
    _CienaCesChassisIOMBuzzerEnable_Type()
)
cienaCesChassisIOMBuzzerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMBuzzerEnable.setStatus("current")


class _CienaCesChassisIOMBuzzerState_Type(Integer32):
    """Custom type cienaCesChassisIOMBuzzerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notSupported", 3))
    )


_CienaCesChassisIOMBuzzerState_Type.__name__ = "Integer32"
_CienaCesChassisIOMBuzzerState_Object = MibScalar
cienaCesChassisIOMBuzzerState = _CienaCesChassisIOMBuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 3),
    _CienaCesChassisIOMBuzzerState_Type()
)
cienaCesChassisIOMBuzzerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMBuzzerState.setStatus("current")
_CienaCesChassisIOMAlarmOutputTable_Object = MibTable
cienaCesChassisIOMAlarmOutputTable = _CienaCesChassisIOMAlarmOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputTable.setStatus("current")
_CienaCesChassisIOMAlarmOutputEntry_Object = MibTableRow
cienaCesChassisIOMAlarmOutputEntry = _CienaCesChassisIOMAlarmOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 4, 1)
)
cienaCesChassisIOMAlarmOutputEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmOutputIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputEntry.setStatus("current")
_CienaCesChassisIOMAlarmOutputIndex_Type = Integer32
_CienaCesChassisIOMAlarmOutputIndex_Object = MibTableColumn
cienaCesChassisIOMAlarmOutputIndex = _CienaCesChassisIOMAlarmOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 4, 1, 1),
    _CienaCesChassisIOMAlarmOutputIndex_Type()
)
cienaCesChassisIOMAlarmOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputIndex.setStatus("current")
_CienaCesChassisIOMAlarmOutputDescription_Type = DisplayString
_CienaCesChassisIOMAlarmOutputDescription_Object = MibTableColumn
cienaCesChassisIOMAlarmOutputDescription = _CienaCesChassisIOMAlarmOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 4, 1, 2),
    _CienaCesChassisIOMAlarmOutputDescription_Type()
)
cienaCesChassisIOMAlarmOutputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputDescription.setStatus("current")


class _CienaCesChassisIOMAlarmOutputState_Type(Integer32):
    """Custom type cienaCesChassisIOMAlarmOutputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notSupported", 3))
    )


_CienaCesChassisIOMAlarmOutputState_Type.__name__ = "Integer32"
_CienaCesChassisIOMAlarmOutputState_Object = MibTableColumn
cienaCesChassisIOMAlarmOutputState = _CienaCesChassisIOMAlarmOutputState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 4, 1, 3),
    _CienaCesChassisIOMAlarmOutputState_Type()
)
cienaCesChassisIOMAlarmOutputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputState.setStatus("current")
_CienaCesChassisIOMAlarmInputTable_Object = MibTable
cienaCesChassisIOMAlarmInputTable = _CienaCesChassisIOMAlarmInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 5)
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputTable.setStatus("current")
_CienaCesChassisIOMAlarmInputEntry_Object = MibTableRow
cienaCesChassisIOMAlarmInputEntry = _CienaCesChassisIOMAlarmInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 5, 1)
)
cienaCesChassisIOMAlarmInputEntry.setIndexNames(
    (0, "CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmInputIndex"),
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputEntry.setStatus("current")
_CienaCesChassisIOMAlarmInputIndex_Type = Integer32
_CienaCesChassisIOMAlarmInputIndex_Object = MibTableColumn
cienaCesChassisIOMAlarmInputIndex = _CienaCesChassisIOMAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 5, 1, 1),
    _CienaCesChassisIOMAlarmInputIndex_Type()
)
cienaCesChassisIOMAlarmInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputIndex.setStatus("current")
_CienaCesChassisIOMAlarmInputDescription_Type = DisplayString
_CienaCesChassisIOMAlarmInputDescription_Object = MibTableColumn
cienaCesChassisIOMAlarmInputDescription = _CienaCesChassisIOMAlarmInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 5, 1, 2),
    _CienaCesChassisIOMAlarmInputDescription_Type()
)
cienaCesChassisIOMAlarmInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputDescription.setStatus("current")


class _CienaCesChassisIOMAlarmInputState_Type(Integer32):
    """Custom type cienaCesChassisIOMAlarmInputState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notSupported", 3))
    )


_CienaCesChassisIOMAlarmInputState_Type.__name__ = "Integer32"
_CienaCesChassisIOMAlarmInputState_Object = MibTableColumn
cienaCesChassisIOMAlarmInputState = _CienaCesChassisIOMAlarmInputState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 5, 1, 3),
    _CienaCesChassisIOMAlarmInputState_Type()
)
cienaCesChassisIOMAlarmInputState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputState.setStatus("current")
_CienaCesChassisIOMName_Type = DisplayString
_CienaCesChassisIOMName_Object = MibScalar
cienaCesChassisIOMName = _CienaCesChassisIOMName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 6),
    _CienaCesChassisIOMName_Type()
)
cienaCesChassisIOMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMName.setStatus("current")


class _CienaCesChassisIOMChassisIndx_Type(Unsigned32):
    """Custom type cienaCesChassisIOMChassisIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CienaCesChassisIOMChassisIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisIOMChassisIndx_Object = MibScalar
cienaCesChassisIOMChassisIndx = _CienaCesChassisIOMChassisIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 7),
    _CienaCesChassisIOMChassisIndx_Type()
)
cienaCesChassisIOMChassisIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMChassisIndx.setStatus("current")


class _CienaCesChassisIOMShelfIndx_Type(Unsigned32):
    """Custom type cienaCesChassisIOMShelfIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_CienaCesChassisIOMShelfIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisIOMShelfIndx_Object = MibScalar
cienaCesChassisIOMShelfIndx = _CienaCesChassisIOMShelfIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 8),
    _CienaCesChassisIOMShelfIndx_Type()
)
cienaCesChassisIOMShelfIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMShelfIndx.setStatus("current")


class _CienaCesChassisIOMSlotIndx_Type(Unsigned32):
    """Custom type cienaCesChassisIOMSlotIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 38),
    )


_CienaCesChassisIOMSlotIndx_Type.__name__ = "Unsigned32"
_CienaCesChassisIOMSlotIndx_Object = MibScalar
cienaCesChassisIOMSlotIndx = _CienaCesChassisIOMSlotIndx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 9),
    _CienaCesChassisIOMSlotIndx_Type()
)
cienaCesChassisIOMSlotIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMSlotIndx.setStatus("current")
_CienaCesChassisIOMSerialNumber_Type = DisplayString
_CienaCesChassisIOMSerialNumber_Object = MibScalar
cienaCesChassisIOMSerialNumber = _CienaCesChassisIOMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 1, 6, 10),
    _CienaCesChassisIOMSerialNumber_Type()
)
cienaCesChassisIOMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisIOMSerialNumber.setStatus("current")
_CienaCesChassisPlatform_ObjectIdentity = ObjectIdentity
cienaCesChassisPlatform = _CienaCesChassisPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2)
)


class _CienaCesChassisPlatformType_Type(OctetString):
    """Custom type cienaCesChassisPlatformType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CienaCesChassisPlatformType_Type.__name__ = "OctetString"
_CienaCesChassisPlatformType_Object = MibScalar
cienaCesChassisPlatformType = _CienaCesChassisPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 1),
    _CienaCesChassisPlatformType_Type()
)
cienaCesChassisPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPlatformType.setStatus("current")
_CienaCesChassisPlatformName_Type = DisplayString
_CienaCesChassisPlatformName_Object = MibScalar
cienaCesChassisPlatformName = _CienaCesChassisPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 2),
    _CienaCesChassisPlatformName_Type()
)
cienaCesChassisPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPlatformName.setStatus("current")
_CienaCesChassisPlatformDesc_Type = DisplayString
_CienaCesChassisPlatformDesc_Object = MibScalar
cienaCesChassisPlatformDesc = _CienaCesChassisPlatformDesc_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 3),
    _CienaCesChassisPlatformDesc_Type()
)
cienaCesChassisPlatformDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPlatformDesc.setStatus("current")
_CienaCesChassisNumSlots_Type = Integer32
_CienaCesChassisNumSlots_Object = MibScalar
cienaCesChassisNumSlots = _CienaCesChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 4),
    _CienaCesChassisNumSlots_Type()
)
cienaCesChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisNumSlots.setStatus("current")
_CienaCesChassisPrimaryCtrlSlot_Type = Integer32
_CienaCesChassisPrimaryCtrlSlot_Object = MibScalar
cienaCesChassisPrimaryCtrlSlot = _CienaCesChassisPrimaryCtrlSlot_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 5),
    _CienaCesChassisPrimaryCtrlSlot_Type()
)
cienaCesChassisPrimaryCtrlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPrimaryCtrlSlot.setStatus("current")
_CienaCesChassisSecondaryCtrlSlot_Type = Integer32
_CienaCesChassisSecondaryCtrlSlot_Object = MibScalar
cienaCesChassisSecondaryCtrlSlot = _CienaCesChassisSecondaryCtrlSlot_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 6),
    _CienaCesChassisSecondaryCtrlSlot_Type()
)
cienaCesChassisSecondaryCtrlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSecondaryCtrlSlot.setStatus("current")
_CienaCesChassisNumFanTrays_Type = Integer32
_CienaCesChassisNumFanTrays_Object = MibScalar
cienaCesChassisNumFanTrays = _CienaCesChassisNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 7),
    _CienaCesChassisNumFanTrays_Type()
)
cienaCesChassisNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisNumFanTrays.setStatus("current")
_CienaCesChassisNumFansPerTray_Type = Integer32
_CienaCesChassisNumFansPerTray_Object = MibScalar
cienaCesChassisNumFansPerTray = _CienaCesChassisNumFansPerTray_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 8),
    _CienaCesChassisNumFansPerTray_Type()
)
cienaCesChassisNumFansPerTray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisNumFansPerTray.setStatus("current")


class _CienaCesChassisDcPower_Type(Integer32):
    """Custom type cienaCesChassisDcPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CienaCesChassisDcPower_Type.__name__ = "Integer32"
_CienaCesChassisDcPower_Object = MibScalar
cienaCesChassisDcPower = _CienaCesChassisDcPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 9),
    _CienaCesChassisDcPower_Type()
)
cienaCesChassisDcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisDcPower.setStatus("current")


class _CienaCesChassisRedunPower_Type(Integer32):
    """Custom type cienaCesChassisRedunPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_CienaCesChassisRedunPower_Type.__name__ = "Integer32"
_CienaCesChassisRedunPower_Object = MibScalar
cienaCesChassisRedunPower = _CienaCesChassisRedunPower_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 10),
    _CienaCesChassisRedunPower_Type()
)
cienaCesChassisRedunPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisRedunPower.setStatus("current")
_CienaCesChassisPhysicalPortsMax_Type = Integer32
_CienaCesChassisPhysicalPortsMax_Object = MibScalar
cienaCesChassisPhysicalPortsMax = _CienaCesChassisPhysicalPortsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 11),
    _CienaCesChassisPhysicalPortsMax_Type()
)
cienaCesChassisPhysicalPortsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPhysicalPortsMax.setStatus("current")
_CienaCesChassisAggPortsMax_Type = Integer32
_CienaCesChassisAggPortsMax_Object = MibScalar
cienaCesChassisAggPortsMax = _CienaCesChassisAggPortsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 12),
    _CienaCesChassisAggPortsMax_Type()
)
cienaCesChassisAggPortsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisAggPortsMax.setStatus("current")
_CienaCesChassisVirtualSwitchMax_Type = Integer32
_CienaCesChassisVirtualSwitchMax_Object = MibScalar
cienaCesChassisVirtualSwitchMax = _CienaCesChassisVirtualSwitchMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 13),
    _CienaCesChassisVirtualSwitchMax_Type()
)
cienaCesChassisVirtualSwitchMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisVirtualSwitchMax.setStatus("current")
_CienaCesChassisVirtualInterfaceMax_Type = Integer32
_CienaCesChassisVirtualInterfaceMax_Object = MibScalar
cienaCesChassisVirtualInterfaceMax = _CienaCesChassisVirtualInterfaceMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 14),
    _CienaCesChassisVirtualInterfaceMax_Type()
)
cienaCesChassisVirtualInterfaceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisVirtualInterfaceMax.setStatus("current")
_CienaCesChassisMulticastGrpsMax_Type = Integer32
_CienaCesChassisMulticastGrpsMax_Object = MibScalar
cienaCesChassisMulticastGrpsMax = _CienaCesChassisMulticastGrpsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 15),
    _CienaCesChassisMulticastGrpsMax_Type()
)
cienaCesChassisMulticastGrpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMulticastGrpsMax.setStatus("current")
_CienaCesChassisRstpDomainsMax_Type = Integer32
_CienaCesChassisRstpDomainsMax_Object = MibScalar
cienaCesChassisRstpDomainsMax = _CienaCesChassisRstpDomainsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 16),
    _CienaCesChassisRstpDomainsMax_Type()
)
cienaCesChassisRstpDomainsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisRstpDomainsMax.setStatus("current")
_CienaCesChassisVirtualInterfacePerVsMax_Type = Integer32
_CienaCesChassisVirtualInterfacePerVsMax_Object = MibScalar
cienaCesChassisVirtualInterfacePerVsMax = _CienaCesChassisVirtualInterfacePerVsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 17),
    _CienaCesChassisVirtualInterfacePerVsMax_Type()
)
cienaCesChassisVirtualInterfacePerVsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisVirtualInterfacePerVsMax.setStatus("current")
_CienaCesChassisReplicPerPortPerVsMax_Type = Integer32
_CienaCesChassisReplicPerPortPerVsMax_Object = MibScalar
cienaCesChassisReplicPerPortPerVsMax = _CienaCesChassisReplicPerPortPerVsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 18),
    _CienaCesChassisReplicPerPortPerVsMax_Type()
)
cienaCesChassisReplicPerPortPerVsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisReplicPerPortPerVsMax.setStatus("current")
_CienaCesChassisReplicMCPortPerVsMax_Type = Integer32
_CienaCesChassisReplicMCPortPerVsMax_Object = MibScalar
cienaCesChassisReplicMCPortPerVsMax = _CienaCesChassisReplicMCPortPerVsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 19),
    _CienaCesChassisReplicMCPortPerVsMax_Type()
)
cienaCesChassisReplicMCPortPerVsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisReplicMCPortPerVsMax.setStatus("current")
_CienaCesChassisSubPortsMax_Type = Integer32
_CienaCesChassisSubPortsMax_Object = MibScalar
cienaCesChassisSubPortsMax = _CienaCesChassisSubPortsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 20),
    _CienaCesChassisSubPortsMax_Type()
)
cienaCesChassisSubPortsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisSubPortsMax.setStatus("current")
_CienaCesChassisQosFlowsMax_Type = Integer32
_CienaCesChassisQosFlowsMax_Object = MibScalar
cienaCesChassisQosFlowsMax = _CienaCesChassisQosFlowsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 21),
    _CienaCesChassisQosFlowsMax_Type()
)
cienaCesChassisQosFlowsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisQosFlowsMax.setStatus("current")
_CienaCesChassisAccessFlowsMax_Type = Integer32
_CienaCesChassisAccessFlowsMax_Object = MibScalar
cienaCesChassisAccessFlowsMax = _CienaCesChassisAccessFlowsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 22),
    _CienaCesChassisAccessFlowsMax_Type()
)
cienaCesChassisAccessFlowsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisAccessFlowsMax.setStatus("current")
_CienaCesChassisCPUSubIntfcsMax_Type = Integer32
_CienaCesChassisCPUSubIntfcsMax_Object = MibScalar
cienaCesChassisCPUSubIntfcsMax = _CienaCesChassisCPUSubIntfcsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 23),
    _CienaCesChassisCPUSubIntfcsMax_Type()
)
cienaCesChassisCPUSubIntfcsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisCPUSubIntfcsMax.setStatus("current")
_CienaCesChassisPBTTunnelGroupsMax_Type = Integer32
_CienaCesChassisPBTTunnelGroupsMax_Object = MibScalar
cienaCesChassisPBTTunnelGroupsMax = _CienaCesChassisPBTTunnelGroupsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 24),
    _CienaCesChassisPBTTunnelGroupsMax_Type()
)
cienaCesChassisPBTTunnelGroupsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPBTTunnelGroupsMax.setStatus("current")
_CienaCesChassisPBTEncapTunnelsMax_Type = Integer32
_CienaCesChassisPBTEncapTunnelsMax_Object = MibScalar
cienaCesChassisPBTEncapTunnelsMax = _CienaCesChassisPBTEncapTunnelsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 25),
    _CienaCesChassisPBTEncapTunnelsMax_Type()
)
cienaCesChassisPBTEncapTunnelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPBTEncapTunnelsMax.setStatus("current")
_CienaCesChassisPBTDecapTunnelsMax_Type = Integer32
_CienaCesChassisPBTDecapTunnelsMax_Object = MibScalar
cienaCesChassisPBTDecapTunnelsMax = _CienaCesChassisPBTDecapTunnelsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 26),
    _CienaCesChassisPBTDecapTunnelsMax_Type()
)
cienaCesChassisPBTDecapTunnelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPBTDecapTunnelsMax.setStatus("current")
_CienaCesChassisPBTServiceIntfcsMax_Type = Integer32
_CienaCesChassisPBTServiceIntfcsMax_Object = MibScalar
cienaCesChassisPBTServiceIntfcsMax = _CienaCesChassisPBTServiceIntfcsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 27),
    _CienaCesChassisPBTServiceIntfcsMax_Type()
)
cienaCesChassisPBTServiceIntfcsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPBTServiceIntfcsMax.setStatus("current")
_CienaCesChassisPBTTransitIntfcsMax_Type = Integer32
_CienaCesChassisPBTTransitIntfcsMax_Object = MibScalar
cienaCesChassisPBTTransitIntfcsMax = _CienaCesChassisPBTTransitIntfcsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 28),
    _CienaCesChassisPBTTransitIntfcsMax_Type()
)
cienaCesChassisPBTTransitIntfcsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisPBTTransitIntfcsMax.setStatus("current")
_CienaCesChassisMeterProfilesMax_Type = Integer32
_CienaCesChassisMeterProfilesMax_Object = MibScalar
cienaCesChassisMeterProfilesMax = _CienaCesChassisMeterProfilesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 29),
    _CienaCesChassisMeterProfilesMax_Type()
)
cienaCesChassisMeterProfilesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMeterProfilesMax.setStatus("current")
_CienaCesChassisFloodContainersMax_Type = Integer32
_CienaCesChassisFloodContainersMax_Object = MibScalar
cienaCesChassisFloodContainersMax = _CienaCesChassisFloodContainersMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 30),
    _CienaCesChassisFloodContainersMax_Type()
)
cienaCesChassisFloodContainersMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFloodContainersMax.setStatus("current")
_CienaCesChassisRCOSProfilesMax_Type = Integer32
_CienaCesChassisRCOSProfilesMax_Object = MibScalar
cienaCesChassisRCOSProfilesMax = _CienaCesChassisRCOSProfilesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 31),
    _CienaCesChassisRCOSProfilesMax_Type()
)
cienaCesChassisRCOSProfilesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisRCOSProfilesMax.setStatus("current")
_CienaCesChassisRCOSMappingsMax_Type = Integer32
_CienaCesChassisRCOSMappingsMax_Object = MibScalar
cienaCesChassisRCOSMappingsMax = _CienaCesChassisRCOSMappingsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 32),
    _CienaCesChassisRCOSMappingsMax_Type()
)
cienaCesChassisRCOSMappingsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisRCOSMappingsMax.setStatus("current")
_CienaCesChassisFCOSMappingsMax_Type = Integer32
_CienaCesChassisFCOSMappingsMax_Object = MibScalar
cienaCesChassisFCOSMappingsMax = _CienaCesChassisFCOSMappingsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 33),
    _CienaCesChassisFCOSMappingsMax_Type()
)
cienaCesChassisFCOSMappingsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisFCOSMappingsMax.setStatus("current")
_CienaCesChassisShapingProfilesMax_Type = Integer32
_CienaCesChassisShapingProfilesMax_Object = MibScalar
cienaCesChassisShapingProfilesMax = _CienaCesChassisShapingProfilesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 34),
    _CienaCesChassisShapingProfilesMax_Type()
)
cienaCesChassisShapingProfilesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisShapingProfilesMax.setStatus("current")
_CienaCesChassisMPLSTunnelGroupsMax_Type = Integer32
_CienaCesChassisMPLSTunnelGroupsMax_Object = MibScalar
cienaCesChassisMPLSTunnelGroupsMax = _CienaCesChassisMPLSTunnelGroupsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 35),
    _CienaCesChassisMPLSTunnelGroupsMax_Type()
)
cienaCesChassisMPLSTunnelGroupsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSTunnelGroupsMax.setStatus("current")
_CienaCesChassisMPLSTunnelsPerGroupMax_Type = Integer32
_CienaCesChassisMPLSTunnelsPerGroupMax_Object = MibScalar
cienaCesChassisMPLSTunnelsPerGroupMax = _CienaCesChassisMPLSTunnelsPerGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 36),
    _CienaCesChassisMPLSTunnelsPerGroupMax_Type()
)
cienaCesChassisMPLSTunnelsPerGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSTunnelsPerGroupMax.setStatus("current")
_CienaCesChassisMPLSEncapTunnelsMax_Type = Integer32
_CienaCesChassisMPLSEncapTunnelsMax_Object = MibScalar
cienaCesChassisMPLSEncapTunnelsMax = _CienaCesChassisMPLSEncapTunnelsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 37),
    _CienaCesChassisMPLSEncapTunnelsMax_Type()
)
cienaCesChassisMPLSEncapTunnelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSEncapTunnelsMax.setStatus("current")
_CienaCesChassisMPLSDecapTunnelsMax_Type = Integer32
_CienaCesChassisMPLSDecapTunnelsMax_Object = MibScalar
cienaCesChassisMPLSDecapTunnelsMax = _CienaCesChassisMPLSDecapTunnelsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 38),
    _CienaCesChassisMPLSDecapTunnelsMax_Type()
)
cienaCesChassisMPLSDecapTunnelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSDecapTunnelsMax.setStatus("current")
_CienaCesChassisMPLSVCMax_Type = Integer32
_CienaCesChassisMPLSVCMax_Object = MibScalar
cienaCesChassisMPLSVCMax = _CienaCesChassisMPLSVCMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 39),
    _CienaCesChassisMPLSVCMax_Type()
)
cienaCesChassisMPLSVCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSVCMax.setStatus("current")
_CienaCesChassisMPLSInterfacesMax_Type = Integer32
_CienaCesChassisMPLSInterfacesMax_Object = MibScalar
cienaCesChassisMPLSInterfacesMax = _CienaCesChassisMPLSInterfacesMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 40),
    _CienaCesChassisMPLSInterfacesMax_Type()
)
cienaCesChassisMPLSInterfacesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSInterfacesMax.setStatus("current")
_CienaCesChassisMPLSTransitTunnelsMax_Type = Integer32
_CienaCesChassisMPLSTransitTunnelsMax_Object = MibScalar
cienaCesChassisMPLSTransitTunnelsMax = _CienaCesChassisMPLSTransitTunnelsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 41),
    _CienaCesChassisMPLSTransitTunnelsMax_Type()
)
cienaCesChassisMPLSTransitTunnelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisMPLSTransitTunnelsMax.setStatus("current")
_CienaCesChassisRedundancyGroupsMax_Type = Unsigned32
_CienaCesChassisRedundancyGroupsMax_Object = MibScalar
cienaCesChassisRedundancyGroupsMax = _CienaCesChassisRedundancyGroupsMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 42),
    _CienaCesChassisRedundancyGroupsMax_Type()
)
cienaCesChassisRedundancyGroupsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisRedundancyGroupsMax.setStatus("current")
_CienaCesChassisLinksPerRedundancyGroupMax_Type = Unsigned32
_CienaCesChassisLinksPerRedundancyGroupMax_Object = MibScalar
cienaCesChassisLinksPerRedundancyGroupMax = _CienaCesChassisLinksPerRedundancyGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 1, 2, 2, 43),
    _CienaCesChassisLinksPerRedundancyGroupMax_Type()
)
cienaCesChassisLinksPerRedundancyGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesChassisLinksPerRedundancyGroupMax.setStatus("current")
_CienaCesChassisMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBConformance = _CienaCesChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2)
)
_CienaCesChassisMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBCompliances = _CienaCesChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 1)
)
_CienaCesChassisMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBGroups = _CienaCesChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2)
)
_CienaCesChassisMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBNotificationPrefix = _CienaCesChassisMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4)
)
_CienaCesChassisMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesChassisMIBNotifications = _CienaCesChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0)
)

# Managed Objects groups

chassisGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 1)
)
chassisGlobalGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisDeviceId"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPartNumber"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSerialNumber"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMfgDate"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisParamVersion"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemDateAndTime"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemTimeOffset"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSystemUTCDateAndTime"))
)
if mibBuilder.loadTexts:
    chassisGlobalGroup.setStatus("current")

chassisPlatformGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 2)
)
chassisPlatformGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPlatformType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPlatformName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPlatformDesc"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisNumSlots"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPrimaryCtrlSlot"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSecondaryCtrlSlot"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisNumFanTrays"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisNumFansPerTray"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisDcPower"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisRedunPower"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPhysicalPortsMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisAggPortsMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisVirtualSwitchMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisVirtualInterfaceMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMulticastGrpsMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisRstpDomainsMax"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisVirtualInterfacePerVsMax"))
)
if mibBuilder.loadTexts:
    chassisPlatformGroup.setStatus("current")

chassisPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 3)
)
chassisPowerSupplyGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyManufacturer"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplySerialNumber"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyPartNum"))
)
if mibBuilder.loadTexts:
    chassisPowerSupplyGroup.setStatus("current")

chassisFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 4)
)
chassisFanGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanAvgSpeed"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanCurrentSpeed"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanMinSpeed"))
)
if mibBuilder.loadTexts:
    chassisFanGroup.setStatus("current")

chassisFanTrayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 5)
)
chassisFanTrayGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayMode"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNumFans"))
)
if mibBuilder.loadTexts:
    chassisFanTrayGroup.setStatus("current")

chassisFanTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 6)
)
chassisFanTempGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempDesc"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTemp"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHigh"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempLow"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempLoThreshold"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHiThreshold"))
)
if mibBuilder.loadTexts:
    chassisFanTempGroup.setStatus("current")

chassisHealthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 8)
)
chassisHealthGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    chassisHealthGroup.setStatus("current")

chassisIomStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 9)
)
chassisIomStateGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerEnable"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmOutputState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmInputState"))
)
if mibBuilder.loadTexts:
    chassisIomStateGroup.setStatus("current")


# Notification objects

cienaCesChassisPowerSupplyFaultedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 1)
)
cienaCesChassisPowerSupplyFaultedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyNotifIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplySlotName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplySlotIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyFaultedNotification.setStatus(
        "current"
    )

cienaCesChassisPowerSupplyOnlineNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 2)
)
cienaCesChassisPowerSupplyOnlineNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyNotifIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplySlotName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplyShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisPowerSupplySlotIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisPowerSupplyOnlineNotification.setStatus(
        "current"
    )

cienaCesChassisFanHiTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 3)
)
cienaCesChassisFanHiTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempTrayNotifIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempNotifId"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTemp"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHiThreshold"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempShelfIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanHiTempNotification.setStatus(
        "current"
    )

cienaCesChassisFanNormalTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 4)
)
cienaCesChassisFanNormalTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempTrayNotifIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempNotifId"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTemp"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempLoThreshold"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempHiThreshold"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempShelfIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanNormalTempNotification.setStatus(
        "current"
    )

cienaCesChassisFanLoTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 5)
)
cienaCesChassisFanLoTempNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempTrayNotifIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempNotifId"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTemp"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempLoThreshold"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTempShelfIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanLoTempNotification.setStatus(
        "current"
    )

cienaCesChassisFanSpeedMinThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 7)
)
cienaCesChassisFanSpeedMinThresholdNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanAvgSpeed"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanShelfIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedMinThresholdNotification.setStatus(
        "current"
    )

cienaCesChassisFanSpeedNormalRangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 8)
)
cienaCesChassisFanSpeedNormalRangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanAvgSpeed"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanShelfIndx"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanSpeedNormalRangeNotification.setStatus(
        "current"
    )

cienaCesChassisFanTrayRemoveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 9)
)
cienaCesChassisFanTrayRemoveNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayRemoveNotification.setStatus(
        "current"
    )

cienaCesChassisFanTrayInsertNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 10)
)
cienaCesChassisFanTrayInsertNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayType"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayInsertNotification.setStatus(
        "current"
    )

cienaCesChassisFanTrayStatusFaultedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 11)
)
cienaCesChassisFanTrayStatusFaultedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayStatusFaultedNotification.setStatus(
        "current"
    )

cienaCesChassisFanTrayStatusOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 12)
)
cienaCesChassisFanTrayStatusOkNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayNotifIndex"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTraySerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisFanTrayStatusOkNotification.setStatus(
        "current"
    )

cienaCesChassisHealthStatusUnknownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 13)
)
cienaCesChassisHealthStatusUnknownNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusUnknownNotification.setStatus(
        "current"
    )

cienaCesChassisHealthStatusWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 14)
)
cienaCesChassisHealthStatusWarningNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusWarningNotification.setStatus(
        "current"
    )

cienaCesChassisHealthStatusFaultedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 15)
)
cienaCesChassisHealthStatusFaultedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusFaultedNotification.setStatus(
        "current"
    )

cienaCesChassisHealthStatusDegradedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 16)
)
cienaCesChassisHealthStatusDegradedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusDegradedNotification.setStatus(
        "current"
    )

cienaCesChassisHealthStatusGoodNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 17)
)
cienaCesChassisHealthStatusGoodNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthSubCategory"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatus"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHealthStatusLast"))
)
if mibBuilder.loadTexts:
    cienaCesChassisHealthStatusGoodNotification.setStatus(
        "current"
    )

cienaCesChassisRebootNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 18)
)
cienaCesChassisRebootNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisRebootReasonErrorType"))
)
if mibBuilder.loadTexts:
    cienaCesChassisRebootNotification.setStatus(
        "current"
    )

cienaCesChassisIOMStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 19)
)
cienaCesChassisIOMStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMStateChangeNotification.setStatus(
        "current"
    )

cienaCesChassisIOMBuzzerEnableChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 20)
)
cienaCesChassisIOMBuzzerEnableChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerEnable"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMBuzzerEnableChangeNotification.setStatus(
        "current"
    )

cienaCesChassisIOMBuzzerStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 21)
)
cienaCesChassisIOMBuzzerStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMBuzzerStateChangeNotification.setStatus(
        "current"
    )

cienaCesChassisIOMAlarmOutputStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 22)
)
cienaCesChassisIOMAlarmOutputStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmOutputDescription"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmOutputState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmOutputStateChangeNotification.setStatus(
        "current"
    )

cienaCesChassisIOMAlarmInputStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 23)
)
cienaCesChassisIOMAlarmInputStateChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmInputDescription"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmInputState"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMName"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMChassisIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMShelfIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSlotIndx"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMSerialNumber"))
)
if mibBuilder.loadTexts:
    cienaCesChassisIOMAlarmInputStateChangeNotification.setStatus(
        "current"
    )

cienaCesChassisUsbFlashEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 24)
)
cienaCesChassisUsbFlashEnabledNotification.setObjects(
    ("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
)
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashEnabledNotification.setStatus(
        "current"
    )

cienaCesChassisUsbFlashDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 25)
)
cienaCesChassisUsbFlashDisabledNotification.setObjects(
    ("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
)
if mibBuilder.loadTexts:
    cienaCesChassisUsbFlashDisabledNotification.setStatus(
        "current"
    )

cienaCesChassisAirFilterServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 26)
)
cienaCesChassisAirFilterServiceNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"))
)
if mibBuilder.loadTexts:
    cienaCesChassisAirFilterServiceNotification.setStatus(
        "current"
    )

cienaCesChassisAlarmCutoffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 27)
)
cienaCesChassisAlarmCutoffNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisAlarmCutoffOrigin"))
)
if mibBuilder.loadTexts:
    cienaCesChassisAlarmCutoffNotification.setStatus(
        "current"
    )

cienaCesChassisDyingGaspNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 4, 0, 28)
)
cienaCesChassisDyingGaspNotification.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisDeviceId"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisHardwareVersion"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisSerialNumber"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMacAddress"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisMfgDate"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisParamVersion"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"))
)
if mibBuilder.loadTexts:
    cienaCesChassisDyingGaspNotification.setStatus(
        "current"
    )


# Notifications groups

chassisNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 7)
)
chassisNotifGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanHiTempNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanLoTempNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanNormalTempNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSpeedMinThresholdNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanSpeedNormalRangeNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayInsertNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisFanTrayRemoveNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisAlarmCutoffNotification"))
)
if mibBuilder.loadTexts:
    chassisNotifGroup.setStatus(
        "current"
    )

chassisIomNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 5, 2, 2, 10)
)
chassisIomNotifGroup.setObjects(
      *(("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMStateChangeNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerEnableChangeNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMBuzzerStateChangeNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmOutputStateChangeNotification"),
        ("CIENA-CES-CHASSIS-MIB", "cienaCesChassisIOMAlarmInputStateChangeNotification"))
)
if mibBuilder.loadTexts:
    chassisIomNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-CHASSIS-MIB",
    **{"cienaCesChassisMIB": cienaCesChassisMIB,
       "cienaCesChassisMIBObjects": cienaCesChassisMIBObjects,
       "cienaCesChassisGlobal": cienaCesChassisGlobal,
       "cienaCesChassisMacAddress": cienaCesChassisMacAddress,
       "cienaCesChassisDeviceId": cienaCesChassisDeviceId,
       "cienaCesChassisPartNumber": cienaCesChassisPartNumber,
       "cienaCesChassisSerialNumber": cienaCesChassisSerialNumber,
       "cienaCesChassisMfgDate": cienaCesChassisMfgDate,
       "cienaCesChassisParamVersion": cienaCesChassisParamVersion,
       "cienaCesChassisSystemDateAndTime": cienaCesChassisSystemDateAndTime,
       "cienaCesChassisSystemUTCDateAndTime": cienaCesChassisSystemUTCDateAndTime,
       "cienaCesChassisSystemTimeOffset": cienaCesChassisSystemTimeOffset,
       "cienaCesChassisRebootReasonErrorType": cienaCesChassisRebootReasonErrorType,
       "cienaCesChassisSystemId": cienaCesChassisSystemId,
       "cienaCesChassisAlarmCutoffOrigin": cienaCesChassisAlarmCutoffOrigin,
       "cienaCesChassisRestart": cienaCesChassisRestart,
       "cienaCesChassisMefSourceMacAddress": cienaCesChassisMefSourceMacAddress,
       "cienaCesChassisObjects": cienaCesChassisObjects,
       "cienaCesChassis": cienaCesChassis,
       "cienaCesChassisPowerModule": cienaCesChassisPowerModule,
       "cienaCesChassisPowerTable": cienaCesChassisPowerTable,
       "cienaCesChassisPowerEntry": cienaCesChassisPowerEntry,
       "cienaCesChassisPowerSupplyIndx": cienaCesChassisPowerSupplyIndx,
       "cienaCesChassisPowerSupplyState": cienaCesChassisPowerSupplyState,
       "cienaCesChassisPowerSupplyType": cienaCesChassisPowerSupplyType,
       "cienaCesChassisPowerSupplyManufacturer": cienaCesChassisPowerSupplyManufacturer,
       "cienaCesChassisPowerSupplySerialNumber": cienaCesChassisPowerSupplySerialNumber,
       "cienaCesChassisPowerSupplyPartNum": cienaCesChassisPowerSupplyPartNum,
       "cienaCesChassisPowerSupplyNotifIndx": cienaCesChassisPowerSupplyNotifIndx,
       "cienaCesChassisPowerSupplyFRU": cienaCesChassisPowerSupplyFRU,
       "cienaCesChassisPowerSupplySlotName": cienaCesChassisPowerSupplySlotName,
       "cienaCesChassisPowerSupplyRevInfo": cienaCesChassisPowerSupplyRevInfo,
       "cienaCesChassisPowerSupplyChassisIndx": cienaCesChassisPowerSupplyChassisIndx,
       "cienaCesChassisPowerSupplyShelfIndx": cienaCesChassisPowerSupplyShelfIndx,
       "cienaCesChassisPowerSupplySlotIndx": cienaCesChassisPowerSupplySlotIndx,
       "cienaCesChassisFanModule": cienaCesChassisFanModule,
       "cienaCesChassisFanTable": cienaCesChassisFanTable,
       "cienaCesChassisFanEntry": cienaCesChassisFanEntry,
       "cienaCesChassisFanTrayIndx": cienaCesChassisFanTrayIndx,
       "cienaCesChassisFanIndx": cienaCesChassisFanIndx,
       "cienaCesChassisFanStatus": cienaCesChassisFanStatus,
       "cienaCesChassisFanAvgSpeed": cienaCesChassisFanAvgSpeed,
       "cienaCesChassisFanCurrentSpeed": cienaCesChassisFanCurrentSpeed,
       "cienaCesChassisFanMinSpeed": cienaCesChassisFanMinSpeed,
       "cienaCesChassisFanTrayNotifIndex": cienaCesChassisFanTrayNotifIndex,
       "cienaCesChassisFanNotifIndex": cienaCesChassisFanNotifIndex,
       "cienaCesChassisFanName": cienaCesChassisFanName,
       "cienaCesChassisFanChassisIndx": cienaCesChassisFanChassisIndx,
       "cienaCesChassisFanShelfIndx": cienaCesChassisFanShelfIndx,
       "cienaCesChassisFanTrayTable": cienaCesChassisFanTrayTable,
       "cienaCesChassisFanTrayEntry": cienaCesChassisFanTrayEntry,
       "cienaCesChassisFanTrayStatus": cienaCesChassisFanTrayStatus,
       "cienaCesChassisFanTrayType": cienaCesChassisFanTrayType,
       "cienaCesChassisFanTrayMode": cienaCesChassisFanTrayMode,
       "cienaCesChassisFanTrayNumFans": cienaCesChassisFanTrayNumFans,
       "cienaCesChassisFanTrayName": cienaCesChassisFanTrayName,
       "cienaCesChassisFanTrayChassisIndx": cienaCesChassisFanTrayChassisIndx,
       "cienaCesChassisFanTrayShelfIndx": cienaCesChassisFanTrayShelfIndx,
       "cienaCesChassisFanTraySlotIndx": cienaCesChassisFanTraySlotIndx,
       "cienaCesChassisFanTraySerialNumber": cienaCesChassisFanTraySerialNumber,
       "cienaCesChassisFanModuleTemp": cienaCesChassisFanModuleTemp,
       "cienaCesChassisFanTempTable": cienaCesChassisFanTempTable,
       "cienaCesChassisFanTempEntry": cienaCesChassisFanTempEntry,
       "cienaCesChassisFanTempTrayIndx": cienaCesChassisFanTempTrayIndx,
       "cienaCesChassisFanTempId": cienaCesChassisFanTempId,
       "cienaCesChassisFanTempDesc": cienaCesChassisFanTempDesc,
       "cienaCesChassisFanTemp": cienaCesChassisFanTemp,
       "cienaCesChassisFanTempHigh": cienaCesChassisFanTempHigh,
       "cienaCesChassisFanTempLow": cienaCesChassisFanTempLow,
       "cienaCesChassisFanTempLoThreshold": cienaCesChassisFanTempLoThreshold,
       "cienaCesChassisFanTempHiThreshold": cienaCesChassisFanTempHiThreshold,
       "cienaCesChassisFanTempTrayNotifIndx": cienaCesChassisFanTempTrayNotifIndx,
       "cienaCesChassisFanTempNotifId": cienaCesChassisFanTempNotifId,
       "cienaCesChassisFanTempName": cienaCesChassisFanTempName,
       "cienaCesChassisFanTempChassisIndx": cienaCesChassisFanTempChassisIndx,
       "cienaCesChassisFanTempShelfIndx": cienaCesChassisFanTempShelfIndx,
       "cienaCesChassisHealth": cienaCesChassisHealth,
       "cienaCesChassisHealthCategory": cienaCesChassisHealthCategory,
       "cienaCesChassisHealthSubCategory": cienaCesChassisHealthSubCategory,
       "cienaCesChassisHealthStatus": cienaCesChassisHealthStatus,
       "cienaCesChassisHealthStatusLast": cienaCesChassisHealthStatusLast,
       "cienaCesChassisCPUHealthTable": cienaCesChassisCPUHealthTable,
       "cienaCesChassisCPUHealthEntry": cienaCesChassisCPUHealthEntry,
       "cienaCesChassisCPUHealthSubCategory": cienaCesChassisCPUHealthSubCategory,
       "cienaCesChassisCPUHealthOriginIndex": cienaCesChassisCPUHealthOriginIndex,
       "cienaCesChassisCPUHealthState": cienaCesChassisCPUHealthState,
       "cienaCesChassisCPUHealthCurrMeasurement": cienaCesChassisCPUHealthCurrMeasurement,
       "cienaCesChassisCPUHealthMaxMeasurement": cienaCesChassisCPUHealthMaxMeasurement,
       "cienaCesChassisCPUHealthMaxThreshold": cienaCesChassisCPUHealthMaxThreshold,
       "cienaCesChassisDatapathHealthTable": cienaCesChassisDatapathHealthTable,
       "cienaCesChassisDatapathHealthEntry": cienaCesChassisDatapathHealthEntry,
       "cienaCesChassisDatapathHealthSubCategory": cienaCesChassisDatapathHealthSubCategory,
       "cienaCesChassisDatapathHealthOriginIndex": cienaCesChassisDatapathHealthOriginIndex,
       "cienaCesChassisDatapathHealthState": cienaCesChassisDatapathHealthState,
       "cienaCesChassisControlPlaneHealthTable": cienaCesChassisControlPlaneHealthTable,
       "cienaCesChassisControlPlaneHealthEntry": cienaCesChassisControlPlaneHealthEntry,
       "cienaCesChassisControlPlaneHealthSubCategory": cienaCesChassisControlPlaneHealthSubCategory,
       "cienaCesChassisControlPlaneHealthOriginIndex": cienaCesChassisControlPlaneHealthOriginIndex,
       "cienaCesChassisControlPlaneHealthState": cienaCesChassisControlPlaneHealthState,
       "cienaCesChassisControlPlaneHealthCurrMeasurement": cienaCesChassisControlPlaneHealthCurrMeasurement,
       "cienaCesChassisControlPlaneHealthMaxMeasurement": cienaCesChassisControlPlaneHealthMaxMeasurement,
       "cienaCesChassisControlPlaneHealthMaxThreshold": cienaCesChassisControlPlaneHealthMaxThreshold,
       "cienaCesChassisFabricHealthTable": cienaCesChassisFabricHealthTable,
       "cienaCesChassisFabricHealthEntry": cienaCesChassisFabricHealthEntry,
       "cienaCesChassisFabricHealthSubCategory": cienaCesChassisFabricHealthSubCategory,
       "cienaCesChassisFabricHealthOriginIndex": cienaCesChassisFabricHealthOriginIndex,
       "cienaCesChassisFabricHealthState": cienaCesChassisFabricHealthState,
       "cienaCesChassisSMHealthTable": cienaCesChassisSMHealthTable,
       "cienaCesChassisSMHealthEntry": cienaCesChassisSMHealthEntry,
       "cienaCesChassisSMHealthSubCategory": cienaCesChassisSMHealthSubCategory,
       "cienaCesChassisSMHealthOriginIndex": cienaCesChassisSMHealthOriginIndex,
       "cienaCesChassisSMHealthState": cienaCesChassisSMHealthState,
       "cienaCesChassisSMTempHealthTable": cienaCesChassisSMTempHealthTable,
       "cienaCesChassisSMTempHealthEntry": cienaCesChassisSMTempHealthEntry,
       "cienaCesChassisSMTempHealthSubCategory": cienaCesChassisSMTempHealthSubCategory,
       "cienaCesChassisSMTempHealthOriginIndex": cienaCesChassisSMTempHealthOriginIndex,
       "cienaCesChassisSMTempHealthState": cienaCesChassisSMTempHealthState,
       "cienaCesChassisSMTempHealthCurrMeasurement": cienaCesChassisSMTempHealthCurrMeasurement,
       "cienaCesChassisSMTempHealthMinMeasurement": cienaCesChassisSMTempHealthMinMeasurement,
       "cienaCesChassisSMTempHealthMaxMeasurement": cienaCesChassisSMTempHealthMaxMeasurement,
       "cienaCesChassisSMTempHealthMinThreshold": cienaCesChassisSMTempHealthMinThreshold,
       "cienaCesChassisSMTempHealthMaxThreshold": cienaCesChassisSMTempHealthMaxThreshold,
       "cienaCesChassisSMSamplesHealthTable": cienaCesChassisSMSamplesHealthTable,
       "cienaCesChassisSMSamplesHealthEntry": cienaCesChassisSMSamplesHealthEntry,
       "cienaCesChassisSMSamplesHealthSubCategory": cienaCesChassisSMSamplesHealthSubCategory,
       "cienaCesChassisSMSamplesHealthOriginIndex": cienaCesChassisSMSamplesHealthOriginIndex,
       "cienaCesChassisSMSamplesHealthState": cienaCesChassisSMSamplesHealthState,
       "cienaCesChassisSMSamplesHealthCurrMeasurement": cienaCesChassisSMSamplesHealthCurrMeasurement,
       "cienaCesChassisSMSamplesHealthMaxMeasurement": cienaCesChassisSMSamplesHealthMaxMeasurement,
       "cienaCesChassisDiskHealthTable": cienaCesChassisDiskHealthTable,
       "cienaCesChassisDiskHealthEntry": cienaCesChassisDiskHealthEntry,
       "cienaCesChassisDiskHealthSubCategory": cienaCesChassisDiskHealthSubCategory,
       "cienaCesChassisDiskHealthOriginIndex": cienaCesChassisDiskHealthOriginIndex,
       "cienaCesChassisDiskHealthState": cienaCesChassisDiskHealthState,
       "cienaCesChassisDiskHealthCurrMeasurement": cienaCesChassisDiskHealthCurrMeasurement,
       "cienaCesChassisDiskHealthMaxMeasurement": cienaCesChassisDiskHealthMaxMeasurement,
       "cienaCesChassisDiskHealthMaxThreshold": cienaCesChassisDiskHealthMaxThreshold,
       "cienaCesChassisModuleTempHealthTable": cienaCesChassisModuleTempHealthTable,
       "cienaCesChassisModuleTempHealthEntry": cienaCesChassisModuleTempHealthEntry,
       "cienaCesChassisModuleTempHealthSubCategory": cienaCesChassisModuleTempHealthSubCategory,
       "cienaCesChassisModuleTempHealthOriginIndex": cienaCesChassisModuleTempHealthOriginIndex,
       "cienaCesChassisModuleTempHealthState": cienaCesChassisModuleTempHealthState,
       "cienaCesChassisModuleTempHealthCurrMeasurement": cienaCesChassisModuleTempHealthCurrMeasurement,
       "cienaCesChassisModuleTempHealthMinMeasurement": cienaCesChassisModuleTempHealthMinMeasurement,
       "cienaCesChassisModuleTempHealthMaxMeasurement": cienaCesChassisModuleTempHealthMaxMeasurement,
       "cienaCesChassisModuleTempHealthMinThreshold": cienaCesChassisModuleTempHealthMinThreshold,
       "cienaCesChassisModuleTempHealthMaxThreshold": cienaCesChassisModuleTempHealthMaxThreshold,
       "cienaCesChassisModuleSamplesHealthTable": cienaCesChassisModuleSamplesHealthTable,
       "cienaCesChassisModuleSamplesHealthEntry": cienaCesChassisModuleSamplesHealthEntry,
       "cienaCesChassisModuleSamplesHealthSubCategory": cienaCesChassisModuleSamplesHealthSubCategory,
       "cienaCesChassisModuleSamplesHealthOriginIndex": cienaCesChassisModuleSamplesHealthOriginIndex,
       "cienaCesChassisModuleSamplesHealthState": cienaCesChassisModuleSamplesHealthState,
       "cienaCesChassisModuleSamplesHealthCurrMeasurement": cienaCesChassisModuleSamplesHealthCurrMeasurement,
       "cienaCesChassisModuleSamplesHealthMaxMeasurement": cienaCesChassisModuleSamplesHealthMaxMeasurement,
       "cienaCesChassisFanTrayHealthTable": cienaCesChassisFanTrayHealthTable,
       "cienaCesChassisFanTrayHealthEntry": cienaCesChassisFanTrayHealthEntry,
       "cienaCesChassisFanTrayHealthSubCategory": cienaCesChassisFanTrayHealthSubCategory,
       "cienaCesChassisFanTrayHealthOriginIndex": cienaCesChassisFanTrayHealthOriginIndex,
       "cienaCesChassisFanTrayHealthState": cienaCesChassisFanTrayHealthState,
       "cienaCesChassisFanTraySpeedMismatchHealthTable": cienaCesChassisFanTraySpeedMismatchHealthTable,
       "cienaCesChassisFanTraySpeedMismatchHealthEntry": cienaCesChassisFanTraySpeedMismatchHealthEntry,
       "cienaCesChassisFanTraySpeedMismatchHealthSubCategory": cienaCesChassisFanTraySpeedMismatchHealthSubCategory,
       "cienaCesChassisFanTraySpeedMismatchHealthOriginIndex": cienaCesChassisFanTraySpeedMismatchHealthOriginIndex,
       "cienaCesChassisFanTraySpeedMismatchHealthState": cienaCesChassisFanTraySpeedMismatchHealthState,
       "cienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement": cienaCesChassisFanTraySpeedMismatchHealthCurrMeasurement,
       "cienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement": cienaCesChassisFanTraySpeedMismatchHealthMaxMeasurement,
       "cienaCesChassisFanTraySpeedMismatchHealthMaxThreshold": cienaCesChassisFanTraySpeedMismatchHealthMaxThreshold,
       "cienaCesChassisFanSpeedMismatchHealthTable": cienaCesChassisFanSpeedMismatchHealthTable,
       "cienaCesChassisFanSpeedMismatchHealthEntry": cienaCesChassisFanSpeedMismatchHealthEntry,
       "cienaCesChassisFanSpeedMismatchHealthSubCategory": cienaCesChassisFanSpeedMismatchHealthSubCategory,
       "cienaCesChassisFanSpeedMismatchHealthOriginIndex": cienaCesChassisFanSpeedMismatchHealthOriginIndex,
       "cienaCesChassisFanSpeedMismatchHealthState": cienaCesChassisFanSpeedMismatchHealthState,
       "cienaCesChassisFanTempHealthTable": cienaCesChassisFanTempHealthTable,
       "cienaCesChassisFanTempHealthEntry": cienaCesChassisFanTempHealthEntry,
       "cienaCesChassisFanTempHealthSubCategory": cienaCesChassisFanTempHealthSubCategory,
       "cienaCesChassisFanTempHealthOriginIndex": cienaCesChassisFanTempHealthOriginIndex,
       "cienaCesChassisFanTempHealthState": cienaCesChassisFanTempHealthState,
       "cienaCesChassisFanTempHealthCurrMeasurement": cienaCesChassisFanTempHealthCurrMeasurement,
       "cienaCesChassisFanTempHealthMinMeasurement": cienaCesChassisFanTempHealthMinMeasurement,
       "cienaCesChassisFanTempHealthMaxMeasurement": cienaCesChassisFanTempHealthMaxMeasurement,
       "cienaCesChassisFanTempHealthMinThreshold": cienaCesChassisFanTempHealthMinThreshold,
       "cienaCesChassisFanTempHealthMaxThreshold": cienaCesChassisFanTempHealthMaxThreshold,
       "cienaCesChassisFanSamplesHealthTable": cienaCesChassisFanSamplesHealthTable,
       "cienaCesChassisFanSamplesHealthEntry": cienaCesChassisFanSamplesHealthEntry,
       "cienaCesChassisFanSamplesHealthSubCategory": cienaCesChassisFanSamplesHealthSubCategory,
       "cienaCesChassisFanSamplesHealthOriginIndex": cienaCesChassisFanSamplesHealthOriginIndex,
       "cienaCesChassisFanSamplesHealthState": cienaCesChassisFanSamplesHealthState,
       "cienaCesChassisFanSamplesHealthCurrMeasurement": cienaCesChassisFanSamplesHealthCurrMeasurement,
       "cienaCesChassisFanSamplesHealthMaxMeasurement": cienaCesChassisFanSamplesHealthMaxMeasurement,
       "cienaCesChassisFanRPMHealthTable": cienaCesChassisFanRPMHealthTable,
       "cienaCesChassisFanRPMHealthEntry": cienaCesChassisFanRPMHealthEntry,
       "cienaCesChassisFanRPMHealthSubCategory": cienaCesChassisFanRPMHealthSubCategory,
       "cienaCesChassisFanRPMHealthOriginIndex": cienaCesChassisFanRPMHealthOriginIndex,
       "cienaCesChassisFanRPMHealthState": cienaCesChassisFanRPMHealthState,
       "cienaCesChassisFanRPMHealthCurrMeasurement": cienaCesChassisFanRPMHealthCurrMeasurement,
       "cienaCesChassisFanRPMHealthMinMeasurement": cienaCesChassisFanRPMHealthMinMeasurement,
       "cienaCesChassisFanRPMHealthMinThreshold": cienaCesChassisFanRPMHealthMinThreshold,
       "cienaCesChassisPowerHealthTable": cienaCesChassisPowerHealthTable,
       "cienaCesChassisPowerHealthEntry": cienaCesChassisPowerHealthEntry,
       "cienaCesChassisPowerHealthSubCategory": cienaCesChassisPowerHealthSubCategory,
       "cienaCesChassisPowerHealthOriginIndex": cienaCesChassisPowerHealthOriginIndex,
       "cienaCesChassisPowerHealthState": cienaCesChassisPowerHealthState,
       "cienaCesChassisFeedPowerHealthTable": cienaCesChassisFeedPowerHealthTable,
       "cienaCesChassisFeedPowerHealthEntry": cienaCesChassisFeedPowerHealthEntry,
       "cienaCesChassisFeedPowerHealthSubCategory": cienaCesChassisFeedPowerHealthSubCategory,
       "cienaCesChassisFeedPowerHealthOriginIndex": cienaCesChassisFeedPowerHealthOriginIndex,
       "cienaCesChassisFeedPowerHealthState": cienaCesChassisFeedPowerHealthState,
       "cienaCesChassisResourceHealthTable": cienaCesChassisResourceHealthTable,
       "cienaCesChassisResourceHealthEntry": cienaCesChassisResourceHealthEntry,
       "cienaCesChassisResourceHealthSubCategory": cienaCesChassisResourceHealthSubCategory,
       "cienaCesChassisResourceHealthState": cienaCesChassisResourceHealthState,
       "cienaCesChassisResourceHealthCurrMeasurement": cienaCesChassisResourceHealthCurrMeasurement,
       "cienaCesChassisResourceHealthMaxMeasurement": cienaCesChassisResourceHealthMaxMeasurement,
       "cienaCesChassisResourceHealthMaxThreshold": cienaCesChassisResourceHealthMaxThreshold,
       "cienaCesChassisMemoryHealthTable": cienaCesChassisMemoryHealthTable,
       "cienaCesChassisMemoryHealthEntry": cienaCesChassisMemoryHealthEntry,
       "cienaCesChassisMemoryHealthSubCategory": cienaCesChassisMemoryHealthSubCategory,
       "cienaCesChassisMemoryHealthOriginIndex": cienaCesChassisMemoryHealthOriginIndex,
       "cienaCesChassisMemoryHealthState": cienaCesChassisMemoryHealthState,
       "cienaCesChassisMemoryHealthCurrMeasurement": cienaCesChassisMemoryHealthCurrMeasurement,
       "cienaCesChassisMemoryHealthMaxMeasurement": cienaCesChassisMemoryHealthMaxMeasurement,
       "cienaCesChassisMemoryHealthMaxThreshold": cienaCesChassisMemoryHealthMaxThreshold,
       "cienaCesChassisMACHealthTable": cienaCesChassisMACHealthTable,
       "cienaCesChassisMACHealthEntry": cienaCesChassisMACHealthEntry,
       "cienaCesChassisMACHealthSubCategory": cienaCesChassisMACHealthSubCategory,
       "cienaCesChassisMACHealthOriginIndex": cienaCesChassisMACHealthOriginIndex,
       "cienaCesChassisMACHealthState": cienaCesChassisMACHealthState,
       "cienaCesChassisMACHealthCurrMeasurement": cienaCesChassisMACHealthCurrMeasurement,
       "cienaCesChassisMACHealthMaxMeasurement": cienaCesChassisMACHealthMaxMeasurement,
       "cienaCesChassisMACHealthMaxThreshold": cienaCesChassisMACHealthMaxThreshold,
       "cienaCesChassisI2CHealthTable": cienaCesChassisI2CHealthTable,
       "cienaCesChassisI2CHealthEntry": cienaCesChassisI2CHealthEntry,
       "cienaCesChassisI2CHealthSubCategory": cienaCesChassisI2CHealthSubCategory,
       "cienaCesChassisI2CHealthOriginIndex": cienaCesChassisI2CHealthOriginIndex,
       "cienaCesChassisI2CHealthState": cienaCesChassisI2CHealthState,
       "cienaCesChassisFlashDriverHealthTable": cienaCesChassisFlashDriverHealthTable,
       "cienaCesChassisFlashDriverHealthEntry": cienaCesChassisFlashDriverHealthEntry,
       "cienaCesChassisFlashDriverHealthSubCategory": cienaCesChassisFlashDriverHealthSubCategory,
       "cienaCesChassisFlashDriverHealthOriginIndex": cienaCesChassisFlashDriverHealthOriginIndex,
       "cienaCesChassisFlashDriverHealthState": cienaCesChassisFlashDriverHealthState,
       "cienaCesChassisFlashDriverHealthCurrMeasurement": cienaCesChassisFlashDriverHealthCurrMeasurement,
       "cienaCesChassisFlashDriverHealthMaxMeasurement": cienaCesChassisFlashDriverHealthMaxMeasurement,
       "cienaCesChassisXcvrHealthTable": cienaCesChassisXcvrHealthTable,
       "cienaCesChassisXcvrHealthEntry": cienaCesChassisXcvrHealthEntry,
       "cienaCesChassisXcvrHealthSubCategory": cienaCesChassisXcvrHealthSubCategory,
       "cienaCesChassisXcvrHealthOriginIndex": cienaCesChassisXcvrHealthOriginIndex,
       "cienaCesChassisXcvrHealthState": cienaCesChassisXcvrHealthState,
       "cienaCesChassisXcvrHealthCurrMeasurement": cienaCesChassisXcvrHealthCurrMeasurement,
       "cienaCesChassisXcvrHealthMinMeasurement": cienaCesChassisXcvrHealthMinMeasurement,
       "cienaCesChassisXcvrHealthMaxMeasurement": cienaCesChassisXcvrHealthMaxMeasurement,
       "cienaCesChassisXcvrHealthMinThreshold": cienaCesChassisXcvrHealthMinThreshold,
       "cienaCesChassisXcvrHealthMaxThreshold": cienaCesChassisXcvrHealthMaxThreshold,
       "cienaCesChassisXcvrHealthUnit": cienaCesChassisXcvrHealthUnit,
       "cienaCesChassisPortLinkHealthTable": cienaCesChassisPortLinkHealthTable,
       "cienaCesChassisPortLinkHealthEntry": cienaCesChassisPortLinkHealthEntry,
       "cienaCesChassisPortLinkHealthSubCategory": cienaCesChassisPortLinkHealthSubCategory,
       "cienaCesChassisPortLinkHealthOriginIndex": cienaCesChassisPortLinkHealthOriginIndex,
       "cienaCesChassisPortLinkHealthState": cienaCesChassisPortLinkHealthState,
       "cienaCesChassisIOMStatusHealthTable": cienaCesChassisIOMStatusHealthTable,
       "cienaCesChassisIOMStatusHealthEntry": cienaCesChassisIOMStatusHealthEntry,
       "cienaCesChassisIOMStatusHealthSubCategory": cienaCesChassisIOMStatusHealthSubCategory,
       "cienaCesChassisIOMStatusHealthOriginIndex": cienaCesChassisIOMStatusHealthOriginIndex,
       "cienaCesChassisIOMStatusHealthState": cienaCesChassisIOMStatusHealthState,
       "cienaCesChassisLinxStatHealthTable": cienaCesChassisLinxStatHealthTable,
       "cienaCesChassisLinxStatHealthEntry": cienaCesChassisLinxStatHealthEntry,
       "cienaCesChassisLinxStatHealthSubCategory": cienaCesChassisLinxStatHealthSubCategory,
       "cienaCesChassisLinxStatHealthOriginIndex": cienaCesChassisLinxStatHealthOriginIndex,
       "cienaCesChassisLinxStatHealthState": cienaCesChassisLinxStatHealthState,
       "cienaCesChassisLinxStatHealthCurrMeasurement": cienaCesChassisLinxStatHealthCurrMeasurement,
       "cienaCesChassisLinxStatHealthMaxMeasurement": cienaCesChassisLinxStatHealthMaxMeasurement,
       "cienaCesChassisLinxStatHealthMaxThreshold": cienaCesChassisLinxStatHealthMaxThreshold,
       "cienaCesChassisSMFabricHealthTable": cienaCesChassisSMFabricHealthTable,
       "cienaCesChassisSMFabricHealthEntry": cienaCesChassisSMFabricHealthEntry,
       "cienaCesChassisSMFabricHealthSubCategory": cienaCesChassisSMFabricHealthSubCategory,
       "cienaCesChassisSMFabricHealthOriginIndex": cienaCesChassisSMFabricHealthOriginIndex,
       "cienaCesChassisSMFabricHealthState": cienaCesChassisSMFabricHealthState,
       "cienaCesChassisSPIHealthTable": cienaCesChassisSPIHealthTable,
       "cienaCesChassisSPIHealthEntry": cienaCesChassisSPIHealthEntry,
       "cienaCesChassisSPIHealthSubCategory": cienaCesChassisSPIHealthSubCategory,
       "cienaCesChassisSPIHealthOriginIndex": cienaCesChassisSPIHealthOriginIndex,
       "cienaCesChassisSPIHealthState": cienaCesChassisSPIHealthState,
       "cienaCesChassisUsbFlashHealthTable": cienaCesChassisUsbFlashHealthTable,
       "cienaCesChassisUsbFlashHealthEntry": cienaCesChassisUsbFlashHealthEntry,
       "cienaCesChassisUsbFlashHealthSubCategory": cienaCesChassisUsbFlashHealthSubCategory,
       "cienaCesChassisUsbFlashHealthOriginIndex": cienaCesChassisUsbFlashHealthOriginIndex,
       "cienaCesChassisUsbFlashHealthState": cienaCesChassisUsbFlashHealthState,
       "cienaCesChassisIomTempHealthTable": cienaCesChassisIomTempHealthTable,
       "cienaCesChassisIomTempHealthEntry": cienaCesChassisIomTempHealthEntry,
       "cienaCesChassisIomTempHealthSubCategory": cienaCesChassisIomTempHealthSubCategory,
       "cienaCesChassisIomTempHealthOriginIndex": cienaCesChassisIomTempHealthOriginIndex,
       "cienaCesChassisIomTempHealthState": cienaCesChassisIomTempHealthState,
       "cienaCesChassisIomTempHealthCurrMeasurement": cienaCesChassisIomTempHealthCurrMeasurement,
       "cienaCesChassisIomTempHealthMinMeasurement": cienaCesChassisIomTempHealthMinMeasurement,
       "cienaCesChassisIomTempHealthMaxMeasurement": cienaCesChassisIomTempHealthMaxMeasurement,
       "cienaCesChassisIomTempHealthMinThreshold": cienaCesChassisIomTempHealthMinThreshold,
       "cienaCesChassisIomTempHealthMaxThreshold": cienaCesChassisIomTempHealthMaxThreshold,
       "cienaCesChassisPowerParamsHealthTable": cienaCesChassisPowerParamsHealthTable,
       "cienaCesChassisPowerParamsHealthEntry": cienaCesChassisPowerParamsHealthEntry,
       "cienaCesChassisPowerParamsHealthSubCategory": cienaCesChassisPowerParamsHealthSubCategory,
       "cienaCesChassisPowerParamsHealthOriginIndex": cienaCesChassisPowerParamsHealthOriginIndex,
       "cienaCesChassisPowerParamsHealthState": cienaCesChassisPowerParamsHealthState,
       "cienaCesChassisPowerOutputVoltageHealthTable": cienaCesChassisPowerOutputVoltageHealthTable,
       "cienaCesChassisPowerOutputVoltageHealthEntry": cienaCesChassisPowerOutputVoltageHealthEntry,
       "cienaCesChassisPowerOutputVoltageHealthSubCategory": cienaCesChassisPowerOutputVoltageHealthSubCategory,
       "cienaCesChassisPowerOutputVoltageHealthOriginIndex": cienaCesChassisPowerOutputVoltageHealthOriginIndex,
       "cienaCesChassisPowerOutputVoltageHealthState": cienaCesChassisPowerOutputVoltageHealthState,
       "cienaCesChassisPowerOutputVoltageHealthCurrMeasurement": cienaCesChassisPowerOutputVoltageHealthCurrMeasurement,
       "cienaCesChassisPowerOutputVoltageHealthMinMeasurement": cienaCesChassisPowerOutputVoltageHealthMinMeasurement,
       "cienaCesChassisPowerOutputVoltageHealthMaxMeasurement": cienaCesChassisPowerOutputVoltageHealthMaxMeasurement,
       "cienaCesChassisPowerOutputVoltageHealthMinThreshold": cienaCesChassisPowerOutputVoltageHealthMinThreshold,
       "cienaCesChassisPowerOutputVoltageHealthMaxThreshold": cienaCesChassisPowerOutputVoltageHealthMaxThreshold,
       "cienaCesChassisModemTempHealthTable": cienaCesChassisModemTempHealthTable,
       "cienaCesChassisModemTempHealthEntry": cienaCesChassisModemTempHealthEntry,
       "cienaCesChassisModemTempHealthSubCategory": cienaCesChassisModemTempHealthSubCategory,
       "cienaCesChassisModemTempHealthOriginIndex": cienaCesChassisModemTempHealthOriginIndex,
       "cienaCesChassisModemTempHealthState": cienaCesChassisModemTempHealthState,
       "cienaCesChassisModemTempHealthCurrMeasurement": cienaCesChassisModemTempHealthCurrMeasurement,
       "cienaCesChassisModemTempHealthMinMeasurement": cienaCesChassisModemTempHealthMinMeasurement,
       "cienaCesChassisModemTempHealthMaxMeasurement": cienaCesChassisModemTempHealthMaxMeasurement,
       "cienaCesChassisModemTempHealthMinThreshold": cienaCesChassisModemTempHealthMinThreshold,
       "cienaCesChassisModemTempHealthMaxThreshold": cienaCesChassisModemTempHealthMaxThreshold,
       "cienaCesChassisModemWatermarkHealthTable": cienaCesChassisModemWatermarkHealthTable,
       "cienaCesChassisModemWatermarkHealthEntry": cienaCesChassisModemWatermarkHealthEntry,
       "cienaCesChassisModemWatermarkHealthSubCategory": cienaCesChassisModemWatermarkHealthSubCategory,
       "cienaCesChassisModemWatermarkHealthOriginIndex": cienaCesChassisModemWatermarkHealthOriginIndex,
       "cienaCesChassisModemWatermarkHealthState": cienaCesChassisModemWatermarkHealthState,
       "cienaCesChassisFileDescriptorHealthTable": cienaCesChassisFileDescriptorHealthTable,
       "cienaCesChassisFileDescriptorHealthEntry": cienaCesChassisFileDescriptorHealthEntry,
       "cienaCesChassisFileDescriptorHealthSubCategory": cienaCesChassisFileDescriptorHealthSubCategory,
       "cienaCesChassisFileDescriptorHealthOriginIndex": cienaCesChassisFileDescriptorHealthOriginIndex,
       "cienaCesChassisFileDescriptorHealthState": cienaCesChassisFileDescriptorHealthState,
       "cienaCesChassisFileDescriptorHealthCurrMeasurement": cienaCesChassisFileDescriptorHealthCurrMeasurement,
       "cienaCesChassisFileDescriptorHealthMaxMeasurement": cienaCesChassisFileDescriptorHealthMaxMeasurement,
       "cienaCesChassisFileDescriptorHealthMaxThreshold": cienaCesChassisFileDescriptorHealthMaxThreshold,
       "cienaCesChassisProcessHealthTable": cienaCesChassisProcessHealthTable,
       "cienaCesChassisProcessHealthEntry": cienaCesChassisProcessHealthEntry,
       "cienaCesChassisProcessHealthSubCategory": cienaCesChassisProcessHealthSubCategory,
       "cienaCesChassisProcessHealthOriginIndex": cienaCesChassisProcessHealthOriginIndex,
       "cienaCesChassisProcessHealthState": cienaCesChassisProcessHealthState,
       "cienaCesChassisProcessHealthCurrMeasurement": cienaCesChassisProcessHealthCurrMeasurement,
       "cienaCesChassisProcessHealthMaxMeasurement": cienaCesChassisProcessHealthMaxMeasurement,
       "cienaCesChassisProcessHealthMaxThreshold": cienaCesChassisProcessHealthMaxThreshold,
       "cienaCesChassisThreadHealthTable": cienaCesChassisThreadHealthTable,
       "cienaCesChassisThreadHealthEntry": cienaCesChassisThreadHealthEntry,
       "cienaCesChassisThreadHealthSubCategory": cienaCesChassisThreadHealthSubCategory,
       "cienaCesChassisThreadHealthOriginIndex": cienaCesChassisThreadHealthOriginIndex,
       "cienaCesChassisThreadHealthState": cienaCesChassisThreadHealthState,
       "cienaCesChassisThreadHealthCurrMeasurement": cienaCesChassisThreadHealthCurrMeasurement,
       "cienaCesChassisThreadHealthMaxMeasurement": cienaCesChassisThreadHealthMaxMeasurement,
       "cienaCesChassisThreadHealthMaxThreshold": cienaCesChassisThreadHealthMaxThreshold,
       "cienaCesChassisIDP": cienaCesChassisIDP,
       "cienaCesChassisIDPEthBaseMac": cienaCesChassisIDPEthBaseMac,
       "cienaCesChassisIDPEthBaseMacRange": cienaCesChassisIDPEthBaseMacRange,
       "cienaCesChassisIDPModuleSerialNumber": cienaCesChassisIDPModuleSerialNumber,
       "cienaCesChassisIDPModelPartNumber": cienaCesChassisIDPModelPartNumber,
       "cienaCesChassisIDPModelRevision": cienaCesChassisIDPModelRevision,
       "cienaCesChassisIDPProductID": cienaCesChassisIDPProductID,
       "cienaCesChassisIDPMfgDate": cienaCesChassisIDPMfgDate,
       "cienaCesChassisIDPCleiCode": cienaCesChassisIDPCleiCode,
       "cienaCesChassisIDPBarcode": cienaCesChassisIDPBarcode,
       "cienaCesChassisIDPSWCompat": cienaCesChassisIDPSWCompat,
       "cienaCesChassisIDPFTC": cienaCesChassisIDPFTC,
       "cienaCesChassisIOM": cienaCesChassisIOM,
       "cienaCesChassisIOMState": cienaCesChassisIOMState,
       "cienaCesChassisIOMBuzzerEnable": cienaCesChassisIOMBuzzerEnable,
       "cienaCesChassisIOMBuzzerState": cienaCesChassisIOMBuzzerState,
       "cienaCesChassisIOMAlarmOutputTable": cienaCesChassisIOMAlarmOutputTable,
       "cienaCesChassisIOMAlarmOutputEntry": cienaCesChassisIOMAlarmOutputEntry,
       "cienaCesChassisIOMAlarmOutputIndex": cienaCesChassisIOMAlarmOutputIndex,
       "cienaCesChassisIOMAlarmOutputDescription": cienaCesChassisIOMAlarmOutputDescription,
       "cienaCesChassisIOMAlarmOutputState": cienaCesChassisIOMAlarmOutputState,
       "cienaCesChassisIOMAlarmInputTable": cienaCesChassisIOMAlarmInputTable,
       "cienaCesChassisIOMAlarmInputEntry": cienaCesChassisIOMAlarmInputEntry,
       "cienaCesChassisIOMAlarmInputIndex": cienaCesChassisIOMAlarmInputIndex,
       "cienaCesChassisIOMAlarmInputDescription": cienaCesChassisIOMAlarmInputDescription,
       "cienaCesChassisIOMAlarmInputState": cienaCesChassisIOMAlarmInputState,
       "cienaCesChassisIOMName": cienaCesChassisIOMName,
       "cienaCesChassisIOMChassisIndx": cienaCesChassisIOMChassisIndx,
       "cienaCesChassisIOMShelfIndx": cienaCesChassisIOMShelfIndx,
       "cienaCesChassisIOMSlotIndx": cienaCesChassisIOMSlotIndx,
       "cienaCesChassisIOMSerialNumber": cienaCesChassisIOMSerialNumber,
       "cienaCesChassisPlatform": cienaCesChassisPlatform,
       "cienaCesChassisPlatformType": cienaCesChassisPlatformType,
       "cienaCesChassisPlatformName": cienaCesChassisPlatformName,
       "cienaCesChassisPlatformDesc": cienaCesChassisPlatformDesc,
       "cienaCesChassisNumSlots": cienaCesChassisNumSlots,
       "cienaCesChassisPrimaryCtrlSlot": cienaCesChassisPrimaryCtrlSlot,
       "cienaCesChassisSecondaryCtrlSlot": cienaCesChassisSecondaryCtrlSlot,
       "cienaCesChassisNumFanTrays": cienaCesChassisNumFanTrays,
       "cienaCesChassisNumFansPerTray": cienaCesChassisNumFansPerTray,
       "cienaCesChassisDcPower": cienaCesChassisDcPower,
       "cienaCesChassisRedunPower": cienaCesChassisRedunPower,
       "cienaCesChassisPhysicalPortsMax": cienaCesChassisPhysicalPortsMax,
       "cienaCesChassisAggPortsMax": cienaCesChassisAggPortsMax,
       "cienaCesChassisVirtualSwitchMax": cienaCesChassisVirtualSwitchMax,
       "cienaCesChassisVirtualInterfaceMax": cienaCesChassisVirtualInterfaceMax,
       "cienaCesChassisMulticastGrpsMax": cienaCesChassisMulticastGrpsMax,
       "cienaCesChassisRstpDomainsMax": cienaCesChassisRstpDomainsMax,
       "cienaCesChassisVirtualInterfacePerVsMax": cienaCesChassisVirtualInterfacePerVsMax,
       "cienaCesChassisReplicPerPortPerVsMax": cienaCesChassisReplicPerPortPerVsMax,
       "cienaCesChassisReplicMCPortPerVsMax": cienaCesChassisReplicMCPortPerVsMax,
       "cienaCesChassisSubPortsMax": cienaCesChassisSubPortsMax,
       "cienaCesChassisQosFlowsMax": cienaCesChassisQosFlowsMax,
       "cienaCesChassisAccessFlowsMax": cienaCesChassisAccessFlowsMax,
       "cienaCesChassisCPUSubIntfcsMax": cienaCesChassisCPUSubIntfcsMax,
       "cienaCesChassisPBTTunnelGroupsMax": cienaCesChassisPBTTunnelGroupsMax,
       "cienaCesChassisPBTEncapTunnelsMax": cienaCesChassisPBTEncapTunnelsMax,
       "cienaCesChassisPBTDecapTunnelsMax": cienaCesChassisPBTDecapTunnelsMax,
       "cienaCesChassisPBTServiceIntfcsMax": cienaCesChassisPBTServiceIntfcsMax,
       "cienaCesChassisPBTTransitIntfcsMax": cienaCesChassisPBTTransitIntfcsMax,
       "cienaCesChassisMeterProfilesMax": cienaCesChassisMeterProfilesMax,
       "cienaCesChassisFloodContainersMax": cienaCesChassisFloodContainersMax,
       "cienaCesChassisRCOSProfilesMax": cienaCesChassisRCOSProfilesMax,
       "cienaCesChassisRCOSMappingsMax": cienaCesChassisRCOSMappingsMax,
       "cienaCesChassisFCOSMappingsMax": cienaCesChassisFCOSMappingsMax,
       "cienaCesChassisShapingProfilesMax": cienaCesChassisShapingProfilesMax,
       "cienaCesChassisMPLSTunnelGroupsMax": cienaCesChassisMPLSTunnelGroupsMax,
       "cienaCesChassisMPLSTunnelsPerGroupMax": cienaCesChassisMPLSTunnelsPerGroupMax,
       "cienaCesChassisMPLSEncapTunnelsMax": cienaCesChassisMPLSEncapTunnelsMax,
       "cienaCesChassisMPLSDecapTunnelsMax": cienaCesChassisMPLSDecapTunnelsMax,
       "cienaCesChassisMPLSVCMax": cienaCesChassisMPLSVCMax,
       "cienaCesChassisMPLSInterfacesMax": cienaCesChassisMPLSInterfacesMax,
       "cienaCesChassisMPLSTransitTunnelsMax": cienaCesChassisMPLSTransitTunnelsMax,
       "cienaCesChassisRedundancyGroupsMax": cienaCesChassisRedundancyGroupsMax,
       "cienaCesChassisLinksPerRedundancyGroupMax": cienaCesChassisLinksPerRedundancyGroupMax,
       "cienaCesChassisMIBConformance": cienaCesChassisMIBConformance,
       "cienaCesChassisMIBCompliances": cienaCesChassisMIBCompliances,
       "cienaCesChassisMIBGroups": cienaCesChassisMIBGroups,
       "chassisGlobalGroup": chassisGlobalGroup,
       "chassisPlatformGroup": chassisPlatformGroup,
       "chassisPowerSupplyGroup": chassisPowerSupplyGroup,
       "chassisFanGroup": chassisFanGroup,
       "chassisFanTrayGroup": chassisFanTrayGroup,
       "chassisFanTempGroup": chassisFanTempGroup,
       "chassisNotifGroup": chassisNotifGroup,
       "chassisHealthGroup": chassisHealthGroup,
       "chassisIomStateGroup": chassisIomStateGroup,
       "chassisIomNotifGroup": chassisIomNotifGroup,
       "cienaCesChassisMIBNotificationPrefix": cienaCesChassisMIBNotificationPrefix,
       "cienaCesChassisMIBNotifications": cienaCesChassisMIBNotifications,
       "cienaCesChassisPowerSupplyFaultedNotification": cienaCesChassisPowerSupplyFaultedNotification,
       "cienaCesChassisPowerSupplyOnlineNotification": cienaCesChassisPowerSupplyOnlineNotification,
       "cienaCesChassisFanHiTempNotification": cienaCesChassisFanHiTempNotification,
       "cienaCesChassisFanNormalTempNotification": cienaCesChassisFanNormalTempNotification,
       "cienaCesChassisFanLoTempNotification": cienaCesChassisFanLoTempNotification,
       "cienaCesChassisFanSpeedMinThresholdNotification": cienaCesChassisFanSpeedMinThresholdNotification,
       "cienaCesChassisFanSpeedNormalRangeNotification": cienaCesChassisFanSpeedNormalRangeNotification,
       "cienaCesChassisFanTrayRemoveNotification": cienaCesChassisFanTrayRemoveNotification,
       "cienaCesChassisFanTrayInsertNotification": cienaCesChassisFanTrayInsertNotification,
       "cienaCesChassisFanTrayStatusFaultedNotification": cienaCesChassisFanTrayStatusFaultedNotification,
       "cienaCesChassisFanTrayStatusOkNotification": cienaCesChassisFanTrayStatusOkNotification,
       "cienaCesChassisHealthStatusUnknownNotification": cienaCesChassisHealthStatusUnknownNotification,
       "cienaCesChassisHealthStatusWarningNotification": cienaCesChassisHealthStatusWarningNotification,
       "cienaCesChassisHealthStatusFaultedNotification": cienaCesChassisHealthStatusFaultedNotification,
       "cienaCesChassisHealthStatusDegradedNotification": cienaCesChassisHealthStatusDegradedNotification,
       "cienaCesChassisHealthStatusGoodNotification": cienaCesChassisHealthStatusGoodNotification,
       "cienaCesChassisRebootNotification": cienaCesChassisRebootNotification,
       "cienaCesChassisIOMStateChangeNotification": cienaCesChassisIOMStateChangeNotification,
       "cienaCesChassisIOMBuzzerEnableChangeNotification": cienaCesChassisIOMBuzzerEnableChangeNotification,
       "cienaCesChassisIOMBuzzerStateChangeNotification": cienaCesChassisIOMBuzzerStateChangeNotification,
       "cienaCesChassisIOMAlarmOutputStateChangeNotification": cienaCesChassisIOMAlarmOutputStateChangeNotification,
       "cienaCesChassisIOMAlarmInputStateChangeNotification": cienaCesChassisIOMAlarmInputStateChangeNotification,
       "cienaCesChassisUsbFlashEnabledNotification": cienaCesChassisUsbFlashEnabledNotification,
       "cienaCesChassisUsbFlashDisabledNotification": cienaCesChassisUsbFlashDisabledNotification,
       "cienaCesChassisAirFilterServiceNotification": cienaCesChassisAirFilterServiceNotification,
       "cienaCesChassisAlarmCutoffNotification": cienaCesChassisAlarmCutoffNotification,
       "cienaCesChassisDyingGaspNotification": cienaCesChassisDyingGaspNotification}
)
