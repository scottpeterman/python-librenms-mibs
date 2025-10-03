# SNMP MIB module (ALPINE-GEN-CARD-EDFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpineoe\ALPINE-GEN-CARD-EDFA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:45 2025
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

(alpineGeneric,) = mibBuilder.importSymbols(
    "ALPINE-ROOT",
    "alpineGeneric")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlpineGenCardEdfa_ObjectIdentity = ObjectIdentity
alpineGenCardEdfa = _AlpineGenCardEdfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1)
)
_AlpineGenCardEdfaInfosTable_Object = MibTable
alpineGenCardEdfaInfosTable = _AlpineGenCardEdfaInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alpineGenCardEdfaInfosTable.setStatus("current")
_AlpineGenCardEdfaInfosEntry_Object = MibTableRow
alpineGenCardEdfaInfosEntry = _AlpineGenCardEdfaInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1)
)
alpineGenCardEdfaInfosEntry.setIndexNames(
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "gceSlotNum"),
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "gceEdfaNum"),
)
if mibBuilder.loadTexts:
    alpineGenCardEdfaInfosEntry.setStatus("current")


class _GceSlotNum_Type(Integer32):
    """Custom type gceSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GceSlotNum_Type.__name__ = "Integer32"
_GceSlotNum_Object = MibTableColumn
gceSlotNum = _GceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 1),
    _GceSlotNum_Type()
)
gceSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceSlotNum.setStatus("current")


class _GceEdfaNum_Type(Integer32):
    """Custom type gceEdfaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GceEdfaNum_Type.__name__ = "Integer32"
_GceEdfaNum_Object = MibTableColumn
gceEdfaNum = _GceEdfaNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 2),
    _GceEdfaNum_Type()
)
gceEdfaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceEdfaNum.setStatus("current")


class _GceMode_Type(Integer32):
    """Custom type gceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GceMode_Type.__name__ = "Integer32"
_GceMode_Object = MibTableColumn
gceMode = _GceMode_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 3),
    _GceMode_Type()
)
gceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceMode.setStatus("current")


class _GceOutputPowerTarget_Type(OctetString):
    """Custom type gceOutputPowerTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceOutputPowerTarget_Type.__name__ = "OctetString"
_GceOutputPowerTarget_Object = MibTableColumn
gceOutputPowerTarget = _GceOutputPowerTarget_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 4),
    _GceOutputPowerTarget_Type()
)
gceOutputPowerTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceOutputPowerTarget.setStatus("current")
if mibBuilder.loadTexts:
    gceOutputPowerTarget.setUnits("dBm")


class _GceGainTarget_Type(OctetString):
    """Custom type gceGainTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceGainTarget_Type.__name__ = "OctetString"
_GceGainTarget_Object = MibTableColumn
gceGainTarget = _GceGainTarget_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 5),
    _GceGainTarget_Type()
)
gceGainTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceGainTarget.setStatus("current")
if mibBuilder.loadTexts:
    gceGainTarget.setUnits("dB")


class _GceOutputPower_Type(OctetString):
    """Custom type gceOutputPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceOutputPower_Type.__name__ = "OctetString"
_GceOutputPower_Object = MibTableColumn
gceOutputPower = _GceOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 6),
    _GceOutputPower_Type()
)
gceOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    gceOutputPower.setUnits("dBm")


class _GceGain_Type(OctetString):
    """Custom type gceGain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceGain_Type.__name__ = "OctetString"
_GceGain_Object = MibTableColumn
gceGain = _GceGain_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 7),
    _GceGain_Type()
)
gceGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceGain.setStatus("current")
if mibBuilder.loadTexts:
    gceGain.setUnits("dB")


class _GceTemperature_Type(OctetString):
    """Custom type gceTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceTemperature_Type.__name__ = "OctetString"
_GceTemperature_Object = MibTableColumn
gceTemperature = _GceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 8),
    _GceTemperature_Type()
)
gceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceTemperature.setStatus("current")


