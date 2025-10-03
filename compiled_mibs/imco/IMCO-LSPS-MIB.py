# SNMP MIB module (IMCO-LSPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\imco\IMCO-LSPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:30 2025
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mib_AN_Dcz_SDS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33283)
)
if mibBuilder.loadTexts:
    mib_AN_Dcz_SDS.setRevisions(
        ("2017-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sdsxpublic_ObjectIdentity = ObjectIdentity
sdsxpublic = _Sdsxpublic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1)
)
_SdsBIGandSTSW_ObjectIdentity = ObjectIdentity
sdsBIGandSTSW = _SdsBIGandSTSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30)
)
_SdsOptoInput_ObjectIdentity = ObjectIdentity
sdsOptoInput = _SdsOptoInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 2)
)


class _Opto1_Type(Integer32):
    """Custom type opto1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("activeSignalPresent", 0),
          ("noSignal", 32768))
    )


_Opto1_Type.__name__ = "Integer32"
_Opto1_Object = MibScalar
opto1 = _Opto1_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 1),
    _Opto1_Type()
)
opto1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opto1.setStatus("current")


class _Opto2_Type(Integer32):
    """Custom type opto2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activeSignalPresent", 0),
          ("noSignal", 1))
    )


_Opto2_Type.__name__ = "Integer32"
_Opto2_Object = MibScalar
opto2 = _Opto2_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 2),
    _Opto2_Type()
)
opto2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opto2.setStatus("current")


class _Opto3_Type(Integer32):
    """Custom type opto3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeSignalPresent", 0),
          ("noSignal", 2))
    )


_Opto3_Type.__name__ = "Integer32"
_Opto3_Object = MibScalar
opto3 = _Opto3_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 2, 3),
    _Opto3_Type()
)
opto3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opto3.setStatus("current")
_SdsOutputRelays_ObjectIdentity = ObjectIdentity
sdsOutputRelays = _SdsOutputRelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3)
)
_SdsOutputRelay1_ObjectIdentity = ObjectIdentity
sdsOutputRelay1 = _SdsOutputRelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1)
)


class _SdsRE1state_Type(Integer32):
    """Custom type sdsRE1state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 255))
    )


_SdsRE1state_Type.__name__ = "Integer32"
_SdsRE1state_Object = MibScalar
sdsRE1state = _SdsRE1state_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 1, 1),
    _SdsRE1state_Type()
)
sdsRE1state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdsRE1state.setStatus("current")
_SdsOutputRelay2_ObjectIdentity = ObjectIdentity
sdsOutputRelay2 = _SdsOutputRelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2)
)


class _SdsRE2state_Type(Integer32):
    """Custom type sdsRE2state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 255))
    )


_SdsRE2state_Type.__name__ = "Integer32"
_SdsRE2state_Object = MibScalar
sdsRE2state = _SdsRE2state_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 2, 1),
    _SdsRE2state_Type()
)
sdsRE2state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdsRE2state.setStatus("current")
_SdsOutputRelay3_ObjectIdentity = ObjectIdentity
sdsOutputRelay3 = _SdsOutputRelay3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3)
)


class _SdsRE3state_Type(Integer32):
    """Custom type sdsRE3state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("activated", 255))
    )


