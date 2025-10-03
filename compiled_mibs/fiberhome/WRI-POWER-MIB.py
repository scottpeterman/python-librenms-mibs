# SNMP MIB module (WRI-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-POWER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:14 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(wri,
 wriProducts) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wri",
    "wriProducts")


# MODULE-IDENTITY

msppPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2)
)
if mibBuilder.loadTexts:
    msppPower.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("current")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1)
)
powerEntry.setIndexNames(
    (0, "WRI-POWER-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("current")
_PowerIndex_Type = Unsigned32
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _PowerType_Type(Integer32):
    """Custom type powerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dcdc", 0),
          ("acdc", 1))
    )


_PowerType_Type.__name__ = "Integer32"
_PowerType_Object = MibTableColumn
powerType = _PowerType_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 2),
    _PowerType_Type()
)
powerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerType.setStatus("current")


class _PowerState_Type(Integer32):
    """Custom type powerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("voltagelack", 1),
          ("voltageoverload", 2))
    )


_PowerState_Type.__name__ = "Integer32"
_PowerState_Object = MibTableColumn
powerState = _PowerState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 3),
    _PowerState_Type()
)
powerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerState.setStatus("current")
_PowerValue_Type = Integer32
_PowerValue_Object = MibTableColumn
powerValue = _PowerValue_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 4),
    _PowerValue_Type()
)
powerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerValue.setStatus("current")
_PowerRole_Type = Integer32
_PowerRole_Object = MibTableColumn
powerRole = _PowerRole_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 5),
    _PowerRole_Type()
)
powerRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerRole.setStatus("current")
_PowerDescr_Type = OctetString
_PowerDescr_Object = MibTableColumn
powerDescr = _PowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 6),
    _PowerDescr_Type()
)
powerDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerDescr.setStatus("current")
_PowerSerial_Type = OctetString
_PowerSerial_Object = MibTableColumn
powerSerial = _PowerSerial_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 7),
    _PowerSerial_Type()
)
powerSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSerial.setStatus("current")
_PowerTemperature_Type = Integer32
_PowerTemperature_Object = MibTableColumn
powerTemperature = _PowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 8),
    _PowerTemperature_Type()
)
powerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerTemperature.setStatus("current")
_PowerFuseStatus_Type = Integer32
_PowerFuseStatus_Object = MibTableColumn
powerFuseStatus = _PowerFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 9),
    _PowerFuseStatus_Type()
)
powerFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerFuseStatus.setStatus("current")


class _PowerStateBits_Type(Integer32):
    """Custom type powerStateBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("voltagelack", 1),
          ("voltageoverload", 2))
    )


_PowerStateBits_Type.__name__ = "Integer32"
_PowerStateBits_Object = MibTableColumn
powerStateBits = _PowerStateBits_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 10),
    _PowerStateBits_Type()
)
powerStateBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStateBits.setStatus("current")


class _PowerTrapEna_Type(Integer32):
    """Custom type powerTrapEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PowerTrapEna_Type.__name__ = "Integer32"
_PowerTrapEna_Object = MibTableColumn
powerTrapEna = _PowerTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 11),
    _PowerTrapEna_Type()
)
powerTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerTrapEna.setStatus("current")
_PowerAllSetting_Type = OctetString
_PowerAllSetting_Object = MibTableColumn
powerAllSetting = _PowerAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 12),
    _PowerAllSetting_Type()
)
powerAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerAllSetting.setStatus("current")
_PowerIndexDescr_Type = OctetString
_PowerIndexDescr_Object = MibTableColumn
powerIndexDescr = _PowerIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 1, 1, 13),
    _PowerIndexDescr_Type()
)
powerIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndexDescr.setStatus("current")
_PowerTrap_ObjectIdentity = ObjectIdentity
powerTrap = _PowerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 2)
)
_PowerGeneral_ObjectIdentity = ObjectIdentity
powerGeneral = _PowerGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 3)
)
_PowerBits_Type = Counter32
_PowerBits_Object = MibScalar
powerBits = _PowerBits_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 3, 1),
    _PowerBits_Type()
)
powerBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerBits.setStatus("current")
_PowerNum_Type = Integer32
_PowerNum_Object = MibScalar
powerNum = _PowerNum_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 3, 2),
    _PowerNum_Type()
)
powerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerNum.setStatus("current")


class _PowerTrapEnable_Type(Integer32):
    """Custom type powerTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PowerTrapEnable_Type.__name__ = "Integer32"
_PowerTrapEnable_Object = MibScalar
powerTrapEnable = _PowerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 3, 3),
    _PowerTrapEnable_Type()
)
powerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerTrapEnable.setStatus("current")


class _PowerMonitorEnable_Type(Integer32):
    """Custom type powerMonitorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PowerMonitorEnable_Type.__name__ = "Integer32"
_PowerMonitorEnable_Object = MibScalar
powerMonitorEnable = _PowerMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 3, 4),
    _PowerMonitorEnable_Type()
)
powerMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMonitorEnable.setStatus("current")

# Managed Objects groups


# Notification objects

powerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 2, 1)
)
powerUp.setObjects(
    ("WRI-POWER-MIB", "powerState")
)
if mibBuilder.loadTexts:
    powerUp.setStatus(
        "current"
    )

powerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 2, 2)
)
powerDown.setObjects(
    ("WRI-POWER-MIB", "powerState")
)
if mibBuilder.loadTexts:
    powerDown.setStatus(
        "current"
    )

powerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 2, 3)
)
powerFault.setObjects(
    ("WRI-POWER-MIB", "powerState")
)
if mibBuilder.loadTexts:
    powerFault.setStatus(
        "current"
    )

powerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 2, 2, 4)
)
powerOk.setObjects(
    ("WRI-POWER-MIB", "powerState")
)
if mibBuilder.loadTexts:
    powerOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-POWER-MIB",
    **{"mspp": mspp,
       "msppChassis": msppChassis,
       "msppPower": msppPower,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerType": powerType,
       "powerState": powerState,
       "powerValue": powerValue,
       "powerRole": powerRole,
       "powerDescr": powerDescr,
       "powerSerial": powerSerial,
       "powerTemperature": powerTemperature,
       "powerFuseStatus": powerFuseStatus,
       "powerStateBits": powerStateBits,
       "powerTrapEna": powerTrapEna,
       "powerAllSetting": powerAllSetting,
       "powerIndexDescr": powerIndexDescr,
       "powerTrap": powerTrap,
       "powerUp": powerUp,
       "powerDown": powerDown,
       "powerFault": powerFault,
       "powerOk": powerOk,
       "powerGeneral": powerGeneral,
       "powerBits": powerBits,
       "powerNum": powerNum,
       "powerTrapEnable": powerTrapEnable,
       "powerMonitorEnable": powerMonitorEnable}
)