class _GceSaveConfig_Type(Integer32):
    """Custom type gceSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GceSaveConfig_Type.__name__ = "Integer32"
_GceSaveConfig_Object = MibTableColumn
gceSaveConfig = _GceSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 9),
    _GceSaveConfig_Type()
)
gceSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceSaveConfig.setStatus("current")


class _GceInputPower_Type(OctetString):
    """Custom type gceInputPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceInputPower_Type.__name__ = "OctetString"
_GceInputPower_Object = MibTableColumn
gceInputPower = _GceInputPower_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 1, 1, 10),
    _GceInputPower_Type()
)
gceInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceInputPower.setStatus("current")
if mibBuilder.loadTexts:
    gceInputPower.setUnits("dBm")
_AlpineGenCardEdfaAlarm_ObjectIdentity = ObjectIdentity
alpineGenCardEdfaAlarm = _AlpineGenCardEdfaAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2)
)
_AlpineGenCardEdfaAlarmThldTable_Object = MibTable
alpineGenCardEdfaAlarmThldTable = _AlpineGenCardEdfaAlarmThldTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alpineGenCardEdfaAlarmThldTable.setStatus("current")
_AlpineGenCardEdfaAlarmThldEntry_Object = MibTableRow
alpineGenCardEdfaAlarmThldEntry = _AlpineGenCardEdfaAlarmThldEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1)
)
alpineGenCardEdfaAlarmThldEntry.setIndexNames(
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "gceaSlotNum"),
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "gceaEdfaNum"),
)
if mibBuilder.loadTexts:
    alpineGenCardEdfaAlarmThldEntry.setStatus("current")


class _GceaSlotNum_Type(Integer32):
    """Custom type gceaSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GceaSlotNum_Type.__name__ = "Integer32"
_GceaSlotNum_Object = MibTableColumn
gceaSlotNum = _GceaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1, 1),
    _GceaSlotNum_Type()
)
gceaSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceaSlotNum.setStatus("current")


class _GceaEdfaNum_Type(Integer32):
    """Custom type gceaEdfaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GceaEdfaNum_Type.__name__ = "Integer32"
_GceaEdfaNum_Object = MibTableColumn
gceaEdfaNum = _GceaEdfaNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1, 2),
    _GceaEdfaNum_Type()
)
gceaEdfaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gceaEdfaNum.setStatus("current")


class _GceaInputPowerThld_Type(OctetString):
    """Custom type gceaInputPowerThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceaInputPowerThld_Type.__name__ = "OctetString"
_GceaInputPowerThld_Object = MibTableColumn
gceaInputPowerThld = _GceaInputPowerThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1, 3),
    _GceaInputPowerThld_Type()
)
gceaInputPowerThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceaInputPowerThld.setStatus("current")
if mibBuilder.loadTexts:
    gceaInputPowerThld.setUnits("dBm")


class _GceaOutputPowerThld_Type(OctetString):
    """Custom type gceaOutputPowerThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceaOutputPowerThld_Type.__name__ = "OctetString"
_GceaOutputPowerThld_Object = MibTableColumn
gceaOutputPowerThld = _GceaOutputPowerThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1, 4),
    _GceaOutputPowerThld_Type()
)
gceaOutputPowerThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceaOutputPowerThld.setStatus("current")
if mibBuilder.loadTexts:
    gceaOutputPowerThld.setUnits("dBm")


class _GceaTemperatureThld_Type(OctetString):
    """Custom type gceaTemperatureThld based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_GceaTemperatureThld_Type.__name__ = "OctetString"
_GceaTemperatureThld_Object = MibTableColumn
gceaTemperatureThld = _GceaTemperatureThld_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 1, 1, 5),
    _GceaTemperatureThld_Type()
)
gceaTemperatureThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gceaTemperatureThld.setStatus("current")
if mibBuilder.loadTexts:
    gceaTemperatureThld.setUnits("degreeC")
_AlpineGenEdfaAlarmInfoTable_Object = MibTable
alpineGenEdfaAlarmInfoTable = _AlpineGenEdfaAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alpineGenEdfaAlarmInfoTable.setStatus("current")
_AlpineGenEdfaAlarmInfoEntry_Object = MibTableRow
alpineGenEdfaAlarmInfoEntry = _AlpineGenEdfaAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1)
)
alpineGenEdfaAlarmInfoEntry.setIndexNames(
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "geaiSlotNum"),
    (0, "ALPINE-GEN-CARD-EDFA-MIB", "geaiEdfaNum"),
)
if mibBuilder.loadTexts:
    alpineGenEdfaAlarmInfoEntry.setStatus("current")


class _GeaiSlotNum_Type(Integer32):
    """Custom type geaiSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GeaiSlotNum_Type.__name__ = "Integer32"