_SdsRE3state_Type.__name__ = "Integer32"
_SdsRE3state_Object = MibScalar
sdsRE3state = _SdsRE3state_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 3, 3, 1),
    _SdsRE3state_Type()
)
sdsRE3state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdsRE3state.setStatus("current")
_SdsADCinputs_ObjectIdentity = ObjectIdentity
sdsADCinputs = _SdsADCinputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 5)
)
_SdsADCitem0_ObjectIdentity = ObjectIdentity
sdsADCitem0 = _SdsADCitem0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1)
)
_SdsTempSensValue_Type = Gauge32
_SdsTempSensValue_Object = MibScalar
sdsTempSensValue = _SdsTempSensValue_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 3),
    _SdsTempSensValue_Type()
)
sdsTempSensValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsTempSensValue.setStatus("current")
_SdsTempSensName_Type = OctetString
_SdsTempSensName_Object = MibScalar
sdsTempSensName = _SdsTempSensName_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 5, 1, 4),
    _SdsTempSensName_Type()
)
sdsTempSensName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsTempSensName.setStatus("current")
_SdsADCvalues_ObjectIdentity = ObjectIdentity
sdsADCvalues = _SdsADCvalues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7)
)
_SdsMaximumLoad_Type = Integer32
_SdsMaximumLoad_Object = MibScalar
sdsMaximumLoad = _SdsMaximumLoad_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 2),
    _SdsMaximumLoad_Type()
)
sdsMaximumLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsMaximumLoad.setStatus("current")
_SdsAlarmText_Type = OctetString
_SdsAlarmText_Object = MibScalar
sdsAlarmText = _SdsAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 3),
    _SdsAlarmText_Type()
)
sdsAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsAlarmText.setStatus("current")
_SdsOutputVoltage1_Type = Integer32
_SdsOutputVoltage1_Object = MibScalar
sdsOutputVoltage1 = _SdsOutputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 4),
    _SdsOutputVoltage1_Type()
)
sdsOutputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsOutputVoltage1.setStatus("current")
_SdsOutputVoltage2_Type = Integer32
_SdsOutputVoltage2_Object = MibScalar
sdsOutputVoltage2 = _SdsOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 5),
    _SdsOutputVoltage2_Type()
)
sdsOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsOutputVoltage2.setStatus("current")
_SdsOutputCurrent_Type = Integer32
_SdsOutputCurrent_Object = MibScalar
sdsOutputCurrent = _SdsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 6),
    _SdsOutputCurrent_Type()
)
sdsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsOutputCurrent.setStatus("current")
_SdsBatteryCapacity_Type = Integer32
_SdsBatteryCapacity_Object = MibScalar
sdsBatteryCapacity = _SdsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 7),
    _SdsBatteryCapacity_Type()
)
sdsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsBatteryCapacity.setStatus("current")
_SdsLoad_Type = Integer32
_SdsLoad_Object = MibScalar
sdsLoad = _SdsLoad_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 8),
    _SdsLoad_Type()
)
sdsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsLoad.setStatus("current")
_SdsCapTestTime_Type = Integer32
_SdsCapTestTime_Object = MibScalar
sdsCapTestTime = _SdsCapTestTime_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 7, 9),
    _SdsCapTestTime_Type()
)
sdsCapTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsCapTestTime.setStatus("current")
_SdsGeneralInfoEntry_ObjectIdentity = ObjectIdentity
sdsGeneralInfoEntry = _SdsGeneralInfoEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8)
)
_SdsManufacturer_Type = OctetString
_SdsManufacturer_Object = MibScalar
sdsManufacturer = _SdsManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 80),
    _SdsManufacturer_Type()
)
sdsManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsManufacturer.setStatus("current")
_SdsModel_Type = OctetString
_SdsModel_Object = MibScalar
sdsModel = _SdsModel_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 81),
    _SdsModel_Type()
)
sdsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsModel.setStatus("current")
_SdsName_Type = OctetString
_SdsName_Object = MibScalar
sdsName = _SdsName_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 82),
    _SdsName_Type()
)
sdsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsName.setStatus("current")
_SdsSerialNumber_Type = OctetString
_SdsSerialNumber_Object = MibScalar
sdsSerialNumber = _SdsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 83),
    _SdsSerialNumber_Type()
)
sdsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsSerialNumber.setStatus("current")
_SdsSoftware_Type = OctetString
_SdsSoftware_Object = MibScalar
sdsSoftware = _SdsSoftware_Object(
    (1, 3, 6, 1, 4, 1, 33283, 1, 30, 8, 84),
    _SdsSoftware_Type()
)
sdsSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdsSoftware.setStatus("current")

# Managed Objects groups


# Notification objects

opto1_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 100)
)
opto1_trap.setObjects(
    ("IMCO-LSPS-MIB", "opto1")
)
if mibBuilder.loadTexts:
    opto1_trap.setStatus(
        ""
    )

opto2_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 101)
)
opto2_trap.setObjects(
    ("IMCO-LSPS-MIB", "opto2")
)
if mibBuilder.loadTexts:
    opto2_trap.setStatus(
        ""
    )

opto3_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 102)
)
opto3_trap.setObjects(
    ("IMCO-LSPS-MIB", "opto3")
)
if mibBuilder.loadTexts:
    opto3_trap.setStatus(
        ""
    )

sdsRE1state_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 150)
)
sdsRE1state_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsRE1state")
)
if mibBuilder.loadTexts:
    sdsRE1state_trap.setStatus(
        ""
    )

sdsRE2state_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 153)
)
sdsRE2state_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsRE2state")
)
if mibBuilder.loadTexts:
    sdsRE2state_trap.setStatus(
        ""
    )

sdsTempSensValue_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 222)
)
sdsTempSensValue_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsTempSensValue")
)
if mibBuilder.loadTexts:
    sdsTempSensValue_trap.setStatus(
        ""
    )

sdsTempSensName_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 223)
)
sdsTempSensName_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsTempSensName")
)
if mibBuilder.loadTexts:
    sdsTempSensName_trap.setStatus(
        ""
    )

