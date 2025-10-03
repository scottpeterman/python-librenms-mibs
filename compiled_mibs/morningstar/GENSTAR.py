# SNMP MIB module (GENSTAR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\morningstar\GENSTAR
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:51 2025
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

(morningstar,) = mibBuilder.importSymbols(
    "MORNINGSTAR",
    "morningstar")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

genStar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33333, 10)
)
if mibBuilder.loadTexts:
    genStar.setRevisions(
        ("2023-11-29 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChargeStateEnum(TextualConvention, Integer32):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("starting", 0),
          ("nightCheck", 1),
          ("disconnected", 2),
          ("night", 3),
          ("fault", 4),
          ("bulk", 5),
          ("absorption", 6),
          ("float", 7),
          ("equalize", 8))
    )



class LoadStateEnum(TextualConvention, Integer32):
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
        *(("start", 0),
          ("norm", 1),
          ("lvdwarn", 2),
          ("lvd", 3),
          ("fault", 4),
          ("disc", 5),
          ("norm-off", 6),
          ("override", 7))
    )



class LoadFaultBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("load-software", 0),
          ("load-overcurrent", 1),
          ("load-ex-short", 2),
          ("load-power-supply", 3),
          ("load-hvd", 4),
          ("load-heatsink-overtemp", 5),
          ("load-fet-shorted", 6))
    )


class FaultBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("system-eeprom", 0),
          ("software", 2),
          ("no-model", 3),
          ("system-setting-edit", 6),
          ("system-bms", 8),
          ("reset", 10),
          ("adc-ovr", 15),
          ("adc-no-inj-update", 16),
          ("adc-double-update", 17),
          ("battery-shunt-missing", 18),
          ("system-setting-bad", 29),
          ("hardware", 30))
    )


class AlarmBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rts-open", 0),
          ("rts-short", 1),
          ("rts-disc", 2),
          ("ths-open", 3),
          ("ths-short", 4),
          ("ths-hot", 5),
          ("i-limit", 6),
          ("ibatt-offset", 7),
          ("batt-sense", 8),
          ("batt-sense-disconnect", 9),
          ("uncal", 10),
          ("rts-5v", 11),
          ("factory", 13),
          ("soc-invalid", 14),
          ("va-high", 17),
          ("ia-offset", 23),
          ("eeprom", 24),
          ("ethernet", 25),
          ("load-lvd", 26),
          ("software", 27),
          ("extflash", 29),
          ("i-l-offset", 32),
          ("rtc-lowbatt", 33),
          ("rtc-wrong", 35),
          ("rtc-hardware", 36),
          ("tindcasting-open", 37),
          ("tindcasting-short", 38),
          ("tindcasting-hot", 39),
          ("wireless-fail", 41),
          ("hardware", 42),
          ("unknown-blocktype", 43),
          ("block1-hardware", 44),
          ("block2-hardware", 45),
          ("block3-hardware", 46),
          ("block4-hardware", 47),
          ("block5-hardware", 48),
          ("block6-hardware", 49),
          ("genstart-primary-fail", 50),
          ("genstart-secondary-fail", 51),
          ("schedule-publisher-fail", 52),
          ("uncal-up", 53),
          ("i-load-offset", 54),
          ("load-fet-open", 55),
          ("bms-sense", 56),
          ("bms-sense-disconnect", 57))
    )


class ChargeFaultBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("charge-software", 0),
          ("charge-batt-hvd", 1),
          ("charge-rts-short", 2),
          ("charge-rts-disc", 3),
          ("charge-slave-to", 4))
    )


class FaultPowersupplyBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("p12", 0),
          ("p5", 1),
          ("p3", 2),
          ("arrayn3", 4),
          ("battn3", 6),
          ("p12-extbb", 7),
          ("p3-extbb", 8),
          ("arrayp10", 9),
          ("battp10", 10))
    )


class BlockFaultBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("block1-missing", 0),
          ("block2-missing", 1),
          ("block3-missing", 2),
          ("block4-missing", 3),
          ("block5-missing", 4),
          ("block6-missing", 5),
          ("block1-remote-fault", 8),
          ("block2-remote-fault", 9),
          ("block3-remote-fault", 10),
          ("block4-remote-fault", 11),
          ("block5-remote-fault", 12),
          ("block6-remote-fault", 13),
          ("block1-hardware-version", 16),
          ("block2-hardware-version", 17),
          ("block3-hardware-version", 18),
          ("block4-hardware-version", 19),
          ("block5-hardware-version", 20),
          ("block6-hardware-version", 21),
          ("block1-fixable-fault", 24),
          ("block2-fixable-fault", 25),
          ("block3-fixable-fault", 26),
          ("block4-fixable-fault", 27),
          ("block5-fixable-fault", 28),
          ("block6-fixable-fault", 29))
    )


class FaultPowerstageBitfield(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("powerstage-overcurrent", 0),
          ("powerstage-fet-short", 1),
          ("powerstage-dn-short", 2),
          ("powerstage-batt-hvd", 3),
          ("powerstage-array-hvd", 4),
          ("powerstage-software", 5),
          ("powerstage-bad-setting", 6),
          ("powerstage-batt-lvd", 7),
          ("powerstage-power-supply", 8),
          ("powerstage-h7rev", 9),
          ("powerstage-hwrev", 10),
          ("powerstage-inductor-temp", 11),
          ("powerstage-hs-temp", 12),
          ("powerstage-inductor-offset", 13),
          ("powerstage-array-offset", 14),
          ("powerstage-misc", 15))
    )


# MIB Managed Objects in the order of their OIDs



class _SubModel_Type(DisplayString):
    """Custom type subModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SubModel_Type.__name__ = "DisplayString"
_SubModel_Object = MibScalar
subModel = _SubModel_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 1),
    _SubModel_Type()
)
subModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subModel.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _DeviceVersion_Type(DisplayString):
    """Custom type deviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DeviceVersion_Type.__name__ = "DisplayString"
_DeviceVersion_Object = MibScalar
deviceVersion = _DeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 3),
    _DeviceVersion_Type()
)
deviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVersion.setStatus("current")


class _Vbterm_Type(DisplayString):
    """Custom type vbterm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Vbterm_Type.__name__ = "DisplayString"
_Vbterm_Object = MibScalar
vbterm = _Vbterm_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 30),
    _Vbterm_Type()
)
vbterm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbterm.setStatus("current")


class _Vload_Type(DisplayString):
    """Custom type vload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Vload_Type.__name__ = "DisplayString"
_Vload_Object = MibScalar
vload = _Vload_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 31),
    _Vload_Type()
)
vload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vload.setStatus("current")