_GeaiSlotNum_Object = MibTableColumn
geaiSlotNum = _GeaiSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 1),
    _GeaiSlotNum_Type()
)
geaiSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiSlotNum.setStatus("current")


class _GeaiEdfaNum_Type(Integer32):
    """Custom type geaiEdfaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GeaiEdfaNum_Type.__name__ = "Integer32"
_GeaiEdfaNum_Object = MibTableColumn
geaiEdfaNum = _GeaiEdfaNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 2),
    _GeaiEdfaNum_Type()
)
geaiEdfaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiEdfaNum.setStatus("current")


class _GeaiCommonAlarm_Type(Integer32):
    """Custom type geaiCommonAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiCommonAlarm_Type.__name__ = "Integer32"
_GeaiCommonAlarm_Object = MibTableColumn
geaiCommonAlarm = _GeaiCommonAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 3),
    _GeaiCommonAlarm_Type()
)
geaiCommonAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiCommonAlarm.setStatus("current")


class _GeaiCaseTemperatureAlarm_Type(Integer32):
    """Custom type geaiCaseTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiCaseTemperatureAlarm_Type.__name__ = "Integer32"
_GeaiCaseTemperatureAlarm_Object = MibTableColumn
geaiCaseTemperatureAlarm = _GeaiCaseTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 4),
    _GeaiCaseTemperatureAlarm_Type()
)
geaiCaseTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiCaseTemperatureAlarm.setStatus("current")


class _GeaiPumpTemperatureAlarm_Type(Integer32):
    """Custom type geaiPumpTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiPumpTemperatureAlarm_Type.__name__ = "Integer32"
_GeaiPumpTemperatureAlarm_Object = MibTableColumn
geaiPumpTemperatureAlarm = _GeaiPumpTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 5),
    _GeaiPumpTemperatureAlarm_Type()
)
geaiPumpTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiPumpTemperatureAlarm.setStatus("current")


class _GeaiPumpBiasAlarm_Type(Integer32):
    """Custom type geaiPumpBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiPumpBiasAlarm_Type.__name__ = "Integer32"
_GeaiPumpBiasAlarm_Object = MibTableColumn
geaiPumpBiasAlarm = _GeaiPumpBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 6),
    _GeaiPumpBiasAlarm_Type()
)
geaiPumpBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiPumpBiasAlarm.setStatus("current")


class _GeaiLossInputAlarm_Type(Integer32):
    """Custom type geaiLossInputAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiLossInputAlarm_Type.__name__ = "Integer32"
_GeaiLossInputAlarm_Object = MibTableColumn
geaiLossInputAlarm = _GeaiLossInputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 7),
    _GeaiLossInputAlarm_Type()
)
geaiLossInputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiLossInputAlarm.setStatus("current")