sdsMaximumLoad_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 401)
)
sdsMaximumLoad_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsMaximumLoad")
)
if mibBuilder.loadTexts:
    sdsMaximumLoad_trap.setStatus(
        ""
    )

sdsAlarmText_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 402)
)
sdsAlarmText_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsAlarmText")
)
if mibBuilder.loadTexts:
    sdsAlarmText_trap.setStatus(
        ""
    )

sdsOutputVoltage1_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 403)
)
sdsOutputVoltage1_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsOutputVoltage1")
)
if mibBuilder.loadTexts:
    sdsOutputVoltage1_trap.setStatus(
        ""
    )

sdsOutputVoltage2_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 404)
)
sdsOutputVoltage2_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsOutputVoltage2")
)
if mibBuilder.loadTexts:
    sdsOutputVoltage2_trap.setStatus(
        ""
    )

sdsOutputCurrent_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 405)
)
sdsOutputCurrent_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsOutputCurrent")
)
if mibBuilder.loadTexts:
    sdsOutputCurrent_trap.setStatus(
        ""
    )

sdsBatteryCapacity_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 406)
)
sdsBatteryCapacity_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsBatteryCapacity")
)
if mibBuilder.loadTexts:
    sdsBatteryCapacity_trap.setStatus(
        ""
    )

sdsLoad_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 407)
)
sdsLoad_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsLoad")
)
if mibBuilder.loadTexts:
    sdsLoad_trap.setStatus(
        ""
    )

sdsCapTestTime_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 33283, 0, 408)
)
sdsCapTestTime_trap.setObjects(
    ("IMCO-LSPS-MIB", "sdsCapTestTime")
)
if mibBuilder.loadTexts:
    sdsCapTestTime_trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMCO-LSPS-MIB",
    **{"mib-AN-Dcz-SDS": mib_AN_Dcz_SDS,
       "opto1-trap": opto1_trap,
       "opto2-trap": opto2_trap,
       "opto3-trap": opto3_trap,
       "sdsRE1state-trap": sdsRE1state_trap,
       "sdsRE2state-trap": sdsRE2state_trap,
       "sdsTempSensValue-trap": sdsTempSensValue_trap,
       "sdsTempSensName-trap": sdsTempSensName_trap,
       "sdsMaximumLoad-trap": sdsMaximumLoad_trap,
       "sdsAlarmText-trap": sdsAlarmText_trap,
       "sdsOutputVoltage1-trap": sdsOutputVoltage1_trap,
       "sdsOutputVoltage2-trap": sdsOutputVoltage2_trap,
       "sdsOutputCurrent-trap": sdsOutputCurrent_trap,
       "sdsBatteryCapacity-trap": sdsBatteryCapacity_trap,
       "sdsLoad-trap": sdsLoad_trap,
       "sdsCapTestTime-trap": sdsCapTestTime_trap,
       "sdsxpublic": sdsxpublic,
       "sdsBIGandSTSW": sdsBIGandSTSW,
       "sdsOptoInput": sdsOptoInput,
       "opto1": opto1,
       "opto2": opto2,
       "opto3": opto3,
       "sdsOutputRelays": sdsOutputRelays,
       "sdsOutputRelay1": sdsOutputRelay1,
       "sdsRE1state": sdsRE1state,
       "sdsOutputRelay2": sdsOutputRelay2,
       "sdsRE2state": sdsRE2state,
       "sdsOutputRelay3": sdsOutputRelay3,
       "sdsRE3state": sdsRE3state,
       "sdsADCinputs": sdsADCinputs,
       "sdsADCitem0": sdsADCitem0,
       "sdsTempSensValue": sdsTempSensValue,
       "sdsTempSensName": sdsTempSensName,
       "sdsADCvalues": sdsADCvalues,
       "sdsMaximumLoad": sdsMaximumLoad,
       "sdsAlarmText": sdsAlarmText,
       "sdsOutputVoltage1": sdsOutputVoltage1,
       "sdsOutputVoltage2": sdsOutputVoltage2,
       "sdsOutputCurrent": sdsOutputCurrent,
       "sdsBatteryCapacity": sdsBatteryCapacity,
       "sdsLoad": sdsLoad,
       "sdsCapTestTime": sdsCapTestTime,
       "sdsGeneralInfoEntry": sdsGeneralInfoEntry,
       "sdsManufacturer": sdsManufacturer,
       "sdsModel": sdsModel,
       "sdsName": sdsName,
       "sdsSerialNumber": sdsSerialNumber,
       "sdsSoftware": sdsSoftware}
)