class _Vbsense_Type(DisplayString):
    """Custom type vbsense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Vbsense_Type.__name__ = "DisplayString"
_Vbsense_Object = MibScalar
vbsense = _Vbsense_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 32),
    _Vbsense_Type()
)
vbsense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbsense.setStatus("current")


class _VCoin_Type(DisplayString):
    """Custom type vCoin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VCoin_Type.__name__ = "DisplayString"
_VCoin_Object = MibScalar
vCoin = _VCoin_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 33),
    _VCoin_Type()
)
vCoin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCoin.setStatus("current")


class _SystemIcharge_Type(DisplayString):
    """Custom type systemIcharge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemIcharge_Type.__name__ = "DisplayString"
_SystemIcharge_Object = MibScalar
systemIcharge = _SystemIcharge_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 34),
    _SystemIcharge_Type()
)
systemIcharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIcharge.setStatus("current")


class _SystemIload_Type(DisplayString):
    """Custom type systemIload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemIload_Type.__name__ = "DisplayString"
_SystemIload_Object = MibScalar
systemIload = _SystemIload_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 35),
    _SystemIload_Type()
)
systemIload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIload.setStatus("current")


class _TempBatt_Type(DisplayString):
    """Custom type tempBatt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TempBatt_Type.__name__ = "DisplayString"
_TempBatt_Object = MibScalar
tempBatt = _TempBatt_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 36),
    _TempBatt_Type()
)
tempBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempBatt.setStatus("current")


class _TempRts_Type(DisplayString):
    """Custom type tempRts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TempRts_Type.__name__ = "DisplayString"
_TempRts_Object = MibScalar
tempRts = _TempRts_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 37),
    _TempRts_Type()
)
tempRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempRts.setStatus("current")


class _TempHeatsink_Type(DisplayString):
    """Custom type tempHeatsink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TempHeatsink_Type.__name__ = "DisplayString"
_TempHeatsink_Object = MibScalar
tempHeatsink = _TempHeatsink_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 38),
    _TempHeatsink_Type()
)
tempHeatsink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHeatsink.setStatus("current")
_ChargeState_Type = ChargeStateEnum
_ChargeState_Object = MibScalar
chargeState = _ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 39),
    _ChargeState_Type()
)
chargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeState.setStatus("current")


class _VbattRefCharge_Type(DisplayString):
    """Custom type vbattRefCharge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbattRefCharge_Type.__name__ = "DisplayString"
_VbattRefCharge_Object = MibScalar
vbattRefCharge = _VbattRefCharge_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 40),
    _VbattRefCharge_Type()
)
vbattRefCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbattRefCharge.setStatus("current")


class _BattSoc_Type(DisplayString):
    """Custom type battSoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BattSoc_Type.__name__ = "DisplayString"
_BattSoc_Object = MibScalar
battSoc = _BattSoc_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 41),
    _BattSoc_Type()
)
battSoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battSoc.setStatus("current")


class _VbattMin_Type(DisplayString):
    """Custom type vbattMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbattMin_Type.__name__ = "DisplayString"
_VbattMin_Object = MibScalar
vbattMin = _VbattMin_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 42),
    _VbattMin_Type()
)
vbattMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbattMin.setStatus("current")


class _VbattMax_Type(DisplayString):
    """Custom type vbattMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbattMax_Type.__name__ = "DisplayString"
_VbattMax_Object = MibScalar
vbattMax = _VbattMax_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 43),
    _VbattMax_Type()
)
vbattMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbattMax.setStatus("current")


class _BattSocMinDaily_Type(DisplayString):
    """Custom type battSocMinDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BattSocMinDaily_Type.__name__ = "DisplayString"
_BattSocMinDaily_Object = MibScalar
battSocMinDaily = _BattSocMinDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 44),
    _BattSocMinDaily_Type()
)
battSocMinDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battSocMinDaily.setStatus("current")


class _BattSocMaxDaily_Type(DisplayString):
    """Custom type battSocMaxDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BattSocMaxDaily_Type.__name__ = "DisplayString"
_BattSocMaxDaily_Object = MibScalar
battSocMaxDaily = _BattSocMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 45),
    _BattSocMaxDaily_Type()
)
battSocMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    battSocMaxDaily.setStatus("current")
_LoadState_Type = LoadStateEnum
_LoadState_Object = MibScalar
loadState = _LoadState_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 46),
    _LoadState_Type()
)
loadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadState.setStatus("current")
_LoadFault_Type = LoadFaultBitfield
_LoadFault_Object = MibScalar
loadFault = _LoadFault_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 47),
    _LoadFault_Type()
)
loadFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFault.setStatus("current")
_LoadFaultDaily_Type = LoadFaultBitfield
_LoadFaultDaily_Object = MibScalar
loadFaultDaily = _LoadFaultDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 48),
    _LoadFaultDaily_Type()
)
loadFaultDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFaultDaily.setStatus("current")
_Fault_Type = FaultBitfield
_Fault_Object = MibScalar
fault = _Fault_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 49),
    _Fault_Type()
)
fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fault.setStatus("current")
_FaultDaily_Type = FaultBitfield
_FaultDaily_Object = MibScalar
faultDaily = _FaultDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 50),
    _FaultDaily_Type()
)
faultDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDaily.setStatus("current")
_Alarm_Type = AlarmBitfield
_Alarm_Object = MibScalar
alarm = _Alarm_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 51),
    _Alarm_Type()
)
alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm.setStatus("current")
_AlarmDaily_Type = AlarmBitfield
_AlarmDaily_Object = MibScalar
alarmDaily = _AlarmDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 52),
    _AlarmDaily_Type()
)
alarmDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDaily.setStatus("current")
_ChargeFault_Type = ChargeFaultBitfield
_ChargeFault_Object = MibScalar
chargeFault = _ChargeFault_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 53),
    _ChargeFault_Type()
)
chargeFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeFault.setStatus("current")
_ChargeFaultDaily_Type = ChargeFaultBitfield
_ChargeFaultDaily_Object = MibScalar
chargeFaultDaily = _ChargeFaultDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 54),
    _ChargeFaultDaily_Type()
)
chargeFaultDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargeFaultDaily.setStatus("current")
_FaultPowersupply_Type = FaultPowersupplyBitfield
_FaultPowersupply_Object = MibScalar
faultPowersupply = _FaultPowersupply_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 55),
    _FaultPowersupply_Type()
)
faultPowersupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultPowersupply.setStatus("current")
_FaultPowersupplyDaily_Type = FaultPowersupplyBitfield
_FaultPowersupplyDaily_Object = MibScalar
faultPowersupplyDaily = _FaultPowersupplyDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 56),
    _FaultPowersupplyDaily_Type()
)
faultPowersupplyDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultPowersupplyDaily.setStatus("current")
_BlockFault_Type = BlockFaultBitfield
_BlockFault_Object = MibScalar
blockFault = _BlockFault_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 57),
    _BlockFault_Type()
)
blockFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockFault.setStatus("current")
_BlockFaultDaily_Type = BlockFaultBitfield
_BlockFaultDaily_Object = MibScalar
blockFaultDaily = _BlockFaultDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 58),
    _BlockFaultDaily_Type()
)
blockFaultDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockFaultDaily.setStatus("current")
_FaultPowerstage_Type = FaultPowerstageBitfield
_FaultPowerstage_Object = MibScalar
faultPowerstage = _FaultPowerstage_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 59),
    _FaultPowerstage_Type()
)
faultPowerstage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultPowerstage.setStatus("current")
_FaultPowerstageDaily_Type = FaultPowerstageBitfield
_FaultPowerstageDaily_Object = MibScalar
faultPowerstageDaily = _FaultPowerstageDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 60),
    _FaultPowerstageDaily_Type()
)
faultPowerstageDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultPowerstageDaily.setStatus("current")


class _VbattMinDaily_Type(DisplayString):
    """Custom type vbattMinDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbattMinDaily_Type.__name__ = "DisplayString"