class _GeaiLossOutputAlarm_Type(Integer32):
    """Custom type geaiLossOutputAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GeaiLossOutputAlarm_Type.__name__ = "Integer32"
_GeaiLossOutputAlarm_Object = MibTableColumn
geaiLossOutputAlarm = _GeaiLossOutputAlarm_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 2, 1, 8),
    _GeaiLossOutputAlarm_Type()
)
geaiLossOutputAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geaiLossOutputAlarm.setStatus("current")

# Managed Objects groups


# Notification objects

alpineGenEdfaPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 3)
)
alpineGenEdfaPowerAlarm.setObjects(
      *(("ALPINE-GEN-CARD-EDFA-MIB", "gceOutputPower"),
        ("ALPINE-GEN-CARD-EDFA-MIB", "geaiLossOutputAlarm"))
)
if mibBuilder.loadTexts:
    alpineGenEdfaPowerAlarm.setStatus(
        "current"
    )

alpineGenEdfaTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 4)
)
alpineGenEdfaTemperatureAlarm.setObjects(
      *(("ALPINE-GEN-CARD-EDFA-MIB", "gceTemperature"),
        ("ALPINE-GEN-CARD-EDFA-MIB", "geaiPumpTemperatureAlarm"),
        ("ALPINE-GEN-CARD-EDFA-MIB", "geaiCaseTemperatureAlarm"))
)
if mibBuilder.loadTexts:
    alpineGenEdfaTemperatureAlarm.setStatus(
        "current"
    )

alpineGenEdfaBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 5)
)
alpineGenEdfaBiasAlarm.setObjects(
    ("ALPINE-GEN-CARD-EDFA-MIB", "geaiPumpBiasAlarm")
)
if mibBuilder.loadTexts:
    alpineGenEdfaBiasAlarm.setStatus(
        "current"
    )

alpineGenEdfaLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 52326, 1, 1, 2, 6)
)
alpineGenEdfaLossAlarm.setObjects(
    ("ALPINE-GEN-CARD-EDFA-MIB", "geaiLossInputAlarm")
)
if mibBuilder.loadTexts:
    alpineGenEdfaLossAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPINE-GEN-CARD-EDFA-MIB",
    **{"alpineGenCardEdfa": alpineGenCardEdfa,
       "alpineGenCardEdfaInfosTable": alpineGenCardEdfaInfosTable,
       "alpineGenCardEdfaInfosEntry": alpineGenCardEdfaInfosEntry,
       "gceSlotNum": gceSlotNum,
       "gceEdfaNum": gceEdfaNum,
       "gceMode": gceMode,
       "gceOutputPowerTarget": gceOutputPowerTarget,
       "gceGainTarget": gceGainTarget,
       "gceOutputPower": gceOutputPower,
       "gceGain": gceGain,
       "gceTemperature": gceTemperature,
       "gceSaveConfig": gceSaveConfig,
       "gceInputPower": gceInputPower,
       "alpineGenCardEdfaAlarm": alpineGenCardEdfaAlarm,
       "alpineGenCardEdfaAlarmThldTable": alpineGenCardEdfaAlarmThldTable,
       "alpineGenCardEdfaAlarmThldEntry": alpineGenCardEdfaAlarmThldEntry,
       "gceaSlotNum": gceaSlotNum,
       "gceaEdfaNum": gceaEdfaNum,
       "gceaInputPowerThld": gceaInputPowerThld,
       "gceaOutputPowerThld": gceaOutputPowerThld,
       "gceaTemperatureThld": gceaTemperatureThld,
       "alpineGenEdfaAlarmInfoTable": alpineGenEdfaAlarmInfoTable,
       "alpineGenEdfaAlarmInfoEntry": alpineGenEdfaAlarmInfoEntry,
       "geaiSlotNum": geaiSlotNum,
       "geaiEdfaNum": geaiEdfaNum,
       "geaiCommonAlarm": geaiCommonAlarm,
       "geaiCaseTemperatureAlarm": geaiCaseTemperatureAlarm,
       "geaiPumpTemperatureAlarm": geaiPumpTemperatureAlarm,
       "geaiPumpBiasAlarm": geaiPumpBiasAlarm,
       "geaiLossInputAlarm": geaiLossInputAlarm,
       "geaiLossOutputAlarm": geaiLossOutputAlarm,
       "alpineGenEdfaPowerAlarm": alpineGenEdfaPowerAlarm,
       "alpineGenEdfaTemperatureAlarm": alpineGenEdfaTemperatureAlarm,
       "alpineGenEdfaBiasAlarm": alpineGenEdfaBiasAlarm,
       "alpineGenEdfaLossAlarm": alpineGenEdfaLossAlarm}
)
