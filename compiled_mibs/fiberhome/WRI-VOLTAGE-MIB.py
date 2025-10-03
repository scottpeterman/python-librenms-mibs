# SNMP MIB module (WRI-VOLTAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-VOLTAGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:15 2025
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

msppVoltage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7)
)
if mibBuilder.loadTexts:
    msppVoltage.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_VoltageGeneral_ObjectIdentity = ObjectIdentity
voltageGeneral = _VoltageGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 1)
)


class _VoltageTrapEnable_Type(Integer32):
    """Custom type voltageTrapEnable based on Integer32"""
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


_VoltageTrapEnable_Type.__name__ = "Integer32"
_VoltageTrapEnable_Object = MibScalar
voltageTrapEnable = _VoltageTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 1, 1),
    _VoltageTrapEnable_Type()
)
voltageTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageTrapEnable.setStatus("current")


class _VoltageMonitorEnable_Type(Integer32):
    """Custom type voltageMonitorEnable based on Integer32"""
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


_VoltageMonitorEnable_Type.__name__ = "Integer32"
_VoltageMonitorEnable_Object = MibScalar
voltageMonitorEnable = _VoltageMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 1, 2),
    _VoltageMonitorEnable_Type()
)
voltageMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageMonitorEnable.setStatus("current")
_VoltageNumber_Type = Integer32
_VoltageNumber_Object = MibScalar
voltageNumber = _VoltageNumber_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 1, 3),
    _VoltageNumber_Type()
)
voltageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNumber.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1)
)
voltageEntry.setIndexNames(
    (0, "WRI-VOLTAGE-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Unsigned32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")


class _VoltageDescr_Type(DisplayString):
    """Custom type voltageDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VoltageDescr_Type.__name__ = "DisplayString"
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 2),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_VoltageLThreshold_Type = Integer32
_VoltageLThreshold_Object = MibTableColumn
voltageLThreshold = _VoltageLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 3),
    _VoltageLThreshold_Type()
)
voltageLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageLThreshold.setStatus("current")
_VoltageHThreshold_Type = Integer32
_VoltageHThreshold_Object = MibTableColumn
voltageHThreshold = _VoltageHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 4),
    _VoltageHThreshold_Type()
)
voltageHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageHThreshold.setStatus("current")
_VoltageValue_Type = Integer32
_VoltageValue_Object = MibTableColumn
voltageValue = _VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 5),
    _VoltageValue_Type()
)
voltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageValue.setStatus("current")


class _VoltageState_Type(Integer32):
    """Custom type voltageState based on Integer32"""
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
          ("lowtrap", 1),
          ("hightrap", 2))
    )


_VoltageState_Type.__name__ = "Integer32"
_VoltageState_Object = MibTableColumn
voltageState = _VoltageState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 6),
    _VoltageState_Type()
)
voltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageState.setStatus("current")


class _VoltageTrapEna_Type(Integer32):
    """Custom type voltageTrapEna based on Integer32"""
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


_VoltageTrapEna_Type.__name__ = "Integer32"
_VoltageTrapEna_Object = MibTableColumn
voltageTrapEna = _VoltageTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 7),
    _VoltageTrapEna_Type()
)
voltageTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageTrapEna.setStatus("current")
_VoltageAllSetting_Type = OctetString
_VoltageAllSetting_Object = MibTableColumn
voltageAllSetting = _VoltageAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 8),
    _VoltageAllSetting_Type()
)
voltageAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageAllSetting.setStatus("current")
_VoltageIndexDescr_Type = OctetString
_VoltageIndexDescr_Object = MibTableColumn
voltageIndexDescr = _VoltageIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 2, 1, 9),
    _VoltageIndexDescr_Type()
)
voltageIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndexDescr.setStatus("current")
_VoltageTrap_ObjectIdentity = ObjectIdentity
voltageTrap = _VoltageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 3)
)

# Managed Objects groups


# Notification objects

voltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 3, 1)
)
voltageOk.setObjects(
      *(("WRI-VOLTAGE-MIB", "voltageDescr"),
        ("WRI-VOLTAGE-MIB", "voltageValue"))
)
if mibBuilder.loadTexts:
    voltageOk.setStatus(
        "current"
    )

voltageFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 7, 3, 2)
)
voltageFault.setObjects(
      *(("WRI-VOLTAGE-MIB", "voltageDescr"),
        ("WRI-VOLTAGE-MIB", "voltageValue"),
        ("WRI-VOLTAGE-MIB", "voltageLThreshold"),
        ("WRI-VOLTAGE-MIB", "voltageHThreshold"))
)
if mibBuilder.loadTexts:
    voltageFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-VOLTAGE-MIB",
    **{"DisplayString": DisplayString,
       "mspp": mspp,
       "msppChassis": msppChassis,
       "msppVoltage": msppVoltage,
       "voltageGeneral": voltageGeneral,
       "voltageTrapEnable": voltageTrapEnable,
       "voltageMonitorEnable": voltageMonitorEnable,
       "voltageNumber": voltageNumber,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageDescr": voltageDescr,
       "voltageLThreshold": voltageLThreshold,
       "voltageHThreshold": voltageHThreshold,
       "voltageValue": voltageValue,
       "voltageState": voltageState,
       "voltageTrapEna": voltageTrapEna,
       "voltageAllSetting": voltageAllSetting,
       "voltageIndexDescr": voltageIndexDescr,
       "voltageTrap": voltageTrap,
       "voltageOk": voltageOk,
       "voltageFault": voltageFault}
)