_VbattMinDaily_Object = MibScalar
vbattMinDaily = _VbattMinDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 61),
    _VbattMinDaily_Type()
)
vbattMinDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbattMinDaily.setStatus("current")


class _VbattMaxDaily_Type(DisplayString):
    """Custom type vbattMaxDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VbattMaxDaily_Type.__name__ = "DisplayString"
_VbattMaxDaily_Object = MibScalar
vbattMaxDaily = _VbattMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 62),
    _VbattMaxDaily_Type()
)
vbattMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbattMaxDaily.setStatus("current")


class _VarrayMaxDaily_Type(DisplayString):
    """Custom type varrayMaxDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VarrayMaxDaily_Type.__name__ = "DisplayString"
_VarrayMaxDaily_Object = MibScalar
varrayMaxDaily = _VarrayMaxDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 63),
    _VarrayMaxDaily_Type()
)
varrayMaxDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varrayMaxDaily.setStatus("current")


class _TimeAbsorbDaily_Type(DisplayString):
    """Custom type timeAbsorbDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TimeAbsorbDaily_Type.__name__ = "DisplayString"
_TimeAbsorbDaily_Object = MibScalar
timeAbsorbDaily = _TimeAbsorbDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 64),
    _TimeAbsorbDaily_Type()
)
timeAbsorbDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeAbsorbDaily.setStatus("current")


class _TimeEqDaily_Type(DisplayString):
    """Custom type timeEqDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TimeEqDaily_Type.__name__ = "DisplayString"
_TimeEqDaily_Object = MibScalar
timeEqDaily = _TimeEqDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 65),
    _TimeEqDaily_Type()
)
timeEqDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeEqDaily.setStatus("current")


class _TimeFloatDaily_Type(DisplayString):
    """Custom type timeFloatDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TimeFloatDaily_Type.__name__ = "DisplayString"
_TimeFloatDaily_Object = MibScalar
timeFloatDaily = _TimeFloatDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 66),
    _TimeFloatDaily_Type()
)
timeFloatDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeFloatDaily.setStatus("current")
_Hourmeter_Type = Unsigned32
_Hourmeter_Object = MibScalar
hourmeter = _Hourmeter_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 67),
    _Hourmeter_Type()
)
hourmeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hourmeter.setStatus("current")


class _SystemChargeKwhDaily_Type(DisplayString):
    """Custom type systemChargeKwhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemChargeKwhDaily_Type.__name__ = "DisplayString"
_SystemChargeKwhDaily_Object = MibScalar
systemChargeKwhDaily = _SystemChargeKwhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 68),
    _SystemChargeKwhDaily_Type()
)
systemChargeKwhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeKwhDaily.setStatus("current")
_SystemChargeKwhResettable10_Type = Unsigned32
_SystemChargeKwhResettable10_Object = MibScalar
systemChargeKwhResettable10 = _SystemChargeKwhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 69),
    _SystemChargeKwhResettable10_Type()
)
systemChargeKwhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeKwhResettable10.setStatus("current")
_SystemChargeKwhTotal10_Type = Unsigned32
_SystemChargeKwhTotal10_Object = MibScalar
systemChargeKwhTotal10 = _SystemChargeKwhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 70),
    _SystemChargeKwhTotal10_Type()
)
systemChargeKwhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeKwhTotal10.setStatus("current")


class _SystemChargeAhDaily_Type(DisplayString):
    """Custom type systemChargeAhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemChargeAhDaily_Type.__name__ = "DisplayString"
_SystemChargeAhDaily_Object = MibScalar
systemChargeAhDaily = _SystemChargeAhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 71),
    _SystemChargeAhDaily_Type()
)
systemChargeAhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeAhDaily.setStatus("current")
_SystemChargeAhResettable10_Type = Unsigned32
_SystemChargeAhResettable10_Object = MibScalar
systemChargeAhResettable10 = _SystemChargeAhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 72),
    _SystemChargeAhResettable10_Type()
)
systemChargeAhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeAhResettable10.setStatus("current")
_SystemChargeAhTotal10_Type = Unsigned32
_SystemChargeAhTotal10_Object = MibScalar
systemChargeAhTotal10 = _SystemChargeAhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 73),
    _SystemChargeAhTotal10_Type()
)
systemChargeAhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemChargeAhTotal10.setStatus("current")


class _SystemBattAhDaily_Type(DisplayString):
    """Custom type systemBattAhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemBattAhDaily_Type.__name__ = "DisplayString"
_SystemBattAhDaily_Object = MibScalar
systemBattAhDaily = _SystemBattAhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 74),
    _SystemBattAhDaily_Type()
)
systemBattAhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBattAhDaily.setStatus("current")
_SystemBattAhResettable10_Type = Integer32
_SystemBattAhResettable10_Object = MibScalar
systemBattAhResettable10 = _SystemBattAhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 75),
    _SystemBattAhResettable10_Type()
)
systemBattAhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBattAhResettable10.setStatus("current")
_SystemBattAhTotal10_Type = Integer32
_SystemBattAhTotal10_Object = MibScalar
systemBattAhTotal10 = _SystemBattAhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 76),
    _SystemBattAhTotal10_Type()
)
systemBattAhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBattAhTotal10.setStatus("current")


class _SystemLoadAhDaily_Type(DisplayString):
    """Custom type systemLoadAhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SystemLoadAhDaily_Type.__name__ = "DisplayString"
_SystemLoadAhDaily_Object = MibScalar
systemLoadAhDaily = _SystemLoadAhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 77),
    _SystemLoadAhDaily_Type()
)
systemLoadAhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoadAhDaily.setStatus("current")
_SystemLoadAhResettable10_Type = Unsigned32
_SystemLoadAhResettable10_Object = MibScalar
systemLoadAhResettable10 = _SystemLoadAhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 78),
    _SystemLoadAhResettable10_Type()
)
systemLoadAhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoadAhResettable10.setStatus("current")
_SystemLoadAhTotal10_Type = Unsigned32
_SystemLoadAhTotal10_Object = MibScalar
systemLoadAhTotal10 = _SystemLoadAhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 79),
    _SystemLoadAhTotal10_Type()
)
systemLoadAhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLoadAhTotal10.setStatus("current")


class _InternalChargeKwhDaily_Type(DisplayString):
    """Custom type internalChargeKwhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InternalChargeKwhDaily_Type.__name__ = "DisplayString"
_InternalChargeKwhDaily_Object = MibScalar
internalChargeKwhDaily = _InternalChargeKwhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 80),
    _InternalChargeKwhDaily_Type()
)
internalChargeKwhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeKwhDaily.setStatus("current")
_InternalChargeKwhResettable10_Type = Unsigned32
_InternalChargeKwhResettable10_Object = MibScalar
internalChargeKwhResettable10 = _InternalChargeKwhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 81),
    _InternalChargeKwhResettable10_Type()
)
internalChargeKwhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeKwhResettable10.setStatus("current")
_InternalChargeKwhTotal10_Type = Unsigned32
_InternalChargeKwhTotal10_Object = MibScalar
internalChargeKwhTotal10 = _InternalChargeKwhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 82),
    _InternalChargeKwhTotal10_Type()
)
internalChargeKwhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeKwhTotal10.setStatus("current")


class _InternalChargeAhDaily_Type(DisplayString):
    """Custom type internalChargeAhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InternalChargeAhDaily_Type.__name__ = "DisplayString"
_InternalChargeAhDaily_Object = MibScalar
internalChargeAhDaily = _InternalChargeAhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 83),
    _InternalChargeAhDaily_Type()
)
internalChargeAhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeAhDaily.setStatus("current")
_InternalChargeAhResettable10_Type = Unsigned32
_InternalChargeAhResettable10_Object = MibScalar
internalChargeAhResettable10 = _InternalChargeAhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 84),
    _InternalChargeAhResettable10_Type()
)
internalChargeAhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeAhResettable10.setStatus("current")
_InternalChargeAhTotal10_Type = Unsigned32
_InternalChargeAhTotal10_Object = MibScalar
internalChargeAhTotal10 = _InternalChargeAhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 85),
    _InternalChargeAhTotal10_Type()
)
internalChargeAhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalChargeAhTotal10.setStatus("current")


class _InternalBattAhDaily_Type(DisplayString):
    """Custom type internalBattAhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InternalBattAhDaily_Type.__name__ = "DisplayString"
_InternalBattAhDaily_Object = MibScalar
internalBattAhDaily = _InternalBattAhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 86),
    _InternalBattAhDaily_Type()
)
internalBattAhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalBattAhDaily.setStatus("current")
_InternalBattAhResettable10_Type = Integer32
_InternalBattAhResettable10_Object = MibScalar
internalBattAhResettable10 = _InternalBattAhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 87),
    _InternalBattAhResettable10_Type()
)
internalBattAhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalBattAhResettable10.setStatus("current")
_InternalBattAhTotal10_Type = Integer32
_InternalBattAhTotal10_Object = MibScalar
internalBattAhTotal10 = _InternalBattAhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 88),
    _InternalBattAhTotal10_Type()
)
internalBattAhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalBattAhTotal10.setStatus("current")


class _Load0AhDaily_Type(DisplayString):
    """Custom type load0AhDaily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Load0AhDaily_Type.__name__ = "DisplayString"
_Load0AhDaily_Object = MibScalar
load0AhDaily = _Load0AhDaily_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 89),
    _Load0AhDaily_Type()
)
load0AhDaily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    load0AhDaily.setStatus("current")
_Load0AhResettable10_Type = Unsigned32
_Load0AhResettable10_Object = MibScalar
load0AhResettable10 = _Load0AhResettable10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 90),
    _Load0AhResettable10_Type()
)
load0AhResettable10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    load0AhResettable10.setStatus("current")
_Load0AhTotal10_Type = Unsigned32
_Load0AhTotal10_Object = MibScalar
load0AhTotal10 = _Load0AhTotal10_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 91),
    _Load0AhTotal10_Type()
)
load0AhTotal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    load0AhTotal10.setStatus("current")


class _AdcIloadF1sDispfil_Type(DisplayString):
    """Custom type adcIloadF1sDispfil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdcIloadF1sDispfil_Type.__name__ = "DisplayString"
_AdcIloadF1sDispfil_Object = MibScalar
adcIloadF1sDispfil = _AdcIloadF1sDispfil_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 92),
    _AdcIloadF1sDispfil_Type()
)
adcIloadF1sDispfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcIloadF1sDispfil.setStatus("current")


class _PowerOutDispfil_Type(DisplayString):
    """Custom type powerOutDispfil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerOutDispfil_Type.__name__ = "DisplayString"
_PowerOutDispfil_Object = MibScalar
powerOutDispfil = _PowerOutDispfil_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 93),
    _PowerOutDispfil_Type()
)
powerOutDispfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOutDispfil.setStatus("current")


class _SystemIbattDispfil_Type(DisplayString):
    """Custom type systemIbattDispfil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SystemIbattDispfil_Type.__name__ = "DisplayString"
_SystemIbattDispfil_Object = MibScalar
systemIbattDispfil = _SystemIbattDispfil_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 94),
    _SystemIbattDispfil_Type()
)
systemIbattDispfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemIbattDispfil.setStatus("current")


class _AdcVarrayFSlowShadowDispfil_Type(DisplayString):
    """Custom type adcVarrayFSlowShadowDispfil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdcVarrayFSlowShadowDispfil_Type.__name__ = "DisplayString"
_AdcVarrayFSlowShadowDispfil_Object = MibScalar
adcVarrayFSlowShadowDispfil = _AdcVarrayFSlowShadowDispfil_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 95),
    _AdcVarrayFSlowShadowDispfil_Type()
)
adcVarrayFSlowShadowDispfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcVarrayFSlowShadowDispfil.setStatus("current")


class _AdcIarrayFSlowShadowDispfil_Type(DisplayString):
    """Custom type adcIarrayFSlowShadowDispfil based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdcIarrayFSlowShadowDispfil_Type.__name__ = "DisplayString"
_AdcIarrayFSlowShadowDispfil_Object = MibScalar
adcIarrayFSlowShadowDispfil = _AdcIarrayFSlowShadowDispfil_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 96),
    _AdcIarrayFSlowShadowDispfil_Type()
)
adcIarrayFSlowShadowDispfil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adcIarrayFSlowShadowDispfil.setStatus("current")


class _EchargevBattRefLimit_Type(DisplayString):
    """Custom type echargevBattRefLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevBattRefLimit_Type.__name__ = "DisplayString"
_EchargevBattRefLimit_Object = MibScalar
echargevBattRefLimit = _EchargevBattRefLimit_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 97),
    _EchargevBattRefLimit_Type()
)
echargevBattRefLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevBattRefLimit.setStatus("current")


class _EchargevAbsorb_Type(DisplayString):
    """Custom type echargevAbsorb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevAbsorb_Type.__name__ = "DisplayString"
_EchargevAbsorb_Object = MibScalar
echargevAbsorb = _EchargevAbsorb_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 98),
    _EchargevAbsorb_Type()
)
echargevAbsorb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevAbsorb.setStatus("current")


class _EchargeiBattAbsorbTerm_Type(DisplayString):
    """Custom type echargeiBattAbsorbTerm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargeiBattAbsorbTerm_Type.__name__ = "DisplayString"
_EchargeiBattAbsorbTerm_Object = MibScalar
echargeiBattAbsorbTerm = _EchargeiBattAbsorbTerm_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 99),
    _EchargeiBattAbsorbTerm_Type()
)
echargeiBattAbsorbTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargeiBattAbsorbTerm.setStatus("current")
_EchargetIBattAbsorbTerm_Type = Unsigned32
_EchargetIBattAbsorbTerm_Object = MibScalar
echargetIBattAbsorbTerm = _EchargetIBattAbsorbTerm_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 100),
    _EchargetIBattAbsorbTerm_Type()
)
echargetIBattAbsorbTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetIBattAbsorbTerm.setStatus("current")


class _EchargevFloatExit_Type(DisplayString):
    """Custom type echargevFloatExit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevFloatExit_Type.__name__ = "DisplayString"
_EchargevFloatExit_Object = MibScalar
echargevFloatExit = _EchargevFloatExit_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 101),
    _EchargevFloatExit_Type()
)
echargevFloatExit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevFloatExit.setStatus("current")


class _EchargevFloatCancel_Type(DisplayString):
    """Custom type echargevFloatCancel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevFloatCancel_Type.__name__ = "DisplayString"
_EchargevFloatCancel_Object = MibScalar
echargevFloatCancel = _EchargevFloatCancel_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 102),
    _EchargevFloatCancel_Type()
)
echargevFloatCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevFloatCancel.setStatus("current")


class _EchargevAbsorptionExt_Type(DisplayString):
    """Custom type echargevAbsorptionExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevAbsorptionExt_Type.__name__ = "DisplayString"
_EchargevAbsorptionExt_Object = MibScalar
echargevAbsorptionExt = _EchargevAbsorptionExt_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 103),
    _EchargevAbsorptionExt_Type()
)
echargevAbsorptionExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevAbsorptionExt.setStatus("current")
_EchargetAbsorptionExt_Type = Unsigned32
_EchargetAbsorptionExt_Object = MibScalar
echargetAbsorptionExt = _EchargetAbsorptionExt_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 104),
    _EchargetAbsorptionExt_Type()
)
echargetAbsorptionExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetAbsorptionExt.setStatus("current")


class _EchargevEqualize_Type(DisplayString):
    """Custom type echargevEqualize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevEqualize_Type.__name__ = "DisplayString"
_EchargevEqualize_Object = MibScalar
echargevEqualize = _EchargevEqualize_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 105),
    _EchargevEqualize_Type()
)
echargevEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevEqualize.setStatus("current")


class _EchargeiEqualizeLimit_Type(DisplayString):
    """Custom type echargeiEqualizeLimit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargeiEqualizeLimit_Type.__name__ = "DisplayString"
_EchargeiEqualizeLimit_Object = MibScalar
echargeiEqualizeLimit = _EchargeiEqualizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 106),
    _EchargeiEqualizeLimit_Type()
)
echargeiEqualizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargeiEqualizeLimit.setStatus("current")


class _EchargevHVD25_Type(DisplayString):
    """Custom type echargevHVD25 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevHVD25_Type.__name__ = "DisplayString"
_EchargevHVD25_Object = MibScalar
echargevHVD25 = _EchargevHVD25_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 107),
    _EchargevHVD25_Type()
)
echargevHVD25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevHVD25.setStatus("current")


class _EchargevHVR_Type(DisplayString):
    """Custom type echargevHVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EchargevHVR_Type.__name__ = "DisplayString"
_EchargevHVR_Object = MibScalar
echargevHVR = _EchargevHVR_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 108),
    _EchargevHVR_Type()
)
echargevHVR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevHVR.setStatus("current")
_EchargetAbsorption_Type = Unsigned32
_EchargetAbsorption_Object = MibScalar
echargetAbsorption = _EchargetAbsorption_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 109),
    _EchargetAbsorption_Type()
)
echargetAbsorption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetAbsorption.setStatus("current")
_EchargetEqualize_Type = Unsigned32
_EchargetEqualize_Object = MibScalar
echargetEqualize = _EchargetEqualize_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 110),
    _EchargetEqualize_Type()
)
echargetEqualize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetEqualize.setStatus("current")
_EchargetEqualizeCalendar_Type = Unsigned32
_EchargetEqualizeCalendar_Object = MibScalar
echargetEqualizeCalendar = _EchargetEqualizeCalendar_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 111),
    _EchargetEqualizeCalendar_Type()
)
echargetEqualizeCalendar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetEqualizeCalendar.setStatus("current")
_EchargetEqualizeTO_Type = Unsigned32
_EchargetEqualizeTO_Object = MibScalar
echargetEqualizeTO = _EchargetEqualizeTO_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 112),
    _EchargetEqualizeTO_Type()
)
echargetEqualizeTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetEqualizeTO.setStatus("current")


class _EchargevTempComp_Type(DisplayString):
    """Custom type echargevTempComp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargevTempComp_Type.__name__ = "DisplayString"
_EchargevTempComp_Object = MibScalar
echargevTempComp = _EchargevTempComp_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 113),
    _EchargevTempComp_Type()
)
echargevTempComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargevTempComp.setStatus("current")


class _EchargeTBattMinLim_Type(DisplayString):
    """Custom type echargeTBattMinLim based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargeTBattMinLim_Type.__name__ = "DisplayString"
_EchargeTBattMinLim_Object = MibScalar
echargeTBattMinLim = _EchargeTBattMinLim_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 114),
    _EchargeTBattMinLim_Type()
)
echargeTBattMinLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargeTBattMinLim.setStatus("current")


class _EchargeTBattMaxLim_Type(DisplayString):
    """Custom type echargeTBattMaxLim based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargeTBattMaxLim_Type.__name__ = "DisplayString"
_EchargeTBattMaxLim_Object = MibScalar
echargeTBattMaxLim = _EchargeTBattMaxLim_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 115),
    _EchargeTBattMaxLim_Type()
)
echargeTBattMaxLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargeTBattMaxLim.setStatus("current")


class _EchargetemperatureFoldbackCold0_Type(DisplayString):
    """Custom type echargetemperatureFoldbackCold0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargetemperatureFoldbackCold0_Type.__name__ = "DisplayString"
_EchargetemperatureFoldbackCold0_Object = MibScalar
echargetemperatureFoldbackCold0 = _EchargetemperatureFoldbackCold0_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 116),
    _EchargetemperatureFoldbackCold0_Type()
)
echargetemperatureFoldbackCold0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetemperatureFoldbackCold0.setStatus("current")


class _EchargetemperatureFoldbackCold100_Type(DisplayString):
    """Custom type echargetemperatureFoldbackCold100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargetemperatureFoldbackCold100_Type.__name__ = "DisplayString"
_EchargetemperatureFoldbackCold100_Object = MibScalar
echargetemperatureFoldbackCold100 = _EchargetemperatureFoldbackCold100_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 117),
    _EchargetemperatureFoldbackCold100_Type()
)
echargetemperatureFoldbackCold100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetemperatureFoldbackCold100.setStatus("current")


class _EchargetemperatureFoldbackHot100_Type(DisplayString):
    """Custom type echargetemperatureFoldbackHot100 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargetemperatureFoldbackHot100_Type.__name__ = "DisplayString"
_EchargetemperatureFoldbackHot100_Object = MibScalar
echargetemperatureFoldbackHot100 = _EchargetemperatureFoldbackHot100_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 118),
    _EchargetemperatureFoldbackHot100_Type()
)
echargetemperatureFoldbackHot100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetemperatureFoldbackHot100.setStatus("current")


class _EchargetemperatureFoldbackHot0_Type(DisplayString):
    """Custom type echargetemperatureFoldbackHot0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EchargetemperatureFoldbackHot0_Type.__name__ = "DisplayString"
_EchargetemperatureFoldbackHot0_Object = MibScalar
echargetemperatureFoldbackHot0 = _EchargetemperatureFoldbackHot0_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 119),
    _EchargetemperatureFoldbackHot0_Type()
)
echargetemperatureFoldbackHot0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echargetemperatureFoldbackHot0.setStatus("current")
_EgreenMode_Type = TruthValue
_EgreenMode_Object = MibScalar
egreenMode = _EgreenMode_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 120),
    _EgreenMode_Type()
)
egreenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egreenMode.setStatus("current")
_EBatteryType_Type = Unsigned32
_EBatteryType_Object = MibScalar
eBatteryType = _EBatteryType_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 121),
    _EBatteryType_Type()
)
eBatteryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eBatteryType.setStatus("current")
_EmodbusId_Type = Unsigned32
_EmodbusId_Object = MibScalar
emodbusId = _EmodbusId_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 122),
    _EmodbusId_Type()
)
emodbusId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emodbusId.setStatus("current")
_EbaudrateMb232_Type = Unsigned32
_EbaudrateMb232_Object = MibScalar
ebaudrateMb232 = _EbaudrateMb232_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 123),
    _EbaudrateMb232_Type()
)
ebaudrateMb232.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ebaudrateMb232.setStatus("current")


class _Eload0VLVD0_Type(DisplayString):
    """Custom type eload0VLVD0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0VLVD0_Type.__name__ = "DisplayString"
_Eload0VLVD0_Object = MibScalar
eload0VLVD0 = _Eload0VLVD0_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 124),
    _Eload0VLVD0_Type()
)
eload0VLVD0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0VLVD0.setStatus("current")


class _Eload0VLVR_Type(DisplayString):
    """Custom type eload0VLVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0VLVR_Type.__name__ = "DisplayString"
_Eload0VLVR_Object = MibScalar
eload0VLVR = _Eload0VLVR_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 125),
    _Eload0VLVR_Type()
)
eload0VLVR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0VLVR.setStatus("current")


class _Eload0vStartLVD_Type(DisplayString):
    """Custom type eload0vStartLVD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0vStartLVD_Type.__name__ = "DisplayString"
_Eload0vStartLVD_Object = MibScalar
eload0vStartLVD = _Eload0vStartLVD_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 126),
    _Eload0vStartLVD_Type()
)
eload0vStartLVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0vStartLVD.setStatus("current")


class _Eload0HVD_Type(DisplayString):
    """Custom type eload0HVD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0HVD_Type.__name__ = "DisplayString"
_Eload0HVD_Object = MibScalar
eload0HVD = _Eload0HVD_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 127),
    _Eload0HVD_Type()
)
eload0HVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0HVD.setStatus("current")


class _Eload0HVR_Type(DisplayString):
    """Custom type eload0HVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0HVR_Type.__name__ = "DisplayString"
_Eload0HVR_Object = MibScalar
eload0HVR = _Eload0HVR_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 128),
    _Eload0HVR_Type()
)
eload0HVR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0HVR.setStatus("current")


class _Eload0SOCDisconnect_Type(DisplayString):
    """Custom type eload0SOCDisconnect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0SOCDisconnect_Type.__name__ = "DisplayString"
_Eload0SOCDisconnect_Object = MibScalar
eload0SOCDisconnect = _Eload0SOCDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 129),
    _Eload0SOCDisconnect_Type()
)
eload0SOCDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0SOCDisconnect.setStatus("current")


class _Eload0SOCReconnect_Type(DisplayString):
    """Custom type eload0SOCReconnect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0SOCReconnect_Type.__name__ = "DisplayString"
_Eload0SOCReconnect_Object = MibScalar
eload0SOCReconnect = _Eload0SOCReconnect_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 130),
    _Eload0SOCReconnect_Type()
)
eload0SOCReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0SOCReconnect.setStatus("current")
_Eload0tLVDWarn_Type = Unsigned32
_Eload0tLVDWarn_Object = MibScalar
eload0tLVDWarn = _Eload0tLVDWarn_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 131),
    _Eload0tLVDWarn_Type()
)
eload0tLVDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0tLVDWarn.setStatus("current")


class _Eload0currentComp_Type(DisplayString):
    """Custom type eload0currentComp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Eload0currentComp_Type.__name__ = "DisplayString"
_Eload0currentComp_Object = MibScalar
eload0currentComp = _Eload0currentComp_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 132),
    _Eload0currentComp_Type()
)
eload0currentComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eload0currentComp.setStatus("current")
_EIPAddr_Type = IpAddress
_EIPAddr_Object = MibScalar
eIPAddr = _EIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 133),
    _EIPAddr_Type()
)
eIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eIPAddr.setStatus("current")
_ENetMask_Type = IpAddress
_ENetMask_Object = MibScalar
eNetMask = _ENetMask_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 134),
    _ENetMask_Type()
)
eNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eNetMask.setStatus("current")
_EGateway_Type = IpAddress
_EGateway_Object = MibScalar
eGateway = _EGateway_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 135),
    _EGateway_Type()
)
eGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eGateway.setStatus("current")
_EPrimaryDNSServer_Type = IpAddress
_EPrimaryDNSServer_Object = MibScalar
ePrimaryDNSServer = _EPrimaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 136),
    _EPrimaryDNSServer_Type()
)
ePrimaryDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePrimaryDNSServer.setStatus("current")
_ESecondaryDNSServer_Type = IpAddress
_ESecondaryDNSServer_Object = MibScalar
eSecondaryDNSServer = _ESecondaryDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 137),
    _ESecondaryDNSServer_Type()
)
eSecondaryDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSecondaryDNSServer.setStatus("current")
_EIsDHCPEnabled_Type = TruthValue
_EIsDHCPEnabled_Object = MibScalar
eIsDHCPEnabled = _EIsDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 138),
    _EIsDHCPEnabled_Type()
)
eIsDHCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eIsDHCPEnabled.setStatus("current")
_EHTTPPort_Type = Unsigned32
_EHTTPPort_Object = MibScalar
eHTTPPort = _EHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 139),
    _EHTTPPort_Type()
)
eHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eHTTPPort.setStatus("current")
_EMBIPPort_Type = Unsigned32
_EMBIPPort_Object = MibScalar
eMBIPPort = _EMBIPPort_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 140),
    _EMBIPPort_Type()
)
eMBIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eMBIPPort.setStatus("current")
_EModbusTcpBridgingEnabled_Type = TruthValue
_EModbusTcpBridgingEnabled_Object = MibScalar
eModbusTcpBridgingEnabled = _EModbusTcpBridgingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 141),
    _EModbusTcpBridgingEnabled_Type()
)
eModbusTcpBridgingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eModbusTcpBridgingEnabled.setStatus("current")
_EWirelessEnable_Type = TruthValue
_EWirelessEnable_Object = MibScalar
eWirelessEnable = _EWirelessEnable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 142),
    _EWirelessEnable_Type()
)
eWirelessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eWirelessEnable.setStatus("current")
_Eqtrig_Type = TruthValue
_Eqtrig_Object = MibScalar
eqtrig = _Eqtrig_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 500),
    _Eqtrig_Type()
)
eqtrig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqtrig.setStatus("current")
_Loaddisconnect_Type = TruthValue
_Loaddisconnect_Object = MibScalar
loaddisconnect = _Loaddisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 501),
    _Loaddisconnect_Type()
)
loaddisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loaddisconnect.setStatus("current")
_Chargedisconnect_Type = TruthValue
_Chargedisconnect_Object = MibScalar
chargedisconnect = _Chargedisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 502),
    _Chargedisconnect_Type()
)
chargedisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chargedisconnect.setStatus("current")
_ClearCountersResettable_Type = TruthValue
_ClearCountersResettable_Object = MibScalar
clearCountersResettable = _ClearCountersResettable_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 503),
    _ClearCountersResettable_Type()
)
clearCountersResettable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersResettable.setStatus("current")
_ClearCountersTotal_Type = TruthValue
_ClearCountersTotal_Object = MibScalar
clearCountersTotal = _ClearCountersTotal_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 504),
    _ClearCountersTotal_Type()
)
clearCountersTotal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearCountersTotal.setStatus("current")
_ClearVbminmax_Type = TruthValue
_ClearVbminmax_Object = MibScalar
clearVbminmax = _ClearVbminmax_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 505),
    _ClearVbminmax_Type()
)
clearVbminmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearVbminmax.setStatus("current")
_ClearFaults_Type = TruthValue
_ClearFaults_Object = MibScalar
clearFaults = _ClearFaults_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 506),
    _ClearFaults_Type()
)
clearFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearFaults.setStatus("current")
_ClearAlarms_Type = TruthValue
_ClearAlarms_Object = MibScalar
clearAlarms = _ClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 507),
    _ClearAlarms_Type()
)
clearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearAlarms.setStatus("current")
_EeUpdate_Type = TruthValue
_EeUpdate_Object = MibScalar
eeUpdate = _EeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 508),
    _EeUpdate_Type()
)
eeUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eeUpdate.setStatus("current")
_LvdOverride_Type = TruthValue
_LvdOverride_Object = MibScalar
lvdOverride = _LvdOverride_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 509),
    _LvdOverride_Type()
)
lvdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lvdOverride.setStatus("current")
_EepromSessionApply_Type = TruthValue
_EepromSessionApply_Object = MibScalar
eepromSessionApply = _EepromSessionApply_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 510),
    _EepromSessionApply_Type()
)
eepromSessionApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eepromSessionApply.setStatus("current")
_Reset_Type = TruthValue
_Reset_Object = MibScalar
reset = _Reset_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 511),
    _Reset_Type()
)
reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset.setStatus("current")
_SetOrClearSoc_Type = TruthValue
_SetOrClearSoc_Object = MibScalar
setOrClearSoc = _SetOrClearSoc_Object(
    (1, 3, 6, 1, 4, 1, 33333, 10, 512),
    _SetOrClearSoc_Type()
)
setOrClearSoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setOrClearSoc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENSTAR",
    **{"ChargeStateEnum": ChargeStateEnum,
       "LoadStateEnum": LoadStateEnum,
       "LoadFaultBitfield": LoadFaultBitfield,
       "FaultBitfield": FaultBitfield,
       "AlarmBitfield": AlarmBitfield,
       "ChargeFaultBitfield": ChargeFaultBitfield,
       "FaultPowersupplyBitfield": FaultPowersupplyBitfield,
       "BlockFaultBitfield": BlockFaultBitfield,
       "FaultPowerstageBitfield": FaultPowerstageBitfield,
       "genStar": genStar,
       "subModel": subModel,
       "serialNumber": serialNumber,
       "deviceVersion": deviceVersion,
       "vbterm": vbterm,
       "vload": vload,
       "vbsense": vbsense,
       "vCoin": vCoin,
       "systemIcharge": systemIcharge,
       "systemIload": systemIload,
       "tempBatt": tempBatt,
       "tempRts": tempRts,
       "tempHeatsink": tempHeatsink,
       "chargeState": chargeState,
       "vbattRefCharge": vbattRefCharge,
       "battSoc": battSoc,
       "vbattMin": vbattMin,
       "vbattMax": vbattMax,
       "battSocMinDaily": battSocMinDaily,
       "battSocMaxDaily": battSocMaxDaily,
       "loadState": loadState,
       "loadFault": loadFault,
       "loadFaultDaily": loadFaultDaily,
       "fault": fault,
       "faultDaily": faultDaily,
       "alarm": alarm,
       "alarmDaily": alarmDaily,
       "chargeFault": chargeFault,
       "chargeFaultDaily": chargeFaultDaily,
       "faultPowersupply": faultPowersupply,
       "faultPowersupplyDaily": faultPowersupplyDaily,
       "blockFault": blockFault,
       "blockFaultDaily": blockFaultDaily,
       "faultPowerstage": faultPowerstage,
       "faultPowerstageDaily": faultPowerstageDaily,
       "vbattMinDaily": vbattMinDaily,
       "vbattMaxDaily": vbattMaxDaily,
       "varrayMaxDaily": varrayMaxDaily,
       "timeAbsorbDaily": timeAbsorbDaily,
       "timeEqDaily": timeEqDaily,
       "timeFloatDaily": timeFloatDaily,
       "hourmeter": hourmeter,
       "systemChargeKwhDaily": systemChargeKwhDaily,
       "systemChargeKwhResettable10": systemChargeKwhResettable10,
       "systemChargeKwhTotal10": systemChargeKwhTotal10,
       "systemChargeAhDaily": systemChargeAhDaily,
       "systemChargeAhResettable10": systemChargeAhResettable10,
       "systemChargeAhTotal10": systemChargeAhTotal10,
       "systemBattAhDaily": systemBattAhDaily,
       "systemBattAhResettable10": systemBattAhResettable10,
       "systemBattAhTotal10": systemBattAhTotal10,
       "systemLoadAhDaily": systemLoadAhDaily,
       "systemLoadAhResettable10": systemLoadAhResettable10,
       "systemLoadAhTotal10": systemLoadAhTotal10,
       "internalChargeKwhDaily": internalChargeKwhDaily,
       "internalChargeKwhResettable10": internalChargeKwhResettable10,
       "internalChargeKwhTotal10": internalChargeKwhTotal10,
       "internalChargeAhDaily": internalChargeAhDaily,
       "internalChargeAhResettable10": internalChargeAhResettable10,
       "internalChargeAhTotal10": internalChargeAhTotal10,
       "internalBattAhDaily": internalBattAhDaily,
       "internalBattAhResettable10": internalBattAhResettable10,
       "internalBattAhTotal10": internalBattAhTotal10,
       "load0AhDaily": load0AhDaily,
       "load0AhResettable10": load0AhResettable10,
       "load0AhTotal10": load0AhTotal10,
       "adcIloadF1sDispfil": adcIloadF1sDispfil,
       "powerOutDispfil": powerOutDispfil,
       "systemIbattDispfil": systemIbattDispfil,
       "adcVarrayFSlowShadowDispfil": adcVarrayFSlowShadowDispfil,
       "adcIarrayFSlowShadowDispfil": adcIarrayFSlowShadowDispfil,
       "echargevBattRefLimit": echargevBattRefLimit,
       "echargevAbsorb": echargevAbsorb,
       "echargeiBattAbsorbTerm": echargeiBattAbsorbTerm,
       "echargetIBattAbsorbTerm": echargetIBattAbsorbTerm,
       "echargevFloatExit": echargevFloatExit,
       "echargevFloatCancel": echargevFloatCancel,
       "echargevAbsorptionExt": echargevAbsorptionExt,
       "echargetAbsorptionExt": echargetAbsorptionExt,
       "echargevEqualize": echargevEqualize,
       "echargeiEqualizeLimit": echargeiEqualizeLimit,
       "echargevHVD25": echargevHVD25,
       "echargevHVR": echargevHVR,
       "echargetAbsorption": echargetAbsorption,
       "echargetEqualize": echargetEqualize,
       "echargetEqualizeCalendar": echargetEqualizeCalendar,
       "echargetEqualizeTO": echargetEqualizeTO,
       "echargevTempComp": echargevTempComp,
       "echargeTBattMinLim": echargeTBattMinLim,
       "echargeTBattMaxLim": echargeTBattMaxLim,
       "echargetemperatureFoldbackCold0": echargetemperatureFoldbackCold0,
       "echargetemperatureFoldbackCold100": echargetemperatureFoldbackCold100,
       "echargetemperatureFoldbackHot100": echargetemperatureFoldbackHot100,
       "echargetemperatureFoldbackHot0": echargetemperatureFoldbackHot0,
       "egreenMode": egreenMode,
       "eBatteryType": eBatteryType,
       "emodbusId": emodbusId,
       "ebaudrateMb232": ebaudrateMb232,
       "eload0VLVD0": eload0VLVD0,
       "eload0VLVR": eload0VLVR,
       "eload0vStartLVD": eload0vStartLVD,
       "eload0HVD": eload0HVD,
       "eload0HVR": eload0HVR,
       "eload0SOCDisconnect": eload0SOCDisconnect,
       "eload0SOCReconnect": eload0SOCReconnect,
       "eload0tLVDWarn": eload0tLVDWarn,
       "eload0currentComp": eload0currentComp,
       "eIPAddr": eIPAddr,
       "eNetMask": eNetMask,
       "eGateway": eGateway,
       "ePrimaryDNSServer": ePrimaryDNSServer,
       "eSecondaryDNSServer": eSecondaryDNSServer,
       "eIsDHCPEnabled": eIsDHCPEnabled,
       "eHTTPPort": eHTTPPort,
       "eMBIPPort": eMBIPPort,
       "eModbusTcpBridgingEnabled": eModbusTcpBridgingEnabled,
       "eWirelessEnable": eWirelessEnable,
       "eqtrig": eqtrig,
       "loaddisconnect": loaddisconnect,
       "chargedisconnect": chargedisconnect,
       "clearCountersResettable": clearCountersResettable,
       "clearCountersTotal": clearCountersTotal,
       "clearVbminmax": clearVbminmax,
       "clearFaults": clearFaults,
       "clearAlarms": clearAlarms,
       "eeUpdate": eeUpdate,
       "lvdOverride": lvdOverride,
       "eepromSessionApply": eepromSessionApply,
       "reset": reset,
       "setOrClearSoc": setOrClearSoc}
)
